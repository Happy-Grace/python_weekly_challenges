# Write a program that accepts user input to create a list of integers.
# Then, compute the sum of all the integers in the list.

user_input = input("Enter integer numbers separated by spaces(e.g 10 20 21): ")

print("")
num = list(map(int, user_input.split()))


print(f"List created using user's input: {num}.\n")

# Finding the total of the list of numbers
# Sum of numbers in a list using the sum() method
total = sum(num)
print(f"The total sum of numbers in the list created: {total}.\n")



# Finding the total of the list using for loop
total_sum = 0
expression = ""
for i in range(len(num)):
    total_sum += num[i]
    expression += str(num[i])
    if i != len(num) - 1:
        expression += " + "

print(f"Total sum: {expression} = {total_sum}")

