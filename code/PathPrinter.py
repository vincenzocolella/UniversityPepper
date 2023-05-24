import argparse

from PIL import Image, ImageDraw, ImageFont


step_count = 30
height = 30
width = 30

image = Image.open("../mappa_new.jpg")

# Draw some lines
draw = ImageDraw.Draw(image)
y_start = 0
y_end = image.height
step_size = int(image.width / step_count)
lines = []
with open("../plans/grid_problemnew.txt") as f:
    line= f.readline()
    while(line):
        
        line = line.split("pos")
        line1 = line[1]
        line1 = line1.replace("_",",").split(",")
        line1= ((float(line1[1])-0.5)*step_size,(float(line1[0])-0.5)*step_size)
        line2 = line[2]
        line2 = line2.strip("\n")
        line2 = line2.replace("_",",").strip(")").split(",")
        line2 = ((float(line2[1])-0.5)*step_size,(float(line2[0])-0.5)*step_size)
        lines.append((line1,line2))
        #cofang = (line2[1]-line1[1])/(line2[0]-line1[0])
        
        line = f.readline()
#it = 1
""" for elem in lines:
    if(it%2 ==0):
        draw.line(elem,fill=200)
    else:
        draw.line(elem,fill=0)
    it+=1 """
del draw

image.show()