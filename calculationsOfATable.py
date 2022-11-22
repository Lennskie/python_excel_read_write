import math
import pandas as pd

#read the file
df = pd.read_excel('sample.xlsx')

#make a new panda dataframe
df2 = df.stack().mean()

#print it for the user
print(df)
print("average",df2)
