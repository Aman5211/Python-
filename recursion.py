# #Recursion 
# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)

# n = int(input("Enter the number: "))

# print(f"The factorial is done by the help of recursion is {factorial(n)}")

#Problem 1
# def greatest_number(a,b,c):
#     if(a>b and a>c):
#         print(f"The greatest number is {a}")
#     elif(b>a and b>c):
#         print(f"The greatest number is {b}")
#     else:
#         print(f"The greatest number is {c}")

# a = int(input("Enter the number a "))
# b = int(input("Enter the number b "))
# c = int(input("Enter the number c "))

# greatest_number(a,b,c)

#Problem 2
'''
sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3
sum(4) = 1+2+3+4
sum(5) = 1+2+3+4+5 
sum(n) = 1+2+3+4+5+.......+n
OR
sum(n) = (n-1) + n

'''
# def sum_naturalnumber(n):
#     if(n==1):
#         return 1
#     return sum_naturalnumber(n-1)+n

# print(sum_naturalnumber(4))

#Problem

# def rem(l,word):   
#     n=[]
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n


# l=["harry","aman","rohit","Sahil"]
# print(rem(l,"an"))

def multiplication(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

a = int(input("Enter the number "))
multiplication(a)
