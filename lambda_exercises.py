''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda num: (num % 2 == 0), number_list))
print(filtered_list)

filtered_list = list(filter(lambda num: (num % 2 == 1), number_list))
print(filtered_list)


''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

days = list(filter(lambda x: len(x)==6, weekdays))
print(days)






''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''

color_list = ['orange', 'red', 'green', 'blue', 'white', 'black']
#update_list = list(filter(lambda color: color != 'orange' and color != 'black', color_list))
#print(update_list)

#or

remove = ['orange', 'black']
update_list = list(filter(lambda color: color not in remove, color_list))
print(update_list)








''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
update_list = list(filter(lambda x: x not in list2, list1))
print(update_list)




''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
list1 = ['red', 'black', 'white', 'green', 'orange']
search1 = list(filter(lambda x: 'ack' in x, list1))
print(search1)
search2 = list(filter(lambda x: 'abc' in x, list1))
print(search2)





''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

#str1 = "Hello8world"
str1 = "HELLO"
#str1= "hello"

check = lambda x: any([y.isupper() for y in x] and
                       [y.islower() for y in x] and
                       [y.isdigit() for y in x] and
                       [len(x)>7])
if check(str1):
    print("pass")
else:
    print("fail")










''' 7)
Write a Python program to sort a list of tuples using Lambda.      

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result: lambda + sort
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
scores = sorted(original_scores, key = lambda x: x[1])
print(scores)