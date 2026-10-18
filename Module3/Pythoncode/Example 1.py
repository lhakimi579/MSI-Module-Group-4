import serial

# -- Replace 'COMx' with your Arduino's serial port
ser = serial.Serial('COM9', 9600)

try:
    while True:
        pot_value = ser.readline().decode().strip()
        print("Potentiometer Value:", pot_value)

except KeyboardInterrupt:
    ser.close()
