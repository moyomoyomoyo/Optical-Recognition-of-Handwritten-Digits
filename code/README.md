# Informazioni aggiuntive per codice
## Installazione librerie
Per utilizzare il dataset direttamente da Python, installa la libreria `ucimlrepo`:

```bash
pip install ucimlrepo
```
Questa libreria consente di caricare i dataset del [UCI Machine Learning Repository](https://archive.ics.uci.edu/).

Per elaborazione e il preprocessing delle immagine, installa la libreria `scikit-image`:
```bash
pip install -U scikit-image
```
Questa libreria offre strumenti per il preprocessing e l’analisi delle immagini: 
ridimensionamento e normalizzazione, filtraggio/denoising, estrazione di feature (bordi, texture) e varie trasformazioni/visualizzazioni.

## Spiegazioni file
### `uploading_dataset.py`
In questo file viene gestito il caricamento del dataset **Optical Recognition of Handwritten Digits** dal UCI Machine Learning Repository tramite la libreria `ucimlrepo`. Il codice separa le **feature** (valori numerici dei pixel 8×8) dal **target** (cifra corretta da 0 a 9) e mostra le dimensioni del dataset. Sono inoltre disponibili funzioni per visualizzare i metadati e le variabili del dataset.


