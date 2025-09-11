# 📊 Practice Task (Pandas)
	# Create a DataFrame with 3 students: name, age, and grade.
	# Add a column called “Passed” where grade > 50 = True.
	# Filter and display only students who passed.

# SOLUTION:

import pandas as pd

students = {
    'name': ['Bob', 'Alice', 'Lily', 'Rose', 'Jennie', 'Max', 'Nate', 'Mali', 'Ben', 'Cooper'], 
    'age': [26, 25, 22, 23, 24, 29, 32, 30, 28, 29], 
    'grade': [73, 80, 95, 67, 60, 50, 49, 45, 32, 77]
}

df = pd.DataFrame(students)

print(f"My created DataFrame: \n")
print(df)

print()

# Adding the Passed to the DataFrame, where grade > 50
df['Passed'] = df['grade'] > 50
print("Printing the DataFrame where 'Passed' column is added: \n")
print(df)

print()

passed_students = df[df['Passed']]
print("Printing only those who Passed: ")
print(passed_students)
