# def is_anangram(word1,word2):
#     word1= sorted(word1)
#     word2 = sorted(word2)
#     if word1 == word2:
#         print('True')
#         return True
#     else:
#         print('false')
#         return False
    
# is_anangram('may','did')
# is_anangram('tap','pat')

def is_same(wordx,wordy):
    wordx= sorted(wordx)
    wordy = sorted(wordy)
    if wordx == wordy:
        return True
    else:
         return False
    
    print(is_same('yam','may'))


my_list = [1,2,3]
for i in my_list:
        print(i)
print([i **2 for i in my_list])        


print([x+y for x in range (1,4) for y in range (1,4)])
print()
print ([x+y for x in range (1,3) for y in range (1,3)])


for C in 'Hi There Mom':
    if C.isupper():
