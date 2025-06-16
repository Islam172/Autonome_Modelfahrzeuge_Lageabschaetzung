import os
from datetime import datetime
import serial
import signal
import time


def signal_handler(signum, frame):
    
    ser.close()
    
    log_file.close()

    exit(0)

signal.signal(signal.SIGINT, signal_handler)
print("Strg+C drücken, um das Skript zu beenden.\n")

try:
    ser= serial.Serial(port="/dev/cu.usbmodem144101",
                          baudrate=9600, 
                          bytesize=8,
                          parity="N",
                          stopbits=1 
                         )
       
except serial.SerialException as e:
         print(f"Fehlermeldung: {e} ")  

log_dir= 'log'
os.makedirs(log_dir, exist_ok=True)

file_name= f"log_{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.csv"
file_path= os.path.join(log_dir, file_name)

log_file=open(file_path, 'w')
log_file.write("Zeit,Winkel Kamera,Winkel nach Comp.-filter\n")
    
start_time= time.time()

    
while 1:
     try: 

      data= ser.readline().decode('utf-8') # oder decode('ascii')
      
      if data:
            timestamp= time.time()-start_time
            log_file.write(f"{timestamp:.2f},{data}\n")
            print(f"{timestamp:.2f},{data}")
      
     except serial.SerialException as e :
            print(f"Fehler beim Lesen von der seriellen Schnittstelle: {e}")
            

    
    



