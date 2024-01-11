import pandas as pd

path="E:\\Web Dev\\Practice\\Data Analysis\\train.csv"
data=pd.read_csv(path)

# print(data.head())
# print(data.shape)
# print(data.columns)

# print(data.info())
# print(data.describe(include='all'))

# data filtering 
# print(data[['Pclass','Ticket','Sex']]) # mutiple columns getting
# print(sum(data['Sex']=='male'))

# find age of male who travel 
# print(data[data['Sex']=='male']['Age'])

# find average age of male who travel 
# print("Average age of male who travel: ",data[data['Sex']=='male']['Age'].mean())

# find max age of male who travel 
# print("Max age of male: ",data[data['Sex']=='male']['Age'].max())

# find number of persons who survived 
# print(len(data[data['Survived']==1]))

# second way to find survived persons using 'sum' function
# print(sum(data['Survived']==1))


# find number of persons who died 
# print(len(data[data['Survived']==0]))

# print(data.isnull().sum())

import seaborn as sns
import matplotlib.pylab as plt

# Visualize which column is having null values   
# plt.figure(figsize=(10,4.5))
# plt.title("Null values")
# plt.xlabel("Age")
# plt.ylabel("Ticket")
# sns.histplot(data['Ticket'],bins=20,kde=True) 
# sns.histplot(data.isnull(),bins=20,kde=True) 
# sns.heatmap(data.isnull()) 
# plt.show()

# per_missing=data.isnull().sum()*100/len(data)
# print(per_missing)

# delete columns 
print(data.columns)
data.drop('Name',axis=1,inplace=True)
per_missing=data.isnull().sum()*100/len(data)
# print(per_missing) 
print(data.columns)
