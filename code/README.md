# Informazioni aggiuntive del codice
## Installazione librerie
Per utilizzare il dataset direttamente da Python, installa la libreria `ucimlrepo`:

```bash
pip install ucimlrepo
```
Questa libreria consente di caricare i dataset del [UCI Machine Learning Repository](https://archive.ics.uci.edu/).

Per elaborazione e il preprocessing delle immagini, installa la libreria `scikit-image`:
```bash
pip install -U scikit-image
```
Questa libreria offre strumenti per il preprocessing e l’analisi delle immagini: ridimensionamento e normalizzazione, filtraggio/denoising, estrazione di feature (bordi, texture) e varie trasformazioni/visualizzazioni.

## Spiegazioni file
La struttura del progetto è organizzata in più file, ognuno con un compito specifico:

### `uploading_dataset.py`
In questo file viene gestito il caricamento del dataset **Optical Recognition of Handwritten Digits** dal UCI Machine Learning Repository tramite la libreria `ucimlrepo`. Il codice separa le **feature** (valori numerici dei pixel 8×8) dal **target** (cifra corretta da 0 a 9) e mostra le dimensioni del dataset. Sono inoltre disponibili funzioni per visualizzare i metadati e le variabili del dataset.

### `show_digit.py`
In questo file vengono mostrate alcune cifre del dataset in una griglia (8×10). Ogni immagine è ricostruita dalle feature numeriche (64 valori → matrice 8×8) e visualizzata in scala di grigi, con la sua etichetta corretta come titolo. Serve per esplorare visivamente il dataset e verificare che i dati siano caricati correttamente.

### `block_reduce.py`
In questo file viene mostrato come un’immagine 32×32 può essere ridotta a una matrice 8×8. Ogni blocco 4×4 viene sostituito dal conteggio dei pixel neri (valori da 0 a 16). Questa procedura riproduce il preprocessing originale del dataset Optical Recognition of Handwritten Digits.

### `mnistify_digit.py`
In questo file viene mostrato come un’immagine del dataset UCI (8×8) può essere trasformata in formato MNIST (32×32). La procedura include normalizzazione, ridimensionamento, blur e aumento del contrasto, con visualizzazione finale della cifra e griglia 4×4.

### `pixel_upscale.py`
In questo file viene mostrato come un’immagine 8×8 del dataset UCI può essere ingrandita a 32×32 replicando i pixel. La visualizzazione affianca l’immagine upscaled con griglia 4×4 e la matrice originale 8×8 con i valori numerici (0–16).

### `spectral_cluster.py`
In questo file applichiamo Spectral Clustering per raggruppare le cifre scritte a mano in 10 cluster non supervisionati, visualizzati in 2D tramite PCA. Una mappatura manuale tra cluster e cifre reali consente il confronto diretto con le etichette originali, evidenziando la coerenza tra gruppi trovati e classi attese.

### `confusion_matrix.py`
In questo file viene mostrata la matrice di confusione che mostra la corrispondenza tra i cluster non supervisionati ottenuti tramite Spectral Clustering e le etichette reali delle cifre. Ogni cella indica quanti campioni con una certa etichetta sono stati assegnati a ciascun cluster, permettendo di valutare la coerenza tra gruppi trovati e classi attese.

### `random_forest.py`
In questo file viene addestrato un classificatore Random Forest per il riconoscimento di cifre scritte a mano, valutandone le prestazioni tramite accuratezza, report di classificazione e visualizzazione della matrice di confusione.
