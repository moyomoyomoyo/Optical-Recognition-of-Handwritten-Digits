import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

conf = pd.crosstab(y['class'], clusters)
plt.figure(figsize=(8,6))
sns.heatmap(conf, annot=True, fmt="d", cmap="viridis")
plt.xlabel("Cluster")
plt.ylabel("Etichetta Reale")
plt.title("Matrice di Confusione (Cluster vs Label)")
plt.show()
