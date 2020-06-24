one = dict(name = "kitty", age = 0.5, location = "lagos")
print(one)
print(one ['age'])

#""" selecting items from a dictionary"""

instructor = {
    "name" : "colt", "owns_dog":True, "num_courses" : 4,"favourite_language": "python", "is_hilarious":False, 44: "my favourite number !"
}
print (instructor.values())
for values in instructor.values():
     print(values)
print()

print (instructor.keys())
for k in instructor.keys():
    print(k)
print()
    # to get both keys and values use .items()
print(instructor.items())
# using a for loop to get both the keys and values
for k,v in instructor.items():
    print(k,v)
    print ()
   # wish to make it more detailed
    print(f"key is {k} and value is {v}")
    
    # to retrieve  a key  in an object use the .get()
print(instructor.get("favourite_language"))
print (instructor.get("norm"))
# creates key _value pairs from  csv from.keys
print({}.fromkeys(["email"],"unknown"))
print({}.fromkeys("email" , "phone")) 
print({}.fromkeys(range(1,10), "zee"))
# to clear a dictionary
d= dict(a=1,b= 2,c=4)
print (d)
d.clear()
print (d)
# to copy/clone use the copy()
c= dict(a=1,b= 12,c=4)
print (c)
b = c.copy()
print("c is being copied to b")
print (b)
# pop() to remove an item from dictionary
print(instructor.pop("name"))
print(instructor)
# popitem removes an item randomly and takes no argument
print(instructor.popitem())
print(instructor.popitem())
# updating a dict update()
zee = {"color" : "yellow"}
zee.update(instructor)
print(zee)
zee["house"] = "onike"
print(zee)


