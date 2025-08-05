friends=["Apple","Orange,54,false,kash","Rohan"]

print(friends[0])
# IN string we can't change the data in the string they are immutable
# but we can change in the tuple/list
friends[0]= "grapes"
print(friends[0])

# list_methods in Python
friends.append("Harry")
print(friends)
l1=[1,5,6,2,22,58]
# l1.sort()
l1.reverse(
)
l1.insert(3,233333)#insert 33333 after the index 3
l1.pop(3)
value =l1.pop(3)
print(value)
print(l1)