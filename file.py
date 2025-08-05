f=open("file.txt")
data=f.read()
print(data)
f.close()

#write in the file

st="Aman is the Gentleman having some personal issues hehehehehehehe"

f=open("myfile.txt","w")

f.write(st)

f.close()                                                  
