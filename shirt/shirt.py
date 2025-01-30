import sys
import csv
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if not (sys.argv[1].endswith((".png",".jpg",".jpeg")) and sys.argv[2].endswith((".png",".jpg",".jpeg"))):
        sys.exit("Invalid Output")
    else:
        x,y=sys.argv[1].split(".")
        a,b=sys.argv[2].split(".")
        if y != b:
            sys.exit("Input and output have different extensions")
        else:
            try:
                imagefile = Image.open(sys.argv[1])
            except FileNotFoundError:
                sys.exit("Input does not exit")
            shirtfile = Image.open("shirt.png")
            size = shirtfile.size
            muppet = ImageOps.fit(imagefile,size)
            muppet.paste(shirtfile, shirtfile)
            muppet.save(sys.argv[2])
