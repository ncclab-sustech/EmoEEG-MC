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

# close the file
edf_file.close()
