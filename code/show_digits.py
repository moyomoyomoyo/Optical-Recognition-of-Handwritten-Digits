# ogni riga rappresenta un'immagine 8x8 di una cifra scritta a mano (valori da 0 a 9)
import matplotlib.pyplot as plt
import numpy as np

# Mostra alcune cifre casuali
n_images = 80   # quante immagini vuoi mostrare
rows = 8        # numero di righe nella griglia
cols = 10       # numero di colonne nella griglia

plt.figure(figsize=(24, 20))  # aumenta la dimensione del grafico

for i in range(n_images):
    plt.subplot(rows, cols, i + 1)
    img = np.array(X.iloc[i]).reshape(8, 8)
    plt.imshow(img, cmap='gray')
    plt.title(f"#{y.iloc[i, 0]}", fontsize=26)
    plt.axis('off')

plt.tight_layout()
plt.show()
