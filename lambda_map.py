# maps takes a function and an iterable(tuples,strings,list ,dictionaries)

nums = [2,4,6,8,10]

doubles = map(lambda x: x*2 ,nums)
# always tell python to to print in a list  else it will not give you a print out
print(list(doubles))


ladies = ["nonye", " esther","gabby","vicky","love"]
women = map(lambda caps: caps.upper(),ladies)
print(list(women))
