import pandas as pd 
dataframe = pd.read_csv('Salaries.csv')
#print(dataframe) -> to check if the read was successful 
#print(dataframe.head(1))
print(dataframe.info())
#now find the average basepay 
print(dataframe.columns)
basepay = dataframe['BasePay'].mean()
print(basepay)