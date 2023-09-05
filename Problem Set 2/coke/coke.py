# Problem statement: https://cs50.harvard.edu/python/2022/psets/2/coke/
due=50
while due>0:
    print(f"Amount Due: {due}")
    add=int(input("Insert Coin: "))
    if add == 25 or add ==10 or add==5:
        due-=add
print(f"Change Owed: {due*-1}")