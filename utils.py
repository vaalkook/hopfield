import numpy as np

def sign(x):
    return np.where(x >= 0, 1, -1)

def recall(pattern, W, steps=5):
    N = pattern.size
    s = pattern.reshape(N, 1)
    for _ in range(steps):
        s = sign(W @ s)
    return s.reshape(pattern.shape)

def add_noise(pattern, percent=0.3):
    noisy = pattern.copy()
    n = int(noisy.size * percent)
    idx = np.random.choice(noisy.size, n, replace=False)
    noisy.flat[idx] *= -1
    return noisy
