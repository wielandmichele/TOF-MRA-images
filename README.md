# Verwendung von 3D CNNs zur Prognose von Therapieergebnissen bei Schlaganfall-Patienten mithilfe von TOF-MRA Bildern
Dieses Repository beinhaltet den Code, welchen ich in meiner Bachelorarbeit verwendet habe. 

### Die Ordner beinhalten Folgendes:
- Functions: Beinhaltet Funktionen, welche in mehreren Skripten verwendet wurden.
- Deskriptive Analyse: Beinhaltet den Code, um die Rohdaten zu analysieren. 
- Datenaufbereitung: Beinhaltet den Code, um die Rohdaten (DICOM Bilder und Labels) in einem HDF5-File zu speichern und die Schritte zur Datenaufbereitung, welcher in der Bachelorarbeit beschrieben werden (einheitliche Bildgrösse, Normalisierung der Signalwerte und Erweiterung der Dimension).
- Modelle: Beinhaltet für die Schlaganfall Detektion und die Outcome Prognose die Hyperparameter Optimierung, die 5-fache Kreuzvalidierung und das Ensembling-Modell.
