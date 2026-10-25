import matplotlib.pyplot as plt
import serial
import matplotlib

ser = serial.Serial('COM9', 9600, timeout=1)

x_vals = []
y_vals = []

plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(-20000, 20000)
ax.set_ylim(-20000, 20000)

line, = ax.plot([], [], 'ro')

while True:
    try:
        data = ser.readline().decode().strip()
        if data:
            values = data.split(',')
            ax_vals = int(values[0])
            ay_vals = int(values[1])
            x_vals.append(ax_vals)
            y_vals.append(ay_vals)
            line.set_data(x_vals, y_vals)
            plt.draw()
            plt.pause(0.05)
    except KeyboardInterrupt:
        break
