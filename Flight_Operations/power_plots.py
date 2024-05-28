import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the csv files
west = pd.read_csv("830_1300_UTC/west_power.csv")
north = pd.read_csv("830_1300_UTC/north_power.csv")
east = pd.read_csv("830_1300_UTC/east_power.csv")
south = pd.read_csv("830_1300_UTC/south_power.csv")


# setting figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data
west.plot(x='Date', y='Tot Power', ax = ax, label='west')
north.plot(x='Date', y='Tot Power', ax = ax, label='north')
east.plot(x='Date', y='Tot Power', ax = ax, label='east')
south.plot(x='Date', y='Tot Power', ax = ax, label='south')

# Customize the plot
ax.set_title('8:30 to 13:00 UTC')
ax.set_xlabel('Date')
ax.set_ylabel('Power')
ax.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("830_1300_UTC_Power.png", dpi=600)
plt.show()
