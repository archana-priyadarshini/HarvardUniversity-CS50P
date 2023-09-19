# Problem statement: https://cs50.harvard.edu/python/2022/psets/6/pizza/
import sys,csv
from tabulate import tabulate


if len(sys.argv)<2:
    sys.exit("Too few command-line arguments ")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments ")
elif not(sys.argv[1].endswith(".csv")):
    sys.exit("Not a CSV file")
try:
    with open(sys.argv[1],"r") as file:
        reader=csv.reader(file)
        print(tabulate(reader,headers="firstrow",tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
