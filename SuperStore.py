import pandas as pd

#Importing and Reading CSV file.
df = pd.read_csv('train.csv')

#Checking the first 5 rows to make sure it was imported correctly.
print(df.head())

#Helps us understand the dataset. Gives us column names, Non-Null Count, and Data types.
print(df.info())

#Tells us how many null values are in the dataset and which column they are in.
print(df.isnull().sum())

#The values that are null are postal codes. Since we have other information about the customers location
#such as State and City, and the fact that there are only 11 missing values, we can manually fill in the missing values for the highest accuracy.


#We have learned that all of the postal codes that are missing are from the same city and state.
missing_postal = df[df['Postal Code'].isna()]
print(missing_postal[['Customer ID', 'City', 'State', 'Postal Code', 'Region']])

#The East Burlington are of Burlington, Vermont is primarily served by two different postal codes: 05401 and 05405.
#Since we cannot determine which postal code the customer falls under for sure without guessing, I will instead remove the data to maintain integrity.

df = df[df['Postal Code'].notna()]

#We have successfully removed any data entries with NA values in them. 
print(df.isnull().sum())

print(df.dtypes)

#Changing the date to datetime 
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)
#Changing the datatype of Postal Code
df['Postal Code'] = df['Postal Code'].astype(int).astype(str)
#Feature engineering Order Month, Order Year, and Order Quarter
df['Order Month'] = df['Order Date'].dt.month
df['Order Year'] = df['Order Date'].dt.year
df['Order Quarter'] = df['Order Date'].dt.to_period('Q')


print(df.dtypes)

#Exporting to CSV for dashboarding
df.to_csv('cleaned_superstore_data.csv', index=False)