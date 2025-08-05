e=set()# Don't use s ={} as it will create an empty dictionary
s={1,5,32,54,5,5,5}

print (s,type(s))
# set should be unordered,not be indexed
#types of tset 

s.add(556)
print(s)
s.remove(1)
print (s,type(s))

#union and intersaction

s1 ={1,3,45,54,34}
s2 ={1,3,4,33}
print(s1.union(s2)) #Saari distinct values ka output de dega
print(s1.intersection(s2)) #Dono mei jo common values o
print(s1-s2)# Do set koi common values of subtract kr skte hei 


# 🧠 Set Comparison & Check
# Method	Description
# issubset(set)	Checks if the current set is a subset of another.
# issuperset(set)	Checks if the current set is a superset of another.
# isdisjoint(set)	Returns True if two sets have no elements in common

#Practice set

# 1
# dicts= {
#     "madad":"Help",
#     "Kursi":"Chair",
#     "Davarja":"Door"


# }
# word= input("Enter the word you want meaning of")

# print(dicts[word])

m=set()
n=input("Enter the number 1 :")
m.add(int(n))
n=input("Enter the number 2 :")
m.add(int(n))
n=input("Enter the number 3 :")
m.add(int(n))
n=input("Enter the number 4 :")
m.add(int(n))
n=input("Enter the number 5 :")
m.add(int(n))
n=input("Enter the number 6 :")
m.add(int(n))
n=input("Enter the number 7 :")
m.add(int(n))
n=input("Enter the number 8 :")
m.add(int(n))
print(m)
