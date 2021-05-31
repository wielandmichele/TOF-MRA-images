# Verwendung von 3D CNNs zur Prognose von Therapieergebnissen bei Schlaganfall-Patienten mithilfe von TOF-MRA Bildern
Dieses Repository beinhaltet den Code, welchen ich für die Modelle in meiner Bachelorarbeit verwendet habe. 

Die Ordner beinhalten Folgendes:
- Funktionen: Beinhaltet Funktionen, welche in mehreren Skripten verwendet wurden.
- Deskriptive Analyse: Beinhaltet den Code, um die Rohdaten zu analysieren. 
- Datenaufbereitung: Beinhaltet den Code, um die Rohdaten (DICOM Bilder und Labels) in einem HDF5-File zu speichern und die Schritte zur Datenaufbereitung, welcher in der Bachelorarbeit beschrieben werden (einheitliche Bildgrösse, Normalisierung der Signalwerte und Erweiterung der Dimension).
- Modelle: Beinhaltet das Modell für die Schlaganfall Detektion und das Modell für die Outcome-Prognose.
