# Problem statement: https://cs50.harvard.edu/python/2022/psets/2/camel/
name=input("camelCase: ")
for a in name:
    if a.isupper():
        name=name.replace(a,f"_{a.lower()}")
print("snake_case:",name)