# Problem statement: https://cs50.harvard.edu/python/2022/psets/0/faces/
def main():
    print(convert(input()))

def convert(message):
    message=message.replace(":)","🙂")
    message=message.replace(":(","🙁")
    return message
main()