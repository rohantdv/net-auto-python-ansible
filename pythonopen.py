#READ

# readfile = open(r"C:\Users\Rohan\Documents\PythonDemoFile.txt", "r")
# xyz = readfile.read()
# print(xyz)

#WRITE

# readfile = open(r"C:\Users\Rohan\Documents\PythonDemoFile.txt", "w")
# xyz = readfile.write("THIS IS A TEST FILE")
# readfile.close()

#OR

# with open(r"C:\Users\Rohan\Documents\PythonDemoFile1.txt", "w") as backup333:
#     backup333.write("This is another test file")

#AMEMD

readfile = open(r"C:\Users\Rohan\Documents\PythonDemoFile.txt", "a")
xyz = readfile.write("\nThis is fifth test")
print(xyz)

#OR

with open(r"C:\Users\Rohan\Documents\PythonDemoFile1.txt", "a") as backup3434:
    backup3434.write("\nGlad, I learnt")