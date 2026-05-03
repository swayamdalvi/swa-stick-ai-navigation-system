import serial
import pynmea2

ser = serial.Serial('/dev/serial0', 9600, timeout=1)

while True:
    line = ser.readline().decode('utf-8', errors='ignore')

    if line.startswith('$GPGGA'):
        msg = pynmea2.parse(line)

        print("Latitude:", msg.latitude)
        print("Longitude:", msg.longitude)
