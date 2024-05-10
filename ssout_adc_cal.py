import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the csv file
data = pd.read_csv("SSOut_DAC_ADC.csv")

#Extract variable names
variable_names = df.iloc[0,0] #Variable names are in the first coumn

print(variable_names)

# Plot Data
plt.figure(figsize=(10,6))

# #Iterate over each row
# for i in range(2, 19):
#     # Extract data from the rows
#     DAC = df.iloc[:, 0] #

