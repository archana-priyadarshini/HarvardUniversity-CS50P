# Problem statement: https://cs50.harvard.edu/python/2022/psets/1/interpreter/
x,y,z=input("Expression: ").split(" ")
x=int(x)
z=int(z)    
if y=="+":
    print(f"{x+z:.1f}")
elif y=="-":
    print(f"{x-z:.1f}")
elif y=="*":
    print(f"{x*z:.1f}")
else:
    print(f"{x/z:.1f}")