# python excel read/write example

This program was custom made for calculating things quickly for a paper.

## installation
>pip install openpxyl
>
>pip install pandas

## explanation about the files
>calculations.py calculates row by row, and cannot have empty cells. This program used sample.xlsx
>
>legacy.py is a terminal application, having almost no automation. You manually add the numbers you want, delimited by a space
>
>calculationsOfATable.py uses the sampleTable.xlsx file to merge rows & collums to make the calculations on a whole batch (This excel file can have empty cells).

Both calculations.py & lecagy.py are not that usefull anymore and can be slow. Some of the code I only got working for Python3.10. This means that you're best of useinng calculationsOfATable.py, but all was used for research purposes.

## run
make sure your calculations.py file & your sample.xlsx file are in the same place when you run the python file

## Common errors
This doesn't appear to work for python3.9, and only works/tested for **python3.10**. Make sure your interpreter is 3.10.
When tested for **3.7**, you might have to *remove the .pop() on line 26 & 42* functions out of "list_maker_deviation" & "list_maker_average" in the calculations.py file because of a weird issue in panda.
