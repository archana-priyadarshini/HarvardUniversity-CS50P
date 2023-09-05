# Problem statement: https://cs50.harvard.edu/python/2022/psets/2/twttr/
input=input("Input: ")
for i in input:
    if i.lower() in ('a','e','i','o','u'):
        input=input.replace(i,"") 
print("Output:",input)