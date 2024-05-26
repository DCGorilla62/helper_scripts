import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the csv file
data = pd.read_csv("Book1.csv", header=None)

print(data)

#Extract variable names
variable_names = data.iloc[:,0].values#Variable names are in the first coumn

# Data
DAC = pd.to_numeric(data.iloc[0,1:].values)
# DCT0 = data.iloc[1,1:].values
# DCT1 = data.iloc[2,1:].values

print("DAC")
print(DAC)

#Create a list to store fit parameters
fit_parameters = []

# Making a plot
plt.figure(figsize=(10,6))

with open('fit_parameters_DAC_to_ADC_Part2.txt', 'w') as f:
    
    for i in range(1,19):
        # print(i)
        print(variable_names[i])
        ADC = pd.to_numeric(data.iloc[i,1:].values)
        # print(ADC)
        plt.scatter(DAC, ADC,
                    #label=f'{variable_names[i]}',
                    marker='o',
                    s=5,
                    alpha=0.5)
        #plt.plot(DAC, ADC)
        
        #Plot a line to the data points
        params = np.polyfit(DAC, ADC, 1)
        slope = params[0]
        intercept = params[1]
        fit = slope*DAC + intercept
        plt.plot(DAC, fit,
                 linestyle='--',
                 linewidth=0.5,
                 label=f'{variable_names[i]}')

        # Print parameters of the fit
        print(f'Fit parameters for {variable_names[i]}:')
        print(f'Slope: {slope}')
        print(f'Intercept: {intercept}')
        print()

        # Write the parameters to a file
        f.write(f'Fit parameters for {variable_names[i]}:')
        f.write(f'Slope: {slope}')
        f.write(f'Intercept: {intercept}')
        f.write("\n")

        # Save teh paramters to the list
        fit_parameters.append([variable_names[i],
                               slope,
                               intercept])

print("Fit parameters saved")
    
# Plot shit
plt.xlabel("DAC")
plt.ylabel("ADC")
plt.title("HSK DAC vs SSOut ADC")
plt.grid(True)
plt.legend()
plt.xlim(0, None)
#plt.ylim(0, None)

plt.savefig("DAC_to_ADC.png", dpi=600)
plt.show()

    
    

# for i in variable_names:
#     print(i)
#     print(DAC[i])
    
#     plt.plot(DAC
# print(variable_names)

# Plot Data
# plt.figure(figsize=(10,6))




# #Iterate over each row
# for i in range(2, 19):
#     # Extract data from the rows
#     DAC = df.iloc[:, 0] #

plt.savefig("DAC_to_ADC_part2.png", dpi=600)
plt.show()
