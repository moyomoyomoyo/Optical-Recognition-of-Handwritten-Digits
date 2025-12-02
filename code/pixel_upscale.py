import numpy as np
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
from skimage.util import view_as_blocks

# SELEZIONE CIFRA "6"
# Trova un indice qualsiasi di un '6'
idx6 = np.where(y['class'] == 6)[0][0]

# Estraggo i valori 8×8
img8 = np.array(X.iloc[idx6]).reshape((8, 8))

# Upscaling: da 8x8 a 32x32 (ripetizione pixel x4)
image32 = np.kron(img8, np.ones((4, 4)))  # ingrandimento
image32_norm = image32 / 16               # normalizzazione 0–1 per visualizzare bene

# Visualizzo:
# 32×32 con griglia
# 8×8 con valori
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Immagine upscaled 32x32 con griglia 4×4
ax[0].imshow(image32_norm, cmap='gray_r', vmin=0, vmax=1)
ax[0].set_title("Immagine ridotta a 8x8")
ax[0].axis('off')

for x in range(0, 32, 4):
    ax[0].axhline(x - 0.5, color='red', linewidth=0.5)
    ax[0].axvline(x - 0.5, color='red', linewidth=0.5)

# Matrice 8×8 con valori 0–16 
ax[1].imshow(img8, cmap='gray_r', vmin=0, vmax=16)
for i in range(8):
    for j in range(8):
        ax[1].text(j, i, int(img8[i, j]),
                   ha='center', va='center',
                   color='red', fontsize=8)
ax[1].set_title("Valori 8×8 (0–16)")
ax[1].axis('off')

plt.tight_layout()
plt.show()
