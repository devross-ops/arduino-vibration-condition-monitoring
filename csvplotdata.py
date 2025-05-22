import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
df = pd.read_csv("vibration_data.csv")

# Plot saved data
plt.plot(df["Timestamp"], df["Vibration Value"])
plt.title("Saved Vibration Sensor Data")
plt.xlabel("Time")
plt.ylabel("Vibration Intensity")
plt.show()
