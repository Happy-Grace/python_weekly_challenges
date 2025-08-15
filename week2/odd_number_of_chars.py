# Create a program that stores a list of words. 
# Then, use list comprehension to create a new list 
# that contains only the words that have an odd number of characters.


# CREATE A LIST OF WORDS
words = ["apple", "banana", "mango", "kiwi", "beetroot", "cashew", "orange", "tangerine", "lemon"]

odd_fruits = [word for word in words if len(word) % 2 != 0]

print(f"New List containing odd character fruits: {odd_fruits}\n")

# Print each fruit in the new list
print(f"Fruits and the number of odd characters it contains: ")
for i in odd_fruits:
    print(f"{i} has {len(i)} characters.")


# ANOTHER WAY

print("\nANOTHER METHOD!")
# Ask user for input
fav_fruits = [
    input(f"Please enter ten of your favourite fruits: Fruit #{i+1}: ")
    for i in range(10)
]

# Now, let's make a new list using list comprhension of fruit with odd number of characters.
odd_fav_fruits = [fruit for fruit in fav_fruits if len(fruit) % 2 != 0]

print(f"\nYour favorite fruits with odd number of characters:")

# Print each fruit in the new list
for i in odd_fav_fruits:
    print(i)



