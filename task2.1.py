import serial

# Updated to use COM9 as requested
ser = serial.Serial('COM9', 9600)

try:
    while True:
        line = ser.readline().decode().strip()
        if line.isdigit():
            pot_value = int(line)
            print("Potentiometer Value:", pot_value)


except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")

finally:
     ser.close() # Close the serial connection
     print("Serial connection closed.")