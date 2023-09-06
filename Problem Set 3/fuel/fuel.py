# Problem statement: https://cs50.harvard.edu/python/2022/psets/3/fuel/

while True:
    try:
        x,y=[int(x) for x in input("Fraction: ").split("/")]
        percent=round(x/y*100)
        if percent>100 or percent<0:
            raise ValueError
        elif 99<=percent<=100:
            print("F")
        elif 0<=percent<=1:
            print("E")
        else:
            print(f"{round(x/y*100)}%")
        break
    except (ValueError, ZeroDivisionError):
        pass
