# Challenge: Use popular Python libraries to perform useful tasks!
	# 📌 Task Requirements:
		# Import the following libraries:
		# pandas (for data manipulation)
		# numpy (for numerical operations)
		# matplotlib (for data visualization)
		# requests (for making web requests)
	
	# Complete the following tasks using the libraries:
		# a. Create a NumPy array of numbers from 1 to 10 and calculate the mean.
		# b. Load a small dataset into a pandas DataFrame and display summary statistics.
		# c. Fetch data from a public API using requests and print a key piece of information.
		# d. Plot a simple line graph using matplotlib (e.g., a list of numbers).

# SOLUTION: 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# a). Array Creation and Mean Calculation:
my_array = np.arange(1, 11)
print(f"Array: {my_array}")
print()

print(f"Mean Calulated: {my_array.mean()}\n")


# b). Pandas DataFrame
students = {
    'Name': ["Lisa", "Rose", "Jisoo", "Jennie", "San", "Vernon", "Sana"], 
    'Age': [28, 28, 30, 29, 26, 28, 29], 
    'Nationality': ["Thai", "Korean-Australian", "Korean", "Korean", "Korean", "Korean-American", "Japanese"], 
    'Gender': ["Female", "Female", "Female", "Female", "Male", "Male", "Female"], 
}

df = pd.DataFrame(students)

print("My Datasets: \n")
print(df)

new_data = {'Name': 'Jun', 'Age': 32, 'Nationality': 'Chinese', 'Gender': 'Male'}

df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

print("New Data Row Added: \n")
print(df)
print()

print("DataFrame Head (first 5 rows): \n")
print(df.head())
print()

print("\nSummary Statistics: \n")
print(df.describe())



# c). Using Requests to Fetch Data

# Fetch data from public API
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    # Print the title of the first post
    print("First post title:", data[0]['title'])
else:
    print("Failed to fetch data:", response.status_code)




# d). Simple Line Graph: 
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plot line graph
plt.plot(x, y, marker='o', linestyle='dashed', color='blue')
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

