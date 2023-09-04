# Problem statement: https://cs50.harvard.edu/python/2022/psets/1/meal/
def main():
    hrs=convert(input("What time is it? "))
    if 7.0<=hrs<=8.0:
        print("breakfast time")
    elif 12.0<=hrs<=13.0:
        print("lunch time")
    elif 18.0<=hrs<=19.0:
        print("dinner time")


def convert(time):
    h,m=[int(x) for x in time.split(":")]
    return h+m/60


if __name__ == "__main__":
    main()