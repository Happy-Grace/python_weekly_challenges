# Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.

# ANSWER:

# Ask user to enter some integers.
num1 = input("Enter integer numbers separated by whitespaces (e.g 10 22 12 etc.): ")

#Convert the users input into a sorted set and by splitting each integer input and mapping into a set.
set1 = set(map(int, num1.split()))

num2 = input("Enter integer numbers separated by whitespaces (e.g 10 22 12 etc.): ")

#Convert the users input into a sorted set and by splitting each integer input and mapping into a set.
set2 = set(map(int, num2.split()))

print("")

# Unsorted Sets

print(f"Unsorted Set1: {set1}")
print(f"Unsorted Set2: {set2}")

print("")

# Sorted Sets
print(f"Sorted Set1: {sorted(set1)}")
print(f"Sorted Set2: {sorted(set2)}")

print("")
# A new set storing common items found both in set1 and set2
set3 = set1.intersection(set2)

# Unsorted common items
print(f"Common Items Unsorted Set: {set3}")

print("")

# Sorted common items
print(f"Common Items Sorted Set: {sorted(set3)}")
