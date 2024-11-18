import pyedflib
from scipy.signal import butter, filtfilt
from scipy.signal import resample

# example file path
file_path = r'\\10.16.32.74\dataset0\xuxin\EmoEEG\sub-60\eeg\sub-60_task-emotion_eeg.edf'

edf_file = pyedflib.EdfReader(file_path)

# get basic information of the EDF file
num_signals = edf_file.signals_in_file
print(f"Channels number: {num_signals}")

for i in range(num_signals):
    label = edf_file.getLabel(i)
    frequency = edf_file.getSampleFrequency(i)
    samples = edf_file.getNSamples()[i]
    duration = samples / frequency
    print(f"Num {i + 1}: channel_name = {label}, Frequency = {frequency} Hz, Samples = {samples}, Time = {duration:.2f} 秒")

# Annotations
try:
    onsets, durations, descriptions = edf_file.readAnnotations()
    
    print("Annotations :")
    for i in range(len(onsets)):
        print(f"Annotation {i + 1}:")
        print(f"  onset: {onsets[i]} s")
        print(f"  duration: {durations[i]} s")
        print(f"  description: {descriptions[i]}")
except AttributeError:
    print("No Annotation.")
    
# We can filter the raw data to 0.5-47Hz firstly.
def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    print("--------begin filter--------")
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='bandpass')
    y = filtfilt(b, a, data.astype(float))  # Convert to float
    return y
    
# TypeID and their corresponding meaning can be found in sub-idx\sub-idx_events.tsv.
# Based on the typeID, we can divide the EEG data into different trial segments.

# Then we can downsample the data to 200Hz.
def downsample_segment(segment, original_rate=frequency, target_rate=200):

    num_samples = len(segment)
    num_resampled_samples = int((num_samples * target_rate) / original_rate)
    return resample(segment, num_resampled_samples)

def process_eeg_data(samples, t_time, ima_segments, vid_segments, rate):
    """
    Process EEG data by segmenting and filtering based on given time indices.
    
    Args:
    samples (np.array): EEG signal data of shape (timepoints, channels).
    t_time (list): Time indices for synchronization.
    ima_segments (list): List of (start, end) indices for 'ima' sessions.
    vid_segments (list): List of (start, end) indices for 'vid' sessions.
    rate (int): Sampling rate of the EEG data.

    Returns:
    tuple: segmented_data, labels
        segmented_data (list): Processed and segmented data for each channel.
        labels (list): Corresponding labels for the segmented data.
    """
    # Initialize data storage for segmented data and labels
    segmented_data = []
    labels = []

    for channel_idx in range(64):
        # Extract data for the current channel
        channel_data = samples[:, channel_idx]

        # Apply bandpass filtering
        channel_data = butter_bandpass_filter(channel_data, 0.5, 47, rate, order=4)

        # Segment data for 'ima' session
        channel_segments_ima = []
        count = 0
        for start_idx, end_idx in ima_segments:
            # Calculate start and end timepoints
            sta = t_time[start_idx]
            print("Original start index (ima):", sta)
            end = t_time[end_idx] - rate

            # Adjust to ensure 30-second data length
            if end - 30 * rate > sta:
                sta = end - 30 * rate
            if end - sta < 30 * rate:
                o_end = end
                end = sta + 32 * rate
                print(f"Adjusted (ima) -> Start: {sta}, End: {end}, Original End: {o_end}")
                trial_data1 = channel_data[sta:(o_end - rate)]
                trial_data2 = channel_data[(o_end + rate):end]
                trial_data = np.concatenate((trial_data1, trial_data2), axis=0)
            else:
                print(f"Segment (ima) -> Start: {sta}, End: {end}")
                trial_data = channel_data[sta:end]

            # Downsample the segment
            trial_data = downsample_segment(trial_data)
            channel_segments_ima.append(trial_data)

            # Create a label for the segment
            labels.append('ima' + str(count))
            count += 1

        segmented_data.append(channel_segments_ima)

        # Segment data for 'vid' session
        channel_segments_vid = []
        count = 0
        for start_idx, end_idx in vid_segments:
            # Calculate start and end timepoints
            sta = t_time[start_idx]
            print("Original start index (vid):", sta)
            end = t_time[end_idx] - rate

            # Adjust to ensure 30-second data length
            if end - 30 * rate > sta:
                sta = end - 30 * rate
            if end - sta < 30 * rate:
                o_end = end
                end = sta + 32 * rate
                print(f"Adjusted (vid) -> Start: {sta}, End: {end}, Original End: {o_end}")
                trial_data1 = channel_data[sta:(o_end - rate)]
                trial_data2 = channel_data[(o_end + rate):end]
                trial_data = np.concatenate((trial_data1, trial_data2), axis=0)
            else:
                print(f"Segment (vid) -> Start: {sta}, End: {end}")
                trial_data = channel_data[sta:end]

            # Downsample the segment
            trial_data = downsample_segment(trial_data)
            channel_segments_vid.append(trial_data)

            # Create a label for the segment
            labels.append('vid' + str(count))
            count += 1

        segmented_data.append(channel_segments_vid)

        print(f"--------------- Channel {channel_idx} processing completed ---------------")

    return segmented_data, labels

# close the file
edf_file.close()
