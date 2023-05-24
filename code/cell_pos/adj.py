jmatrix = 31
file1 = open("poses.txt", "a")
for i in range(1,jmatrix):
    for j in range(1,jmatrix):
        if(j+1<jmatrix):
            file1.write("(adj pos"+str(i)+"_"+str(j)+" pos"+str(i)+"_"+str(j+1)+")\n")
            file1.write("(= (step pos"+str(i)+"_"+str(j)+" pos"+str(i)+"_"+str(j+1)+") 1)\n")
        if(i+1<jmatrix):
            file1.write("(adj pos"+str(i)+"_"+str(j)+" pos"+str(i+1)+"_"+str(j)+")\n")
            file1.write("(= (step pos"+str(i)+"_"+str(j)+" pos"+str(i+1)+"_"+str(j)+") 1)\n")
        if(j-1>0):
            file1.write("(adj pos"+str(i)+"_"+str(j)+" pos"+str(i)+"_"+str(j-1)+")\n")
            file1.write("(= (step pos"+str(i)+"_"+str(j)+" pos"+str(i)+"_"+str(j-1)+") 1)\n")
        if(i-1>0):
            file1.write("(adj pos"+str(i)+"_"+str(j)+" pos"+str(i-1)+"_"+str(j)+")\n")
            file1.write("(= (step pos"+str(i)+"_"+str(j)+" pos"+str(i-1)+"_"+str(j)+") 1)\n")
        if(j+1<jmatrix and i+1<jmatrix):
            file1.write("(adj pos"+str(i)+"_"+str(j)+" pos"+str(i+1)+"_"+str(j+1)+")\n")
            file1.write("(= (step pos"+str(i)+"_"+str(j)+" pos"+str(i+1)+"_"+str(j+1)+") 1)\n")
        if(j+1<jmatrix and i-1>0):
            file1.write("(adj pos"+str(i)+"_"+str(j)+" pos"+str(i-1)+"_"+str(j+1)+")\n")
            file1.write("(= (step pos"+str(i)+"_"+str(j)+" pos"+str(i-1)+"_"+str(j+1)+") 1)\n")
        if(j-1>0 and i+1<jmatrix):
            file1.write("(adj pos"+str(i)+"_"+str(j)+" pos"+str(i+1)+"_"+str(j-1)+")\n")
            file1.write("(= (step pos"+str(i)+"_"+str(j)+" pos"+str(i+1)+"_"+str(j-1)+") 1)\n")
        if(j-1>0 and i-1>0):
            file1.write("(adj pos"+str(i)+"_"+str(j)+" pos"+str(i-1)+"_"+str(j-1)+")\n")
            file1.write("(= (step pos"+str(i)+"_"+str(j)+" pos"+str(i-1)+"_"+str(j-1)+") 1)\n")
file1.close()
