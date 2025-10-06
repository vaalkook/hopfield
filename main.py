import numpy as np
import matplotlib.pyplot as plt
from hopfield_numeros import num_9, num_7, num_5, num_6

patterns = [num_9, num_7, num_5, num_6]

N = patterns[0].size
W = np.zeros((N, N))
for p in patterns:
    x = p.reshape(N, 1)
    W += x @ x.T
np.fill_diagonal(W, 0)

def sign(x):
    return np.where(x >= 0, 1, -1)

def recall(pattern, W, steps=5):
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

def show(img, title):
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')

test = add_noise(num_5, 0.4)
result = recall(test, W)

plt.figure(figsize=(6, 3))
plt.subplot(1, 2, 1)
show(test, "Entrada con ruido (5)")
plt.subplot(1, 2, 2)
show(result, "Salida recordada")
plt.show()
