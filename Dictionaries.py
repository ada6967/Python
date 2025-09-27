Student={
"Name":"Surname",
"Age":1,
"Class":1
}
print(Student)

#Empty dictionary:
Q={}
print(Q)

#Method 2:
Cat=dict({
"Name":"q",
"Age":1
})
print(Cat)

#Mixing data types in a dictionary:
q={
"Fruit":"Mango",
1:[1,2,3,4,5]
}
print(q)

#Accessing a dictionary:
Dog={
"Name":"Q",
"Age":1,
"Breed":"Husky",
"Colour":"White"
}
print(Dog)
print(Dog["Name"])
print(Dog["Colour"])
print(Dog["Age"])

#Updating a dictionary:
House={
"Name":"W",
"Age":1,
"Colour":"White"
}
print(House)
House["Age"]=2
print(House)

#Deleting a key value pair:
del House["Colour"]
print(House)

#Nested dictionary(dictionary inside dictionary):
People={
1:{"Name":"w", "Age":1},
2:{"Name":"E", "Age":1},
}
print(People)

#Accessing nested dictionaries values:
print(People[1]["Name"])