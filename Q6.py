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

# which type of restaurant received moere offline orders, so that Zomato can provide customers with some good offers.
pivot_table=read_data.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivot_table,annot=True,fmt='d')
plt.title("heatmap")
plt.xlabel("online Order")
plt.ylabel("Listed_in(type)")
plt.show()