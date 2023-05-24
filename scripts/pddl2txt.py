import subprocess
import os
import argparse
from PIL import Image, ImageDraw, ImageFont



def create_problem(lista,goal):
    #os.chdir("scripts/")
    
    #create the same element as in the pddl problem

        
    #take the goal
    """
    with open("../utils/goal.txt") as go:
        goal = go.readline()
        go.close()
    """
    
    #modify the pddl problem    
    if (lista!=''):
        lista = lista.split(",")
        for i in range(len(lista)):
            lista[i] = lista[i]+"\n"
        
        with open('../problems/grid_problem.pddl','r') as f:
            lines = f.readlines()
            for elem in lista:
                if elem in lines:
                    lines.remove(elem)
                    
        f.close()
        iter = 0
        flag_it = False
        while(not flag_it):
            if "goal" in lines[iter]:
                lines[iter] = "    (:goal (and(at "+goal+")))\n"
                flag_it=True
            iter+=1
            
        #write the new_problem
        with open("../problems/grid_problem_tmp.pddl","w") as car:
            for elem in lines:
                car.write(elem)
        car.close()
        return run()
    else:
        return goal+".jpg"
    
def print_path(solution,path):

    step_count = 30
    height = 30
    width = 30

    image = Image.open("../img/mappa_new.jpg")

    # Draw lines
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / step_count)
    lines = []
    with open(solution) as f:
        line= f.readline()
        previous_line_horiz_r = False
        horiz_line1=0.5
        horiz_line2=0.5
        while(line):
            
            line = line.split("pos")
            line1 = line[1]
            line1 = line1.replace("_",",").split(",")
            line2 = line[2]
            line2 = line2.strip("\n")
            line2 = line2.replace("_",",").strip(")").split(",")
            
            if(line1[0]==line2[0] and int(line1[1])>int(line2[1])):
                
                if(previous_line_horiz_r):
                    horiz_line1=1
                    horiz_line2=1
                else:
                    horiz_line1=0.5
                    horiz_line2=1
                    previous_line_horiz_r=True
            else:
                if(previous_line_horiz_r):
                    horiz_line1=1
                else:
                    horiz_line1=0.5
                horiz_line2=0.5
                previous_line_horiz_r=False
            line1= ((float(line1[1])-horiz_line1)*step_size,(float(line1[0])-horiz_line1)*step_size)
            line2 = ((float(line2[1])-horiz_line2)*step_size,(float(line2[0])-horiz_line2)*step_size)
            lines.append((line1,line2))
            
            #cofang = (line2[1]-line1[1])/(line2[0]-line1[0])
            
            line = f.readline()
    #it = 1
    for elem in lines:
        draw.line(elem,fill=200)
    del draw
    
    image.save("../img/tmp.jpg")
    os.chdir(path)
    return "tmp.jpg"


def run(): 
    path = os.getcwd()
    os.chdir("../problems/")
    
    out = os.popen("'./optic-clp' 'grid_domain.pddl' 'grid_problem_tmp.pddl'").read()
    new_out = out.split(";;;; Solution Found")
    new_out = new_out[1]
    f = open("../utils/sol.txt","w")
    f.write(new_out)
    f.close()
    
    with open("../utils/sol.txt","r") as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        kar = open("../utils/sol1.txt","w")
        while(line):
            kar.write(line[:-10]+"\n")
            line=f.readline()
        kar.close()
    f.close()
    
    return print_path("../utils/sol1.txt",path)
