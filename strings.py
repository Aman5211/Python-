name="Aman"
# string slicing is done, last index include nhi hota hei 
nameshort = name[0:4]
print(nameshort)

#negative slicing
name="harry"

print(name[-4:-1])
print(name[1:4])

#Slicing with skip values
name ="qwertyuiop"
print("The skiping character should be five - ",name[0:6:2])

# Escape sequence character
a ="Aman is hardworking men \n and \'become successful\'"
print(a)


#Practice set for the chapter 3
a=str(input("Write the name of the person - "))
print("GOOD AFTERNOON", a)

# PROBLEM2

letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "11 May 2026"))

#Problem 3 ( Find and occurance)
name = "Aman is a  good boy"
print(name.find("  "))
print(name.replace("  "," "))
# string are immutable and these find, replace values are stored as a new string not changing the current string of the function
print(name)