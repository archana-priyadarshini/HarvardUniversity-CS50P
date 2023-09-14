# Problem statement: https://cs50.harvard.edu/python/2022/psets/2/plates/
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #starts with at least two letters, max 6 & min 2 characters,No periods, spaces, or punctuation marks are allowed.
    if s[0:2].isalpha() and 2<=len(s)<=6 and s.isalnum():
        if s.isalpha():
            return True
        for i,ch in enumerate(s):
            if ch.isdigit():
                if s[i:].isdigit() and int(ch)!=0:
                    return True
                break
    return False

if __name__=="__main__":
    main()