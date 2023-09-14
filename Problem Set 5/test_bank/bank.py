# Problem statement: https://cs50.harvard.edu/python/2022/psets/1/bank/
def main():
    res=value(input("Greeting: "))
    print(f"${res}")


def value(greeting):
    greeting=greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()