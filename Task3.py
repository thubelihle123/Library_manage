"""You are provided with insurance dataset on blackboard. Please logon on blackboard and download the 
dataset. Write a python code to:
§ Read the dataset.
§ Inspects its column by displaying the first 10 records.
§ Display records for make and usage for sets_num that are more than 40.
§ Plot a basic graph showing effective_yr on y axes and carrying capacity on x-axes"""

import pandas as pd
data = pd.read_csv("c:/Users/Thubelihle Dube/Downloads/motor_insure.csv (2)/motor_data11-14lats.csv")

print(data.head(10))


#Plot a basic graph showing effective_yr on y axes and carrying capacity on x-axes"""

import matplotlib.pyplot as plt

plt.plot(data['EFFECTIVE_YR'], data['CARRYING_CAPACITY'])
plt.ylabel('EFFECTIVE YAER')
plt.xlabel('CARRYING CAPACITY')
plt.title('EFFECTIVE VS CARRING CAPACITY')
plt.show()