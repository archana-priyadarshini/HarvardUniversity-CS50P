#Problem Statement: https://cs50.harvard.edu/python/2022/psets/4/professor/
import random


def main():
    level=get_level()
    score=0
    for i in range(10):
        x= generate_integer(level)
        y= generate_integer(level)
        correct_ans=x+y
        chances=3
        while chances>0:
            try:
                ans= int(input(f" {x} + {y} = "))
                if correct_ans == ans:
                    score+=1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                chances-=1
                pass
        if i==0:
           print(f" {x} + {y} =",x+y)
    print("Score:",score)


def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if 1<=level<=3:
                return level
        except:
            pass


def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    elif level==3:
        return random.randint(100,999)


if __name__ == "__main__":
    main()