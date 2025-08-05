# class employees:
#     name="Aman" #class attributes
#     language= "Python for data analyst" #class attributes
#     salary=1200000 #class attributes


# Aman=employees()
# Aman.name="Aman" #This is the Instance attribute not the class attribute
# print(Aman.name,Aman.language,Aman.salary)

# sahil=employees()
# sahil.name="Sahil" #This is the Instance attribute not the class attribute
# print(sahil.name,sahil.language, sahil.salary)

# vivek=employees()
# vivek.name="Vivek"#This is the Instance attribute not the class attribute
# print(vivek.name,vivek.salary,vivek.language)  

# #Instance attributes>> object attribute always takes place to the priority
# # ex
# raman=employees()
# # raman.language="C++"
# print(raman.language,raman.salary)

#constructor attributes which is used in many cases it is really important 
# class employees:
#     name="Aman" #class attributes
#     language= "Python for data analyst" #class attributes
#     salary=1200000 #class attributes

#     def __init__(self,name,salary,language):  #dundar method which is automatically called
#         self.name=name
#         self.salary=salary
#         self.language=language
#         print("I'm creating the projects")

#     def getinfo(self):
#         print(f"The language is {self.language}")

# Aman=employees("Vikram",454444444,"AI")    
# # print(Aman)
# Aman.name="AMAN"
# print(Aman.name,Aman.salary,Aman.language)


#Practice questions
# class Programming:
#     company="Microsoft" #class attribute
#     def __init__(self,name,salary,pin):
#         self.name=name
#         self.salary=salary
#         self.pin=pin
    
# p=Programming("Aman", 3000000,208027)
# print(p.name,p.salary,p.pin,p.company)
# r=Programming("ROHIT",1200000,202057)
# print(r.name,r.salary,r.pin,r.company)

#2 Making the calculators
# class Calculator:
#     def __init__(self,n):
#         self.n=n

#     def square(self):
#         print(f"The  square of {self.n} number is {self.n*self.n}")

#     def cube(self):
#         print(f"The cube of {self.n} is {self.n*self.n*self.n}")

# a=Calculator(4)
# a.square()
# a.cube()

#3 Train check status question

from random import randint

class train:
    def __init__(self,TrainNo):
        self.TrainNo= TrainNo
    
    def book(self,fro,to):
        print(f"The ticket is booked in train no. : {self.TrainNo} from {fro} to {to}")
    
    def getstatus(self,fro,to):
        print(f"Train no. : {self.TrainNo} is running on time")

    def getfare(self,fro,to):
        print(f"Ticket fare in train no. {self.TrainNo} is {randint(444,7412)}")   

Train=train(13452)        
Train.book("kanpur","Delhi")
Train.getstatus("kanpur","Delhi")
Train.getfare("kanpur","Delhi")
