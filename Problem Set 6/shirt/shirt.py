#Problem Statement: https://cs50.harvard.edu/python/2022/psets/6/shirt/

import sys,os
from PIL import Image,ImageOps

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments ")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments ")

input=sys.argv[1]
output=sys.argv[2]
inp_ext,out_ext=os.path.splitext(input)[1],os.path.splitext(output)[1]

if inp_ext not in ('.jpeg','.jpg','.png') or out_ext not in ('.jpeg','.jpg','.png'):
    sys.exit("Invalid input")
if inp_ext!=out_ext:
    sys.exit("Input and output have different extensions")
try:
    input_image=Image.open(input)
    shirt = Image.open("shirt.png")
    cropped=ImageOps.fit(input_image, shirt.size)
    cropped.paste(shirt,shirt)
    cropped.save(output)
except FileNotFoundError:
    sys.exit("Input does not exist")
    
    

