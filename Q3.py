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

# what are the rating that the majority of restauranthave customer

plt.hist(read_data['rate'],bins=10)
plt.title("rating distribution")
plt.show()