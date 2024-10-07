import numpy as np
import pickle
import mne
import os

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
freqs = [[1, 4], [4, 8], [8, 14], [14, 30], [30, 47]]

# Process data and save each subject's DE features as a separate .pkl file
output_dir = r''
os.makedirs(output_dir, exist_ok=True)

for sub in range(n_subs):
    de_sub = np.zeros((64, n_vids * 30, len(freqs)))
    for i in range(len(freqs)):
        print('Current freq band:', freqs[i])
        for j in range(n_vids):
            data_video = data[sub, j, :, :]
            print(data_video.shape)
            low_freq = freqs[i][0]
            high_freq = freqs[i][1]
            data_video_filt = mne.filter.filter_data(data_video, fs, l_freq=low_freq, h_freq=high_freq)
            data_video_filt = data_video_filt.reshape(64, -1, fs)
            de_one = 0.5 * np.log(2 * np.pi * np.exp(1) * (np.var(data_video_filt, 2)))
            de_sub[:, 30 * j: 30 * (j + 1), i] = de_one

    output_path = os.path.join(output_dir, f'_de.pkl')
    with open(output_path, 'wb') as f:
        pickle.dump({'de': de_sub}, f)

    print(f'Subject  DE features saved to {output_path}')
