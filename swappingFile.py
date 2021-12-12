def swapFileData():
    fileName=input("Enter the file name:")
    fileName2=input("Enter the file2 name:")
    

    file=open(fileName,"r")
    file2=open(fileName2,"w")
    for line in file:
        file2.write(line)
swapFileData()