import pandas as pd 
dataframe = pd.read_csv('Salaries.csv')
#print(dataframe) -> to check if the read was successful 
#print(dataframe.head(1))
print(dataframe.info())
#now find the average basepay 
print(dataframe.columns)
basepay = dataframe['BasePay']
print(f'The Mean is {basepay.mean()}')
#find the highest amount of overtime pay 
overtime = dataframe['OvertimePay'].max()
print(f'the highest overtime is {overtime}')
## all information about an employee
details_emp = [dataframe[dataframe['EmployeeName'] == 'CATHRINE SNEED']]
print(details_emp)
#how much dose she make 
details_sal = dataframe[dataframe['EmployeeName'] == 'CATHRINE SNEED']['TotalPay']
print(f'her totle pay is {details_sal}')
#what is the name of the highest paid person 
highest_paid = dataframe['TotalPayBenefits'].max()
print(dataframe[dataframe['TotalPayBenefits'] == highest_paid]['EmployeeName'])
# or what we can do is 
print(dataframe.loc[dataframe['TotalPayBenefits'].idxmax()])
# now find the lowest paid person in the company 
lowest = dataframe.loc[dataframe['TotalPayBenefits'].idxmin()]
print(f'the lowest payed person is {lowest}')
# avg basepay for all the employess per year 
print(dataframe.groupby('Year').mean()['BasePay'])
# how many unique job titles are there in the company 
print(dataframe['JobTitle'].nunique())
#what are teh top 5 most common jobs 
commonjobs = dataframe['JobTitle'].value_counts().head(5)
print(commonjobs)
# JOB title with only one occurance in 2013
unique_jobtitle = dataframe[dataframe['Year'] == 2013]['JobTitle'].value_counts() == 1
print(sum(unique_jobtitle))
# How many people have the word chief in their job title 
def find_chief(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

chiefs_count = dataframe['JobTitle'].apply(lambda x : find_chief(x))
print(sum(chiefs_count))




