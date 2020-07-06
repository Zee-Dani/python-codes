# filter is used to select items from an iterable  and puts them in a new list
# its condition will usually be a boolean

# using the filter to select even numbers from a list

number = [2,4,5,6,7,90,77,11,4,75,79,11,124,67,87,78,54,122,123,234,407,408,500]

evens = list(filter(lambda n:n%2 == 0, number))
print(evens)
# USING FILTER TO SELECT WORD WITH I IN THE MIDDLE FROM WORDS
words = ["ZIP","YID","JAP","DEF","CAF","BIB" ,"JAR", "YIN","JAW ","JAY"," KAB", "LIN","KAE"," KAF" ,"KAI"," MAP"," MAR"]

word_i = filter(lambda wod : wod[1]== "I",words)
print (list(word_i))



