import serial
import time
import matplotlib.pyplot as plt
import csv
from collections import deque
import os

# Connect to Arduino (Change 'COM3' to match your port)
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Allow time for connection

# Initialize Plot
plt.ion()
fig, ax = plt.subplots()
data = deque(maxlen=100)  # Stores last 100 values for live graphing

# Open CSV file to store data
with open("data/vibration_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Vibration Value"])  # CSV headers

    while True:
        try:
            line = ser.readline().decode().strip()  # Read and decode serial data
            if line.isdigit():  # Ensure it's a valid number
                value = int(line)
                timestamp = time.time()  # Get current time

                # Store value in deque for real-time plotting
                data.append(value)

                # Write data to CSV
                writer.writerow([timestamp, value])
                file.flush()  # Ensures data is written immediately

                # Update live graph
                ax.clear()
                ax.plot(data)
                ax.set_title("Real-Time Vibration Sensor Data")
                ax.set_xlabel("Time")
                ax.set_ylabel("Vibration Intensity")
                plt.draw()
                plt.pause(0.1)  # Small delay for real-time effect

        except KeyboardInterrupt:
            print("\nStopping data collection and closing file...")
            break

ser.close()
