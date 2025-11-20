# Optical Recognition of Handwritten Digits
Riconoscimento delle cifre numeriche scritte a mano (0-9).

## Descrizione
Come dataset è stato utilizzato **Optical Recognition of Handwritten Digits** ottenuto dal sito UCI Machine Learning Repository.
L'obiettivo è identificare correttamente le cifre scritte a mano partendo da immagini rasterizzate.

## Origine del dataset
Il dataset utilizzato è stato donato al sito dell'UCI Machine Learning Repository nel 1998. I dati derivano da immagini di cifre scritte a mano raccolte da **43 persone**: 30 hanno contribuito al training set e 13 al test set.

## Dataset
- *Fonte*: [UCI Optical Recognition of Handwritten Digits](https://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits)
- *Numero di istanze*: 5620 
- *Numero di feature*: 64 (valori dei pixel)
- *Tipo di feature*: interi (0-16)
- *Target*: cifre da 0 a 9
- *Classi bilanciate*: ogni cifra ha circa 380 esempi nel training set e ~180 nel test set

## Preprocessing
Le immagini originali erano **bitmap 32x32**; sono state suddivise in blocchi **4x4**, contando i pixel attivi ("on pixels"). Questo ha generato una matrice **8x8** con valori interi tra **0 e 16**, riducendo la dimensionalità e rendendo il riconscimento più robusto a piccole distorsioni.
