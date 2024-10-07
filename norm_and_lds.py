import numpy as np

def running_norm(data, bn_val, n_counters, data_mean, data_var, decay_rate):
    data_norm = np.zeros_like(data)
    for sub in range(data.shape[0]):
        running_sum = np.zeros(data.shape[-1])
        running_square = np.zeros(data.shape[-1])
        decay_factor = 1.
        for counter in range(n_counters):
            data_one = data[sub, counter*bn_val: (counter+1)*bn_val, :]
            running_sum = running_sum + data_one
            running_mean = running_sum / (counter+1)
            running_square = running_square + data_one**2
            running_var = (running_square - 2 * running_mean * running_sum) / (counter+1) + running_mean**2

            curr_mean = decay_factor*data_mean + (1-decay_factor)*running_mean
            curr_var = decay_factor*data_var + (1-decay_factor)*running_var
            decay_factor = decay_factor*decay_rate

            data_one = (data_one - curr_mean) / np.sqrt(curr_var + 1e-5)
            data_norm[sub, counter*bn_val: (counter+1)*bn_val, :] = data_one

    return data_norm

def LDS(sequence):
    ave = np.mean(sequence, axis=0)  
    u0 = ave
    X = sequence.transpose((1, 0))  

    V0 = 0.01
    A = 1
    T = 0.0001
    C = 1
    sigma = 1

    [m, n] = X.shape 
    P = np.zeros((m, n))  
    u = np.zeros((m, n)) 
    V = np.zeros((m, n)) 
    K = np.zeros((m, n)) 

    K[:, 0] = (V0 * C / (C * V0 * C + sigma)) * np.ones((m,))
    u[:, 0] = u0 + K[:, 0] * (X[:, 0] - C * u0)
    V[:, 0] = (np.ones((m,)) - K[:, 0] * C) * V0

    for i in range(1, n):
        P[:, i - 1] = A * V[:, i - 1] * A + T
        K[:, i] = P[:, i - 1] * C / (C * P[:, i - 1] * C + sigma)
        u[:, i] = A * u[:, i - 1] + K[:, i] * (X[:, i] - C * A * u[:, i - 1])
        V[:, i] = (np.ones((m,)) - K[:, i] * C) * P[:, i - 1]

    X = u

    return X.transpose((1, 0))
