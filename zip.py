# zip iterates over an iterable and returns a tuple
# if items are of different  length  it iterates  to the the shortest length


num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]

word = ["hi", "hu", "he", "li", "be", "car", ]
my_zip = zip(num1, num2, word)
print(list(my_zip))

# *star operator is used  to  unpack a tuple
unpack = [(2, 3), (7, 8), (5, 6), (8, 9), (1, 2)]
u = list(zip(*unpack))
print(u)
