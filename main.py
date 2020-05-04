from tkinter import *

import PIL
from PIL import Image, ImageFont
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import *



file_path = askopenfilename()
img = PIL.Image.open(file_path)
myheight, mywidth = img.size
format = img.format
img = img.resize((myheight,mywidth),PIL.Image.ANTIALIAS)
save_path = asksaveasfilename()
img.save(save_path+ '_compressed.JPG')

