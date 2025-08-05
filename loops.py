# while loops
# i=1

while(i<=50):
    print(i)
    i+=1                            #i=i+1
    
print(i)

i=0
print(type(i))
while(i<5):             # i starts with zero isko dhyan rakhna
    print("Aman")
    i=i+1


# New program 
l=[1,"aman",34,3454.43,True,"Devansh"]
i=0
while (i<len(l)):
    print(l[i])
    i=i+1


# fOR loops

for i in range(100):
    print(i)

Very improtant understanding about the continue and break
for i in range(100):
    if (i==34):
        break #it breaks the loop when 34 comes in the loop
    i+=1 
    print(i)

# continue statement

for i in range(100):
    if (i==34):
        continue #it breaks the loop when 34 comes in the loop
    i+=1 
    print(i)
 
# Table writing without any adding extra variables

# n=int(input("Enter the number: "))

# for i in range(1,11):   
#     print(f"{n} X {i} ={n * i}")


#find the number is prime or not 

# n = int(input("Enter the number "))

# for i in range(2,n):
#     if(n%i==0):
#         print("The number is not a prime number ")
#         break
# else:
#     print("The number is prime number") 

#find the sum of the natural numbers

# n=int(input("Enter the number"))
# i=1
# sum=0
# while(i<=n):
#     sum=sum+i
#     i=i+1
# print(sum)

#find the factorial of the number
# n=int(input("enter the number "))
# product =1

# for i in range(1,n+1):
#     product=product*i
# print(f" The number of {n} factorial is {product}")

#Table should be print as reversed

n=int(input("Enter the number: "))

for i in range(1,11):   
    print(f"{n} X {11-i} ={n * (11-i)}")
    
