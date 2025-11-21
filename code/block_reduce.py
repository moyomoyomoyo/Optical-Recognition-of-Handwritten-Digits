import numpy as np
import matplotlib.pyplot as plt
from skimage.util import view_as_blocks

# Creiamo un'immagine casuale 32x32 con valori 0 (bianco) e 1 (nero)
size = 32
image = np.random.randint(0, 2, (size, size))

# Dividiamo l'immagine in blocchi 4x4
blocks = view_as_blocks(image, block_shape=(4, 4))

# Calcoliamo il numero di pixel neri (1) in ogni blocco 4x4
reduced = blocks.sum(axis=(2, 3))

# Visualizziamo il processo
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# Immagine originale 32x32 con griglia 4x4
ax[0].imshow(image, cmap='gray_r', vmin=0, vmax=1)  # 0 bianco, 1 nero
ax[0].set_title("Originale 32×32 con griglia 4×4")
ax[0].axis('off')
# Aggiungiamo la griglia 4x4
for x in range(0, size, 4):
    ax[0].axhline(x-0.5, color='red', linewidth=0.5)
    ax[0].axvline(x-0.5, color='red', linewidth=0.5)

# Immagine ridotta 8x8 (valori 0–16)
ax[1].imshow(reduced, cmap='gray_r', vmin=0, vmax=16)
ax[1].set_title("Ridotta 8×8 (pixel neri 0–16)")
ax[1].axis('off')

# Visualizziamo anche i valori numerici su ogni blocco
ax[2].imshow(reduced, cmap='gray_r', vmin=0, vmax=16)
for i in range(8):
    for j in range(8):
        ax[2].text(j, i, reduced[i, j], ha='center', va='center', color='red', fontsize=8)
ax[2].set_title("Conteggio pixel neri per blocco (0–16)")
ax[2].axis('off')

plt.tight_layout()
plt.show()
