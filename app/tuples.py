my_new_learning = tuple(range (11)) #tuple of numbers from 0 to 9. It cannot be changed. It can be used wherever an immutable sequence of numbers is needed.
print(my_new_learning)
print(type(my_new_learning))  #prints the type of the variable my_new_learning, which is <class 'tuple'>
print("How manny times number 5 appears:",my_new_learning.count(5))  #prints the number of occurrences of the value 5 in the tuple, which is 1
print("Index of number 10:",my_new_learning.index(10))  #prints the index of the first occurrence of the value 5 in the tuple, which is 10
print("Length of the tuple:",len(my_new_learning))  #prints the length of the tuple, which is 11