import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, time


# Functions to filter out a time range
def filter_time_range(df, start_time, end_time):
    # Convert datetime column to datetime object with correct format
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')
    

    # Extract the time part only
    #df['time'] = df['Date'].dt.time

    # Filter the dataframe for the specified time range
    df_filtered = df[(df['Date'] >= start_time) & (df['Date'] <= end_time)]
    
    return df_filtered

def set_time_range(delta):

    # Get the current time
    end_time = pd.Timestamp.now()

    # Filter for time delta period you want
    start_time = end_time - timedelta(hours=delta)
    
    return start_time, end_time

# Setting the parent directory of the directory holding the csv files
data_dir = "0900_1500_UTC_05-29"

# Read the csv files
west = pd.read_csv(data_dir + "/west_power.csv")
north = pd.read_csv(data_dir + "/north_power.csv")
east = pd.read_csv(data_dir + "/east_power.csv")
south = pd.read_csv(data_dir + "/south_power.csv")


start_time, end_time = set_time_range(2)

# Define the time range
# start_time = time(13,30, 0)
# end_time = time(15, 0, 0)

west = filter_time_range(west, start_time, end_time)
north = filter_time_range(north, start_time, end_time)
east = filter_time_range(east, start_time, end_time)
south = filter_time_range(south, start_time, end_time)

# setting figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data
west.plot(x='Date', y='Tot Power', ax = ax, label='west')
north.plot(x='Date', y='Tot Power', ax = ax, label='north')
east.plot(x='Date', y='Tot Power', ax = ax, label='east')
south.plot(x='Date', y='Tot Power', ax = ax, label='south')

# Customize the plot
ax.set_title(data_dir)
ax.set_xlabel('Date')
ax.set_ylabel('Power')
ax.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("power_" + data_dir + ".png", dpi=600)
# plt.show()
