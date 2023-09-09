# Problem statement: https://cs50.harvard.edu/python/2022/psets/4/figlet/
import sys,random
from pyfiglet import Figlet
figlet = Figlet()
if not((len(sys.argv)==1) or (len(sys.argv)==3 and sys.argv[1] in ["-f","--font"] and sys.argv[2] in figlet.getFonts())):
    sys.exit("Invalid usage")
s=input("Input: ")
if (len(sys.argv)<=1):
    f=random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(s))
else:
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(s))