import math
import cv2 as cv
import signal



def signal_handler(signum, frame):

    exit(0)


def main():   

    signal.signal(signal.SIGINT, signal_handler)

    cam = cv.VideoCapture(0)
    
    angle_deg: float = 0

    aruco_dict = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_50)
    parameters = cv.aruco.DetectorParameters()
    detector = cv.aruco.ArucoDetector(aruco_dict, parameters)

    while 1:
        
        ret, frame = cam.read()
        #print(frame)
        if ret==True:

            rgb_to_gray= cv.COLOR_BGR2GRAY
            image = cv.cvtColor(frame, rgb_to_gray)

        corners, ids, rejected = detector.detectMarkers(image)

        if ids is None:
            print("Kein Aruco Marker erkannt")
            continue

        for i in range(len(ids)):
            print(f"Marker {i+1} : {ids[i]}")

            print(f"Koordinaten der Ecken des Markers {corners[i]}")

            angle_deg= get_angle(corners[i][0])

            print(f"Winkel des Markers {ids[i]}: {angle_deg:.2f}")
            print("============================================================")




def get_angle(corners):
    """
    Berechnet den winkel aus den koordinaten
    der Eckpunkte des Markers
    Eingabe: Eckpunkte
    Ausgabe: Winkel in 0°-360°
    """
        
    a= (corners[0] + corners[1])/ 2

    print(f"Koordinaten vom Mittelpunkt A der oberen Seite : {a}")

    b= (corners[0] + corners[2])/ 2

    print(f"Koordinaten vom Mittelpunkt M des Markers: {b}")
    
    r = a - b

    print(f"Koordinaten vom Richtungsvektor r: {r}")

    angle = math.asin(r[1]/ (math.sqrt(r[0]**2 + r[1]**2)) )
    angle = angle / math.pi * 180

    # Winkel im Bereich 0°-360° umrechnen
    #""""
    if r[0] >= 0 : 

        angle = 270-angle

    elif r[0] <= 0:

        angle =  angle + 90   
    #"""
    return angle
        


if __name__== "__main__":
    main() 
