# 🎲 Practice Task (NumPy): 
	# Create an array with numbers 10 to 50.
	# Find the maximum and minimum values. 
	# Multiply all elements by 3

# Solution: 
import numpy as np

# Create an array from using range from 10 to 50.
my_arrray = np.arange(10, 51)

print(f"My array: {my_arrray}\n")

# Find the max in the array
max_num = my_arrray.max()
print(f"The maximim number in my array is: {max_num}\n")

print(f"Multiplying all elemnets in the array: {my_arrray}.\n\nResult: {my_arrray * 3}.\n")