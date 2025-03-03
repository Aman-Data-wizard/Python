"""this_tuple =("apple", "Banana", "Cherry")
print(this_tuple[-1])#negative indexing

#Range of indexes
this_tuple =("apple", "mango", "cherry",
             "orange", "kiwi", "melon", "grapes")
print(this_tuple[2:5])#returns 3rd 4th and 5th element

this_tuple = ("apple", "mango", "kiwi", "orange", "pine")
print(this_tuple[:4])

#to check if item Exists
this_tuple = ("apple", "banana", "cherry")
if "cherry" in this_tuple:
     print("yes, it's in the fruit tupple")
else:
     print("No!")    """

names = ("Roger", "syd", "Aman", "siuuu")

print (names [0])
print (names [1]) 

print(names.index("Roger"))
print(names.index("syd"))
print(len(names))
print(names[-1])
print("Roger" in names)

#Slicing

print(names[0:3])
print(names[1:])

print(sorted(names))