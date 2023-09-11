# Problem statement: https://cs50.harvard.edu/python/2022/psets/4/adieu/
import inflect
p = inflect.engine()
names=[]
while True:
    try:
        name=input("Name: ")
        names.append(name)
    except EOFError:
        break
print("\nAdieu, adieu, to",p.join(names))