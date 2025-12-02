from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y['class'], test_size=0.2, random_state=42, stratify=y['class']
)

# Random Forest
rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    random_state=42
)

rf.fit(X_train, y_train)

# Predizioni 
y_pred = rf.predict(X_test)

# Accuracy random forest
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy Random Forest: {acc:.4f}")

# Classification Report 
# Ottieni report come dict
report = classification_report(y_test, y_pred, output_dict=True)

# Converti in DataFrame
df_report = pd.DataFrame(report).transpose()

df_report = df_report.iloc[:-3]

plt.figure(figsize=(10, 6))
sns.heatmap(df_report, annot=True, cmap="viridis", fmt=".2f", cbar=False)
plt.title("Classification Report - Random Forest")
plt.show()

# Confusion Matrix 
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10,7))
sns.heatmap(cm, annot=True, fmt="d", cmap="viridis")
plt.xlabel("Predetto")
plt.ylabel("Reale")
plt.title("Matrice di Confusione - Random Forest")
plt.show()
