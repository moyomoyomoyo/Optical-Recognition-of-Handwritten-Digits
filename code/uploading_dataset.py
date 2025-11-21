from ucimlrepo import fetch_ucirepo
import pandas as pd

# Caricamento dataset
optical_recognition_of_handwritten_digits = fetch_ucirepo(id=80) # id del dataset specifico per optical recognition of handwritten digits

# Dati e target
X = optical_recognition_of_handwritten_digits.data.features # X è la parte numerica del dataset: i dati che userai per addestrare i modelli di machine learning
y = optical_recognition_of_handwritten_digits.data.targets # y è la risposta corretta: dice quale numero è stato scritto a mano.

print("Shape delle feature:", X.shape) # 5620 righe × 64 colonne (valori di pixel 8×8)
print("Shape del target:", y.shape) # etichetta da 0 a 9 per ciascuna immagine

# # Visualizza metadati e variabili
# print("\nMetadata:")
# print(optical_recognition_of_handwritten_digits.metadata)

# print("\nInformazioni sulle variabili:")
# print(optical_recognition_of_handwritten_digits.variables)
