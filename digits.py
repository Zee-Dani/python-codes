# x=0
# while x < 100:
# 	x += 1
# 	if x%5 == 0:
# 		print(x)
# 	else:
# 	        print (x, end='')

    
# def word_search(doc_list, keyword):
    
#     keyword=keyword.strip().rstrip('.').lower()
#     new_list=[]
#     for index, doc in enumerate(doc_list):
#         for word in doc.split():
#             if keyword == word.strip().rstrip('.').lower():
#                 new_list.append(index)
#     return new_list

    
# doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
# print (word_search(doc_list, "car"))
    

x = 0
while x < 10:
	print(x,end ='  ')
	x = x+1
print()
print('final value of x :',x )