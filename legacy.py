import math

#define how to calculate the average
def average(lst):
    return sum(lst) / len(lst)

#start the program with asking for numbers, with the delimiter being a space
userInput = input("Give me all your numbers, splitted by a space: \n")
#have the userInput as a list
numbers_list = [float(num) for num in userInput.split()]

#you need a counter to you know... count...
counter = 0

#do some cool calculations here
for i in numbers_list:
    above = (i-average(numbers_list))**2
    counter += above

#some other cool calculations
total = math.sqrt((counter/(len(numbers_list)-1)))

#print time like a boss!
print(numbers_list)
print("average: ", average(numbers_list))
print("standard deviation", total)