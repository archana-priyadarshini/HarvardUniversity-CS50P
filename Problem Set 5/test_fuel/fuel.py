# Problem statement: https://cs50.harvard.edu/python/2022/psets/3/fuel/
def main():
    num=input("Fraction: ")
    res=convert(num)
    print(gauge(res))

def convert(fraction):
    x,y=[int(num) for num in fraction.split("/")]
    if y==0:
        raise ZeroDivisionError
    elif x>y:
        raise ValueError
    else:
        return int(round(x/y*100))


def gauge(percentage):
    try:
        if 99<=percentage<=100:
            return "F"
        elif 0<=percentage<=1:
            return "E"
        elif 1 < percentage < 99:
            return f"{percentage}%"
        else:
            raise TypeError
    except TypeError:
        pass


if __name__ == "__main__":
    main()