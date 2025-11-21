from sklearn.cluster import SpectralClustering
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Riduzione dimensionale per visualizzare
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Spectral Clustering con 10 cluster (0–9)
spectral = SpectralClustering(
    n_clusters=10,
    affinity='nearest_neighbors',   # costruisce grafo di similarità
    assign_labels='kmeans',         # usa KMeans nello spazio spettrale
    random_state=42
)
clusters = spectral.fit_predict(X)

# Palette personalizzata
colors = [
    "#e6194b", "#3cb44b", "#ffe119", "#0082c8", "#f58231",
    "#911eb4", "#46f0f0", "#f032e6", "#d2f53c", "#fabebe"
]

cmap = ListedColormap(colors)

# Visualizzazione con PCA
plt.figure(figsize=(8,6))
scatter = plt.scatter(
    X_pca[:, 0], X_pca[:, 1],
    c=clusters, cmap=cmap, alpha=0.6
)
plt.title("Clustering delle cifre (PCA + Spectral Clustering)")

# Aggiunta della colorbar con etichette dei cluster
cbar = plt.colorbar(scatter, ticks=range(10))
cbar.set_label("Cluster")
cbar.set_ticks(range(10))
cbar.set_ticklabels([str(i) for i in range(10)])

plt.show()
