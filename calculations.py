import math
import pandas as pd

#read the file
path='sample.xlsx'
df = pd.read_excel('sample.xlsx')

#define how to calculate the average
def average(lst):
    return sum(lst) / len(lst)

#make the list readable for the program
def list_maker_average(lst):
    lst = lst.values.flatten().tolist()
    lst.pop(0) #this remove the name from the row out of the list
    return(lst)

#return the average of a row to df
def average_of_the_row(row):
    row = list_maker_average(row)
    return average(row)

#make another list_maker for deviation because the average adds a row to the df
def list_maker_deviation(lst):
    lst = lst.values.flatten().tolist()
    lst.pop(0)
    lst.pop(len(lst)-1) #remove the average out of the df
    return(lst)

#return the deviation of a row to df
def deviation_of_the_row(row):
    row = list_maker_deviation(row)
    counter = 0
    for i in row:
        above = (i-average(row))**2
        counter += above
    return(math.sqrt((counter/(len(row)-1))))

#list maker for the 3 times deviation
def list_maker_deviation_3(lst):
    lst = lst.values.flatten().tolist()
    lst.pop(0)
    lst.pop(len(lst)-1) #remove the average out of the df
    lst.pop(len(lst)-1) #remove the deviation out of the df
    return(lst)

#the deviation times 3, needs to be rewritten because of the bad optimisation. (might fix later)
def deviation_of_the_row_3(row):
    row = list_maker_deviation_3(row)
    counter = 0
    for i in row:
        above = (i-average(row))**2
        counter += above
    return((math.sqrt((counter/(len(row)-1))))*3)

#simple list maker because it just needs the average and deviation later
def list_maker_cv(lst):
    lst = lst.values.flatten().tolist()
    return(lst)

#calculate the deviation
def cv_of_the_row(row):
    row = list_maker_cv(row)
    deviation = row[len(row)-2]
    average = row[len(row)-3]
    return (deviation/average)*100

#cool calculations!
df['average'] = df.apply(lambda row : average_of_the_row(row), axis = 1)
df['deviation'] = df.apply(lambda row : deviation_of_the_row(row), axis = 1)
df['3 times deviation'] = df.apply(lambda row : deviation_of_the_row_3(row), axis = 1)
df['CV'] = df.apply(lambda row : cv_of_the_row(row), axis = 1)

#print it for the user
print(df)

#save it to the same file again, on another page
df.to_excel('output.xlsx')