# Autonome_Modelfahrzeuge_Lageabschaetzung
### siehe Dokumentation_lageabschaetzung.pdf

Für dieses Projekt gab es 4 Gruppen:

1- lokale Positionsabschätzung mit Beschl.-Sensor / Zweifachintegrierte Beschleunigung:
linearer Versuchsstand → Abschätzung der möglichen Genauigkeit
Fusion Aruco Position (von Kamera, Datenupdate im einstelligen Hz-Bereich) + doppelt integrierter Beschleunigungssensor

2-lokale Lageabschätzung mit Gyro / Integrierte Winkelgeschwindigkeit:
Versuchsstand zur Abschätzung der Gyro-Drift
Fusion Aruco-Heading mit integrierter Winkelgeschwindigkeit

3-Rechenmodell in Matlab des Cars erstellen und Modellgenauigkeit verifizieren. Damit kann dann der Regler optimiert werden.

4-Diverse Navigationsmethoden recherchieren und möglichst drei testen

Meine Gruppe hat sich mit der Lageabschaetzung beschäftigt:

1. Gyroskop und Winkelgeschwindigkeit
Ein Gyroskop misst die Winkelgeschwindigkeit, also die Geschwindigkeit, mit der sich das Fahrzeug um eine oder mehrere Achsen dreht. In einem autonomen Modellfahrzeug ist dies wichtig, um die Ausrichtung (Lage) des Fahrzeugs im Raum zu kennen. Diese Winkelgeschwindigkeit wird in der Regel kontinuierlich gemessen.

2. Integrierte Winkelgeschwindigkeit
Durch die Integration der Winkelgeschwindigkeit kann man die aktuelle Orientierung (bzw. den Winkel) des Fahrzeugs bestimmen. Das bedeutet, dass die gemessene Winkelgeschwindigkeit über die Zeit summiert wird, um die Gesamtrotation zu berechnen. Diese Methode hat allerdings ihre Grenzen, da kleine Messfehler im Gyroskop (z. B. Rauschen oder Drift) zu großen Abweichungen führen können, wenn sie über einen längeren Zeitraum integriert werden.

3. Gyro-Drift und Versuchstand zur Abschätzung
Ein großes Problem bei Gyroskopen ist der sogenannte Drift. Dies bedeutet, dass über die Zeit auch ohne tatsächliche Bewegung eine falsche Rotation gemessen werden kann. Der Drift entsteht durch Ungenauigkeiten im Sensor, die sich im Laufe der Zeit aufsummieren. In eurem Projekt werdet ihr wahrscheinlich einen Versuchsstand nutzen, um diesen Drift systematisch zu untersuchen. Ihr werdet Daten sammeln, um zu sehen, wie sich der Drift über die Zeit verhält, und so einen Korrekturfaktor bestimmen.

4. Fusion von Aruco-Heading und integrierter Winkelgeschwindigkeit
Da die Gyroskop-Daten allein aufgrund des Drifts nicht ausreichen, wird eine Sensorfusion angewandt. Dabei nutzt man die Position und Ausrichtung, die mit Hilfe von Aruco-Markern erfasst wird, um den Drift zu korrigieren. Ein Aruco-Marker ist ein optisches Erkennungssystem (ähnlich wie QR-Codes), das mit einer Kamera verwendet wird, um die Position und Ausrichtung des Fahrzeugs zu bestimmen.

Aruco-Heading: Die Kamera am Fahrzeug erkennt den Aruco-Marker und bestimmt die Ausrichtung (Heading) relativ zu diesem Marker.

Fusion: Diese Daten werden mit der integrierten Winkelgeschwindigkeit kombiniert, um eine genauere Schätzung der Fahrzeugausrichtung zu erhalten. Dies geschieht in einem Kalman-Filter oder einem ähnlichen Algorithmus, der verschiedene Sensoren miteinander fusioniert, um die beste Schätzung zu bekommen.


