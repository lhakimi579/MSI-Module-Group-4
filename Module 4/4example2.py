from collections import deque
import time
import serial
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
SERIAL_PORT = "COM9"  # Update to match your Arduino's COM port
BAUD_RATE = 9600
MAX_POINTS = 100  # Rolling window for real-time motion path plotting
AUTHORIZED_CARDS = [
    "0013082958",

]  # Replace with your actual card UIDs


def detect_circular_motion(ser):
  """Captures live MPU6050 data and checks for circular motion patterns."""
  print("\n>>> Perform circular motion now (Monitoring sensor for 4 seconds)...")

  x_vals = deque(maxlen=MAX_POINTS)
  y_vals = deque(maxlen=MAX_POINTS)

  # Setup live plot window for motion verification
  plt.ion()
  fig, ax = plt.subplots(figsize=(5, 5))
  (line,) = ax.plot([], [], "ro-", alpha=0.7, label="Motion Path")
  ax.set_xlim(-18000, 18000)
  ax.set_ylim(-18000, 18000)
  ax.set_title("Verifying Circular Gesture...")
  ax.grid(True)

  start_time = time.time()
  motion_detected = False

  # Collect data for 4 seconds to analyze gesture
  while time.time() - start_time < 4.0:
    if ser.in_waiting > 0:
      line_data = ser.readline().decode("utf-8", errors="ignore").strip()
      if line_data:
        values = line_data.split(",")
        if len(values) >= 2:
          try:
            ax_val = int(values[0])
            ay_val = int(values[1])

            x_vals.append(ax_val)
            y_vals.append(ay_val)

            line.set_xdata(x_vals)
            line.set_ydata(y_vals)
            plt.draw()
            plt.pause(0.001)
          except ValueError:
            continue

  plt.close(fig)
  plt.ioff()

  # Simple gesture validation logic (e.g., checking if motion has spread across multiple quadrants)
  if len(x_vals) > 20:
    # A basic heuristic: if X and Y values fluctuate significantly, consider it a valid gesture
    x_range = max(x_vals) - min(x_vals)
    y_range = max(y_vals) - min(y_vals)
    if x_range > 3000 and y_range > 3000:
      motion_detected = True

  return motion_detected


def main():
  try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Allow serial connection to initialize
    print("System Ready. Waiting for RFID scan...")

    while True:
      print("\n--------------------------------------------------")
      # USB RFID desktop reader behaves like a keyboard and types out the UID
      uid = input("Tap your RFID card on the USB Reader: ").strip().upper()

      if not uid:
        continue

      print(f"Scanned UID: {uid}")

      if uid in AUTHORIZED_CARDS:
        print("RFID Authorized! Please perform the motion gesture.")

        # Trigger motion verification using MPU6050
        if detect_circular_motion(ser):
          print("Motion verified successfully! Access Granted.")
          ser.write(b"A")  # Sends 'A' command to Arduino (Servo unlock + Green LED)
        else:
          print("Motion invalid or not detected. Access Denied.")
          ser.write(b"D")  # Sends 'D' command to Arduino (Red LED)
      else:
        print("Unauthorized RFID tag. Access Denied.")
        ser.write(b"D")  # Sends 'D' command to Arduino (Red LED)

      time.sleep(0.5)

  except KeyboardInterrupt:
    print("\nProgram terminated by user.")
  finally:
    if "ser" in locals() and ser.is_open:
      ser.close()


if __name__ == "__main__":
  main()