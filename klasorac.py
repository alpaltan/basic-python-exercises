import os

for i in range(1, 137, 1):
    a = 13 + i
    b = "Exercise_" + str(a)
    os.mkdir(str(b))
    mycwd = os.getcwd()
    os.chdir(mycwd + "/" + str(b))
    dosya = open("quest.txt", "x")
    dosya.close()
    dosya = open("solution.py", "x")
    dosya.close()
    os.chdir(mycwd)
