# Problem statement: https://cs50.harvard.edu/python/2022/psets/1/deep/
question=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if question.lower().strip() in("42","forty-two","forty two"):
    print("Yes")
else:
    print("No")