import pandas as pd

#read the file
df = pd.read_excel('sampleTable.xlsx')

#make a new panda dataframe
df2 = df.stack().mean()
df3 = df.stack().std()

#print it for the user
print("original:", df)
print("average:", df2)
print("deviation:", df3)
print("deviation times 3:", df3*3)
print("cv:", (df3/df2)*100)

