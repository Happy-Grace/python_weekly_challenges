# Divisible By Ten:
# Create a function that determines whether or not a number is divisible by ten. 
# A number is divisible by ten if the remainder of the number divided by 10 is 0. 
# Using this, we can complete this function in a few steps:

# Define the function header to accept one input num 
# Calculate the remainder of the input divided by 10 (use modulus) 
# Use an if statement to check if the remainder was 0. 
# If the remainder was 0, return True, otherwise, return False


# Define the function
def divisible_by_ten(num):
    
    # Condition statement to check if the number 'num' is divisible by 10.
    if num % 10 == 0:
        return True
    else:
        return False

# Test Run the Function with Various Numbers
print(divisible_by_ten(5))
print(divisible_by_ten(10))
print(divisible_by_ten(28))
print(divisible_by_ten(1000))
print(divisible_by_ten(-10))
print(divisible_by_ten(-100))
print(divisible_by_ten(12))
print(divisible_by_ten(191))
