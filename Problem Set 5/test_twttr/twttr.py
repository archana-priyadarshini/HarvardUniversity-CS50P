# Problem statement: https://cs50.harvard.edu/python/2022/psets/2/twttr/
def main():
    res=shorten(input("Input: "))
    print("Output:",input)

def shorten(word):
    for i in word:
        if i.lower() in ('a','e','i','o','u'):
            word=word.replace(i,"")
    return word


if __name__ == "__main__":
    main()