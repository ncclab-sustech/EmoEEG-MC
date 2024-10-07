import numpy as np
import h5py
import scipy.io as sio
import pickle
import mne
import os
from scipy.signal import welch

# Load the data
data_path = r'_reorder.pkl'
# data_paths = os.listdir(data_path)
# data_paths.sort()

n_subs = 1
n_vids = 21
chn = 64
fs = 200
sec = 30
data = np.zeros((n_subs, n_vids, chn, fs * sec))

# for idx, path in enumerate(data_paths):
#     with open(os.path.join(data_path, path), 'rb') as f:
#         data_sub = pickle.load(f)
#         data[idx, :, :, :] = data_sub[:, :, :].transpose([1, 0, 2])

with open(data_path, 'rb') as f:
        data_sub = pickle.load(f)
        data[0, :, :, :] = data_sub[:, :, :].transpose([1, 0, 2])

# data shape: (sub, vid, chn, fs * sec)
print('Data loaded:', data.shape)

n_subs = data.shape[0]
fs = 200
freq_bands = [[1, 4], [4, 8], [8, 14], [14, 30], [30, 47]]

# Process data and save each subject's PSD features as a separate .pkl file
output_dir = r''
os.makedirs(output_dir, exist_ok=True)

for sub in range(n_subs):
    psd_sub = np.zeros((64, n_vids * 30, len(freq_bands)))
    for i, (low_freq, high_freq) in enumerate(freq_bands):
        print('Current freq band:', (low_freq, high_freq))
        for j in range(n_vids):
            data_video = data[sub, j, :, :]
            print(data_video.shape)
            data_video_filt = mne.filter.filter_data(data_video, fs, l_freq=low_freq, h_freq=high_freq)
            data_video_filt = data_video_filt.reshape(64, -1, fs)
            for ch in range(64):
                f, Pxx = welch(data_video_filt[ch], fs=fs, nperseg=58)
                band_power = np.mean(Pxx[(f >= low_freq) & (f <= high_freq)])
                psd_sub[ch, 30 * j: 30 * (j + 1), i] = band_power

    output_path = os.path.join(output_dir, f'_psd.pkl')
    with open(output_path, 'wb') as f:
        pickle.dump({'psd': psd_sub}, f)

    print(f'Subject  PSD features saved to {output_path}')
