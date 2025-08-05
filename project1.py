#Snake water and gun game
import random
'''
snake =1
water =0
gun =-1

'''
def random_value():
    return random.choice([1, 0, -1])

computer= random_value()
yourstr=input("Enter your choice ")
yourdict={"s":1,"w":0,"g":-1}
reversedict={1:"Snake",0:"Water",-1:"Gun"} # ye isliye banai gai hei jise mei hum show kr sake ki hum kya input le rhe hei 

you=yourdict[yourstr]
print(f"You chose {reversedict[you]}\n Computer chose {reversedict[computer]}")

# conditons
if(computer==you):
    print("The match is drawn")
else:
    if(you==1 and computer==0):
        print("you win")

    elif(you==1 and computer==-1):
        print("You lose")
        
    elif(you==0 and computer==-1):
        print("You Win")

    elif(you==0 and computer==1):
        print("You lose")

    elif(you==-1 and computer==1):
        print("You Win")

    elif(you==-1 and computer==0):
        print("You lose")
    else:
        print("Something went wrong")    