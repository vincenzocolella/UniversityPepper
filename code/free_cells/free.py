walls = []

with open("wall.txt") as f:
    line = f.readline()
    while(line):
        line1 = line.strip("\n")
        walls.append(line1)
        line=f.readline()
f.close()
file1 = open("free.txt", "a")
for i in range(1,31):
    for j in range(1,31):
        str1= "pos"+str(i)+"_"+str(j)
        if(str1 not in walls):
            file1.write("(f "+str1+")\n")
file1.close()
