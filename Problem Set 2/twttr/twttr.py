# Problem statement: https://cs50.harvard.edu/python/2022/psets/2/twttr/
inp=input("Input: ")
for i in inp:
    if i.lower() in ('a','e','i','o','u'):
        inp=inp.replace(i,"")
print("Output:",inp)