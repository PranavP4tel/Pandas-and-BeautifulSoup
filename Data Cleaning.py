#Data cleaning
import pandas as pd

df = pd.read_excel(r".\Pandas_Files\Customer Call List.xlsx")
df = df.drop_duplicates() # Removing duplicates

#Removing unused column
df = df.drop(columns = 'Not_Useful_Column')

#Removing extra characters in column data
df['Last_Name'] = df['Last_Name'].str.strip('...')
df['Last_Name'] = df['Last_Name'].str.strip('_')
df['Last_Name'] = df['Last_Name'].str.strip('/')

#Formatting phone number
df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]','',regex=True)
df['Phone_Number'] = df['Phone_Number'].apply(lambda x:str(x)).apply(lambda x:x[:3]+'-'+x[3:6]+'-'+x[6:10])
df['Phone_Number'] = df['Phone_Number'].str.replace('nan--','')
df['Phone_Number'] = df['Phone_Number'].str.replace('Na--','')

#Formatting/Seperating Address into appropriate columns
df[['Street_Address','State','ZIP Code']] = df['Address'].str.split(",",n=2,expand=True)

#Standardize Paying Customer column values
df['Paying Customer'] = df['Paying Customer'].str.replace('Yes','Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No','N')

#Standardize Do_Not_Contact column values
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No','N')

df = df.fillna('')

#Removing any data where phone number is missing or Do Not Contact value is Yes
for i in df.index:
    if df.loc[i,'Do_Not_Contact'] == 'Y':
        df.drop(i,inplace=True)

for i in df.index:
    if df.loc[i,'Phone_Number'] == '':
        df.drop(i, inplace=True)

df.reset_index(drop=True)
print(df)