from sklearn.cluster import SpectralClustering
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

# ---- PCA per visualizzazione ----
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# ---- Spectral Clustering ----
spectral = SpectralClustering(
    n_clusters=10,
    affinity='nearest_neighbors',
    assign_labels='kmeans',
    random_state=42
)
clusters = spectral.fit_predict(X)

# ---- MAPPING CLUSTER -> CIFRE REALI ----
mapping = {
    0: 7, 1: 8, 2: 5, 3: 9, 4: 2,
    5: 6, 6: 0, 7: 3, 8: 4, 9: 1
}

clusters_mapped = np.array([mapping[c] for c in clusters])

colors = [
    "#000000", "#D4A017", "#023D1F", "#8C3B00", "#6A2E8A", 
    "#C75AFF", "#005F7F", "#00A88A", "#FF6A3D", "#A6A6A6"
]

cmap = ListedColormap(colors)

# ---- GRAFICO CLUSTER RIMAPPATI ----
plt.figure(figsize=(8,6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters_mapped, cmap=cmap, alpha=0.6)
plt.title("Clustering (colori mappati sulle cifre reali)")
plt.colorbar()
plt.show()

# ---- GRAFICO CLASSI REALI ----
plt.figure(figsize=(8,6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y['class'], cmap=cmap, alpha=0.6)
plt.title("Etichette reali (PCA)")
plt.colorbar()
plt.show()
