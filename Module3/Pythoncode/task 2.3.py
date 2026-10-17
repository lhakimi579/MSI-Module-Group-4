import serial
import matplotlib.pyplot as plt

# Updated to use COM9 as requested
ser = serial.Serial('COM9', 9600)
plt.ion() # Interactive mode for real-time plot
fig, ax = plt.subplots()
x_vals, y_vals = [], []

try:
    while True:
        line = ser.readline().decode().strip()
        if line.isdigit():
            pot_value = int(line)
            print("Potentiometer Value:", pot_value)
            x_vals.append(len(x_vals))
            y_vals.append(int(pot_value))

            ax.clear()
            ax.plot(x_vals, y_vals, marker='o')
            ax.set_ylim(0, 1023)
            ax.set_xlim(0,max(50, len(x_vals)))# Plot potentiometer readings
            plt.pause(0.1)  # Update plot

            # Check if value exceeds half of its max range (1023 / 2 = ~511)
            if pot_value > 511:
                ser.write(b'H')  # Send 'H' to turn LED ON
            else:
              ser.write(b'L')  # Send 'L' to turn LED OFF

except KeyboardInterrupt:
    ser.close()
    plt.ioff() # Turn off interactive mode
    plt.show() # Final plot display
    print("Serial connection closed.")
