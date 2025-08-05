# a=int(input("Enter your age: "))
      
# if(18<a<99):

#     print("Your age is for above consent")
      
# elif(a<0):
#  print("You are entering an invalid negative age")

# elif(a>=100):
#    print("Your age is not livable ")
   
# else:
#     print("Your age is for below concent")

# print("THE PROGRAM IS END")


# Relational operator and Conditional operator are same

# Practice questions
# 1
# a1=int(input("Enter the number a1 "))
# a2=int(input("Enter the number a2 "))
# a3=int(input("Enter the number a3 "))
# a4=int(input("Enter the number a4 "))

# if(a1>a2 and a1>a3 and a1>a4):
#    print("Greatest number is a1", a1)

# elif(a2>a1 and a2>a3 and a2>a4):
#    print("Greatest number is a2", a2)

# elif(a3>a2 and a3>a1 and a3>a4):
#    print("Greatest number is a3", a3)

# if(a4>a2 and a4>a3 and a1<a4):
#    print("Greatest number is a4", a4)

#2

# m1=int(input("Enter the Maths a1 "))
# m2=int(input("Enter the Physics a2 "))
# m3=int(input("Enter the Chemistry a3 "))

# total_percentage= (m1+m2+m3)/3

# if (total_percentage>=40 and m1>=33 and m2>=33 and m3>33):
#    print("You are pass and your percentage is ", total_percentage)

# else:
#    print("You are fail try again next year !", total_percentage)

 #3

# p1= "Make a lot of money"
# p2= "Buy now"
# p3= "Subscribe this"
# p4= "Click this"

# message = input("Enter your message: ")

# if((p1 in message)or(p2 in message)or(p3 in message)or(p4 in message)):
#    print("Spam messages are not allowed")
# else:
#    print(message)

#3
post = input(" Enter the post : ")

if("harry" in post.lower()):
   print("This post is talking about the harry ")
else:
   print("The post is not talking about the harry ")