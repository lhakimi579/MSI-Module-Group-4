import serial
import matplotlib.pyplot as plt

# Connect to serial port COM9
ser = serial.Serial('COM9', 9600)
plt.ion()  # Interactive mode for real-time plot
fig, ax = plt.subplots()
x_vals, y_vals = [], []

# Flags for keyboard controls
led_manual_off = False
arduino_halted = False


def on_key(event):
    global led_manual_off, arduino_halted
    
    if event.key == 'r':  # Press 'r' to resume automatic control & execution
        led_manual_off = False
        arduino_halted = False
        ser.write(b'R')
        print("\n[KEYBOARD] Resumed automatic control and Arduino execution.")
    elif event.key == 'x':  # Press 'x' to halt Arduino execution
        arduino_halted = True
        ser.write(b'X')
        print("\n[KEYBOARD] Sent HALT command to Arduino.")


# Connect the key press event to the matplotlib window
fig.canvas.mpl_connect('key_press_event', on_key)

try:
    print("Running... Click on the Matplotlib plot window:")
    print(" - Press 's' or Space to turn LED OFF")
    print(" - Press 'x' to HALT Arduino execution")
    print(" - Press 'r' to RESUME Arduino execution")

    while True:
        line = ser.readline().decode().strip()
        if line.isdigit():
            pot_value = int(line)
            print("Potentiometer Value:", pot_value)
            x_vals.append(len(x_vals))
            y_vals.append(int(pot_value))

            ax.clear()
            ax.plot(x_vals, y_vals, marker='o', color='b')
            ax.set_ylim(0, 1023)
            ax.set_xlim(0, max(50, len(x_vals)))
            ax.set_title("Real-Time Potentiometer Readings")
            ax.set_xlabel("Sample")
            ax.set_ylabel("Value")
            plt.pause(0.1)  # Updates plot and processes GUI/keyboard events

            # LED Control Logic (only if not halted)
            if not arduino_halted:
                if led_manual_off:
                    ser.write(b'L')  # Force LED OFF
                else:
                    if pot_value > 511:
                        ser.write(b'H')  # Turn LED ON
                    else:
                        ser.write(b'L')  # Turn LED OFF

except KeyboardInterrupt:
    ser.close()
    plt.ioff()
    plt.show()
    print("Serial connection closed.")
