import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import zomato dataset
read_data=pd.read_csv("C:\\Users\\KKAMIT\\Desktop\\ZOMATO\\data .csv")
# print(read_data)

# remove the five from rate column 
def rating(value):
    value=str(value).split('/')
    value=value[0]
    return float(value)
read_data['rate']=read_data['rate'].apply(rating)
print(read_data['rate'])
# 1 what type of restaurant do the majority of customers order from

sns.countplot(x=read_data['listed_in(type)'])
plt.xlabel("resturant")
plt.show()