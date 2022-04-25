# question 1
# #    assign the variable x to 2 and y to 3

# x, y = 2, 3 # the pythonic way <*^*> less readable
# print (x,y)
# #    clear the variable x
# del x
# print(y)
# # print(x) 


# Question 2
# print(x)

# Question 3
# import math


# x,y = 10,3

# # u = x + y
# u = x+y

# # v = xy
# v = x*y

# # w = x/y
# w = x/y

# # z = sin(x)
# z = math.sin(x)

# # r = 8sin(x) 
# r = 8*math.sin(x)

# # s = 5sin(xy)
# s = 5*math.sin(x*y)

# # p = x**y
# p = x**y


# Question 3
# # Assign string ‘123’ to the variable S.
# # Convert the string into a float type and assign the output to the variable N.
# # Verify that S is a string and N is a float using the type function.
# S = '123'
# N = float(S)
# print(f"type of S={S} is {type(S)}, and N={N} is {type(N)}")

# Question 4
# # Assign the string ‘HELLO’ to the variable s1 and the string ‘hello’ to the variable s2.
# # Use the == operator to show that they are not equal.
# # Use the == operator to show that s1 and s2 are equal if the lower method is used on s1.
# # Use the == operator to show that s1 and s2 are equal if upper method is used on s2.

# s1 = "HELLO"
# s2 = "hello"
# if s1==s2: print("there are not equal strictly");
# if s1.lower()==s2: print("there are equal esantialy lower first are equaled");
# if s1==s2.upper(): print("there are equal esantialy upper first are equaled");


# Question 5
# # Use the print function to generate the following strings.
# role = "Engineering"
# obje = "Book"
# print(f"the word '{role}' has {len(role)}")
# print(f"the word '{obje}' has {len(obje)}")

# Question 6
# Check if ‘Python’ is in ‘Python is great!’.
# objWord = "Python"
# target = "Python is great!"

# print(objWord in target)

# Question 7
# # Get the last word ‘great’ from ‘Python is great!’
# target = "Python is great!"
# print(target.removesuffix('!').split()[-1])

# Question 8
# # Assign list [1, 8, 9, 15] to a variable 
# # list_a and insert 2 at index 1 using the insert method.
# # Append 4 to the list_a using the append method.
# # then Sort the list_a in problem 10 in ascending order.
# list_a = [1, 8, 9, 15]
# list_a.insert(1,2)
# list_a.append(4)
# list_a.sort()
# print(list_a)

# Question 9
# Turn ‘Python is great!’ to a list.

# target = "Python is great!"
# print(list(target))

# Question 10
# create one tuple with element ‘One’, 1 and assign it to tuple_a

# tuple_a = ('One',)
# print(tuple_a)

# the rest of the exercices 
# https://pythonnumericalmethods.berkeley.edu/notebooks/chapter02.08-Summary-and-Problems.html#problems


# Question 11
# # Get the unique element from (2, 3, 2, 3, 1, 2, 5).
# mytuples = tuple(set((2, 3, 2, 3, 1, 2, 5)))
# print(mytuples)

# Question 12
# # Assign (2, 3, 2) to set_a, and (1, 2, 3) to set_b. Get the following:
# # union of set_a and set_b
# # intersection of set_a and set_b
# # difference of set_a to set_b using difference method
# set_a = {2, 3, 2}
# set_b = {1, 2, 3}

# print(set_a | set_b)
# print(set_a & set_b)
# print(set_b - set_a)

# Question 13

# # Create a dictionary that has the keys ‘A’, ‘B’, ‘C’
# # with values ‘a’, ‘b’, ‘c’ individually. Print all the keys in the dictionary.

# di = { 'A':'a', 'B':'b', 'C':'c' }
# print(di.keys())
# print('B' in di.keys())

# Question 14

# import numpy as np

# arr = np.linspace(-10,10,100)
# print(arr)

# Question 15

# import numpy as np

# #   Let array_a be an array [-1, 0, 1, 2, 0, 3].
# #   Write a command that will return an array consisting of
# #   all the elements of array_a that are larger than zero.
# #   Hint: Use logical expression as the index of the array.

# array_a = np.array([-1, 0, 1, 2, 0, 3])
# array_b = array_a[array_a>0]

# print(array_b)


# Question 16

# import numpy as np

# #    Create an array y=⎛⎝⎜323528359⎞⎠⎟ and calculate the transpose of the array.

# array_a = np.array([[3, 5, 3],[2, 2, 5],[3, 8, 9]])
# print(array_a.T)

# #   create a zero array with size (2, 4).
# array_a = np.zeros((2,4))
# array_a[:,1] = 1
# print(array_a)
