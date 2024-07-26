import numpy as np

# 1 convert list into array

list1 = [1, 2, 3, 4, 5]
arr1 = np.array(list1)
print(arr1)


# 2 convert list into array then display the array then display first and last index then multiply each element by two and display result
 
list1 = [1,2,3,4,5]
arr1 = np.array(list1)
print(arr1)
print("first element: " ,arr1[0])
print("last element: " ,arr1[-1])
arr2 = arr1 * 2
print("Array with each element multiplied by two: ", arr2)


# 3 write a numpy program to create an array of 10 zero , 10 ones and 10 fives

zeros_array = np.zeros(10)
ones_array = np.ones(10)
fives_array = np.full(10, 5)
print("Array of 10 zeros: ",zeros_array)
print("\nArray of 10 ones: ",ones_array)
print("\nArray of 10 fives: ",fives_array)


# 4 Write a numpy program to create  3*3 matrix with values ranging form 2 to 10
values = np.arange(2, 11)
matrix = values.reshape((3, 3))
print("3x3 matrix with values ranging from 2 to 10: ",matrix)