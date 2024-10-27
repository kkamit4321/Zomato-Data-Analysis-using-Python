import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
read_data = pd.read_csv("C:\\Users\\KKAMIT\\Desktop\\ZOMATO\\data .csv")

def rating(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

read_data['rate'] = read_data['rate'].apply(rating)
# print(read_data['rate'])

# how many votes has each types of restaurant received from customers

g_data = read_data.groupby('listed_in(type)')['votes'].sum().reset_index()

plt.plot(g_data['listed_in(type)'], g_data['votes'], c='red', marker='o')
plt.xlabel("Types of Restaurant")
plt.ylabel("Votes")      
plt.show()
