# Create a program that asks for the user’s name and favorite color, 
# then prints a personalized greeting like: 
# “Hello, [Name]! Your favorite color, [Color], is awesome!”

# Ask for User's Input.
first_name = input("Enter yor first name: ")
# middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")

color = input("Enter your favourite color: ")

full_name = f"{first_name} {last_name}"
# full_name = first_name + " " + " " + last_name

print(f"Hello, {full_name}! Your favourite colour(s), {color}, is/are awesome!.")