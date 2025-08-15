# Write a program that uses a dictionary to store information about a person, 
# such as their name, age, and favorite color. 
# Ask the user for input and store the information in the dictionary. 
# Then, print the dictionary to the console


# ANSWER

# Ask user for input about their Name, Age and Favourite Colour.
name = input("Please enter your name (e.g John Doe): ")

age = int(input("How old are you: (can only be an integer e.g 20): "))

fav_color = input("Enter your favourite colour: ")


# Store users input into a disctionary
user_info = {}

user_info["Name"] = name
user_info["Age"] = age
user_info["Colour"] = fav_color

print("")

print(f"User's Information: ")
# print("")
for key, value in user_info.items():
    print(f"{key}: {value}")