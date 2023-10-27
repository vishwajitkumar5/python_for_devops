import os

f = open("raj.txt","w")
f.write("nnandna")
f.close()

f= open("raj.txt","r")
print(f.read())