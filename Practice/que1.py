#1. Perform the following operations using Python on a data set :
#  read data from different formats(like csv, xls)
# 2. indexing and selecting data, sort data, describe attributes of data, 
# checking data types of each column. (Use Titanic Dataset).

#1. read data from different formats(like csv, xls)

print("Loading Dataset ")
import pandas as pd
df=pd.read_csv("Datasets/Titanic.csv")
data=df.head()
print(data)
print(df.sample())

#2. indexing and selecting data, sort data, describe attributes of data
# checking data types of each column.
print(" Indexing and selecting data ")
df.set_index("PassengerId", inplace=True)
df.head()

#selecting specific column
print("Selecting specific column ")
print(df["Name"].head())
#selecting multiple columns
print(df[["Name","Age","Sex"]].head())

#selecting rows and columns
#loc is use for the label base indexing to select rows and columns 
#The .loc method is used to access rows and columns in a DataFrame by their label or index.
#[[0, 1, 2]]:Specifies the rows to be accessed using their index labels (in this case, row indices 0, 1, and 2).
#["Name", "Age", "Sex"]: Specifies the columns to be accessed by their names. 
# It selects only these three columns from the DataFrame.
#Use .iloc for integer-based indexing, which ignores the index labels:
#print(df.iloc[[0, 1, 2]][["Name", "Age", "Sex"]])

print("Selecting rows and columns ")
print(df.iloc[[0, 1, 2]][["Name", "Age", "Sex"]])

#3 . sort data
#sort_values() function is used to sort the data in ascending or descending order.
#By default, it sorts in ascending order. If you want to sort in descending order, you
#can pass the ascending parameter as False
print("Sorting data ")


print(df.sort_values(by="Age",ascending=False).head())
#4. describe attributes of data
#describe() function is used to get a quick statistical summary of the data.
print("Describe attributes of data ")
print(df.describe(include= 'all'))    
#5. checking data types of each column
print("Checking data types of each column ")
print(df.dtypes)
