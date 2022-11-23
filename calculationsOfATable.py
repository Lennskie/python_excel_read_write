import pandas as pd

#read the file
df = pd.read_excel('sampleTable.xlsx')

#make a new panda dataframe
df2 = df.stack().mean()

#print it for the user
print(df)
print("average",df2)

#count the rows and columns of the table
rows = len(df.axes[0])
columns = len(df.axes[1])

#get how many NaN are in the table
NaN = df.isnull().sum().sum()

#get the real data
real_data = (rows*columns)-NaN