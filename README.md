# python excel read/write example

## installation
>pip install openpxyl
>
>pip install pandas

## run
make sure your calculations.py file & your sample.xlsx file are in the same place when you run the python file

## Common errors
This doesn't appear to work for python3.9, and only works/tested for **python3.10**. Make sure your interpreter is 3.10.
When tested for **3.7**, you might have to *remove the .pop() on line 26 & 42* functions out of "list_maker_deviation" & "list_maker_average" because of something in panda.