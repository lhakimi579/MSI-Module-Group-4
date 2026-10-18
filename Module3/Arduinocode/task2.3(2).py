import serial
import matplotlib.pyplot as plt

# Connect to serial port COM9
ser = serial.Serial('COM9', 9600)
plt.ion()  # Interactive mode for real-time plot
fig, ax = plt.subplots()
x_vals, y_vals = [], []

# Flag for keyboard override
led_manual_off = False

def on_key(event):
    global led_manual_off
    if event.key == 's' or event.key == ' ':  # Press 's' or Spacebar to force LED OFF
        led_manual_off = True
        ser.write(b'L')
        print("\n[KEYBOARD] LED manually stopped (OFF).")
    elif event.key == 'r':  # Press 'r' to resume automatic potentiometer control
        led_manual_off = False
        print("\n[KEYBOARD] Resumed automatic LED control.")

# Connect the key press event to the matplotlib window
fig.canvas.mpl_connect('key_press_event', on_key)

try:
    print("Running... Click on the Matplotlib plot window and press 's' to stop the LED, or 'r' to resume.")
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
            ax.set_xlim(0, max(50, len(x_vals)))
            plt.pause(0.1)  # Updates plot and processes GUI/keyboard events

            # LED Control Logic
            if led_manual_off:
                ser.write(b'L')  # Force LED OFF regardless of potentiometer
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