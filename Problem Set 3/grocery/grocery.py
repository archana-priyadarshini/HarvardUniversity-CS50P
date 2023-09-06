# Problem statement: https://cs50.harvard.edu/python/2022/psets/3/grocery/
grocery_list={}
while True:
    try:
        item=input().upper()
        if item in grocery_list:
            grocery_list[item]=grocery_list[item]+1
        else:
            grocery_list[item]=1
    except EOFError:
        break
sorted=dict(sorted(grocery_list.items()))
for key,value in sorted.items():
    print(f"{value} {key}")