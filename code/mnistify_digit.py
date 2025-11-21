import numpy as np
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
from skimage.transform import resize
from scipy.ndimage import gaussian_filter

# Prende un "6" dal dataset UCI
idx6 = np.where(y['class'] == 6)[0][0]
img8 = np.array(X.iloc[idx6]).reshape((8, 8))
img8_norm = img8 / 16  # normalizzazione

# Scaling → 32x32
img32 = resize(img8_norm, (32, 32), order=1, anti_aliasing=True)

# Applicazione stile MNIST
img32 = gaussian_filter(img32, sigma=1.8)  # più blur
img32 = 1 - img32                          # sfondo nero come MNIST
img32 = img32 ** 2.2                       # aumenta contrasto

# Visualizzazione immagine
plt.figure(figsize=(5,5))
plt.imshow(img32, cmap='gray')
plt.title("Cifra UCI stile MNIST (32×32)")
plt.axis('off')

# Aggiunta griglia 4x4
size = 32
for x in range(0, size, 4):
    plt.axhline(x-0.5, color = 'red', linewidth = 0.5)
    plt.axvline(x-0.5, color = 'red', linewidth = 0.5)

plt.show()
