# Create a tuple containing the names of five of your favorite books. 
# Then, use a for loop to print each book name on a separate line.


# ANSWER:
# Favourite Books
fav_books = ("War Room", "Courageous", "God's Generals", "Alex Rider Series", "Gifted")

print("My favourite books are: ")
for i in range(len(fav_books)):
    print(fav_books[i])

print("\n")
# Another Way

# Asks user for input and stores the input in a List.
user_input = [
    input(f"Enter five of your favourite book #{i+1}: ") 
    for i in range(5)
]

# Stores the book into a tuple
books = tuple(user_input)

# Prints the user's favourite books.
print(f"\nYour favourite books are: ")
for book in books:
    print(book)