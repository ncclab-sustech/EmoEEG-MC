import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.decomposition import FastICA
import mne

def find_neighbors(ch_name, info):
    """
    Identifies neighboring channels for a given channel name based on the EEG montage.

    Parameters:
    - ch_name: str, the channel name to find neighbors for.
    - info: mne.Info, the info object containing channel and montage information.

    Returns:
    - neighbors: list of str, the names of neighboring channels.
    """
    adjacency_matrix, ch_names_adj = mne.channels.find_ch_adjacency(info, "eeg")
    ch_idx = ch_names_adj.index(ch_name)
    neighbors_idx = np.where(adjacency_matrix[ch_idx].toarray()[0])[0]
    neighbors = [ch_names_adj[idx] for idx in neighbors_idx]
    return neighbors

def repair_bad_channel_for_trial(trial_data, ch_idx, bad_channels, info):
    """
    Repairs bad channels by replacing their data with the average of their neighbors.

    Parameters:
    - trial_data: list of ndarray, the trial data for each channel.
    - ch_idx: int, index of the channel to be repaired.
    - bad_channels: list of str, names of channels identified as bad.
    - info: mne.Info, contains channels and montage info.

    Returns:
    - trial_data: list of ndarray, the modified trial data with repaired channels.
    """
    ch_name = info['ch_names'][ch_idx]
    if ch_name in bad_channels:
        print(f"Repairing: {ch_name}")
        neighbors = find_neighbors(ch_name, info)
        neighbors = [n for n in neighbors if n not in bad_channels]
        neighbor_data = [trial_data[info['ch_names'].index(n)] for n in neighbors]
        mean_neighbors = np.mean(neighbor_data, axis=0)
        trial_data[ch_idx] = mean_neighbors
    return trial_data

def average_reference(data):
    """
    Applies average reference to the data.

    Parameters:
    - data: ndarray, EEG data to be re-referenced.

    Returns:
    - re_referenced_data: ndarray, average-referenced data.
    """
    avg = np.mean(data, axis=0)
    re_referenced_data = data - avg
    return re_referenced_data

sub = 1  # Subject ID
trial = 21  # Number of trials

# Choose processing type
now_type = 'vid'  # 'ima' for imagination, 'vid' for video
now = 'ica'  # 'ica' for Independent Component Analysis

# Load EEG data
with open(f'sub{sub}.pkl', 'rb') as f:
    data = pickle.load(f)

# Splitting data into imagination and video based on index
ima_data = [channel_data[:trial] for idx, channel_data in enumerate(data) if idx % 2 == 0]
vid_data = [channel_data[:trial] for idx, channel_data in enumerate(data) if idx % 2 == 1]

# EEG setup
fs = 200  # Sampling frequency
ch_names = [
    'Fp1', 'Fpz', 'Fp2', 'AF7', 'AF3','AF4','AF8', 'F7', 'F5','F3','F1','Fz', 'F2', 'F4', 'F6', 'F8',
    'FT7', 'FC5', 'FC3', 'FC1','FCz','FC2','FC4', 'FC6', 'FT8', 'T7','C5', 'C3', 'C1', 'Cz', 'C2', 'C4', 'C6', 'T8',
    'TP7', 'CP5', 'CP3', 'CP1','CPz','CP2', 'CP4','CP6', 'TP8', 'P7','P5', 'P3', 'P1', 'Pz','P2', 'P4', 'P6', 'P8',
    'PO7', 'PO3','POz', 'PO4','PO8', 'O1','Oz','O2', 'F9', 'F10', 'TP9', 'TP10'
]
info = mne.create_info(ch_names=ch_names, sfreq=fs, ch_types='eeg')
montage = mne.channels.make_standard_montage('brainproducts-RNP-BA-128')
info.set_montage(montage)

# Initialize repaired data structures
n_ima_data = [list(trial) for trial in ima_data]
n_vid_data = [list(trial) for trial in vid_data]

# Specify bad channels
bad_channels = ['TP10']

# Repair bad channels for each trial
for trial_idx in range(trial):
    trial_data = n_ima_data[trial_idx] if now_type == 'ima' else n_vid_data[trial_idx]
    for ch_idx in range(64):
        trial_data = repair_bad_channel_for_trial(trial_data, ch_idx, bad_channels, info)
        if now_type == 'ima':
            n_ima_data[trial_idx] = trial_data
        else:
            n_vid_data[trial_idx] = trial_data

if now == 'ica':
    # Apply ICA and average reference
    processed_data = n_ima_data if now_type == 'ima' else n_vid_data
    all_trials_data = np.concatenate(processed_data, axis=1)
    raw_all_trials = mne.io.RawArray(all_trials_data, info)
    ica = mne.preprocessing.ICA(n_components=60, method='fastica', random_state=97, max_iter=800)
    ica.fit(raw_all_trials)

    # Plot ICA components and ask user for components to exclude
    ica.plot_sources(raw_all_trials)
    ica.plot_components(picks=range(60))
    exclude_comps = input("Enter components to exclude (e.g., '0,2,3'): ").split(',')
    ica.exclude = [int(comp) for comp in exclude_comps if comp]

    # Apply ICA correction
    raw_corrected = ica.apply(raw_all_trials, exclude=ica.exclude)
    corrected_data = average_reference(raw_corrected.get_data())

    # Save processed data
    file_name = f'sub{sub}_ica_{now_type}.pkl'
    with open(file_name, 'wb') as file:
        pickle.dump(corrected_data, file)
