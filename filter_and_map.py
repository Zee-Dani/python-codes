names = ["leo","colt","debo","gabby", "mickies"]
# return a new list with the string "your instructor is "+ each value in the array,but onli if the value is less than 4 characters
Instructor = list (map(lambda name: f"Your instructor is {name}",
          filter(lambda value:len(value) < 4,names)))

print(Instructor)

