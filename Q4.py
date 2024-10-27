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
# Zomato has observed that most couples order. most of their food online what is the average spending on each order
c_data=read_data['approx_cost(for two people)']  
sns.countplot(x=c_data)  
plt.show()
