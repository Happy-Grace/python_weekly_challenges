# 🧪 Practice Tasks
	# Create a bar chart showing 5 different countries and their population.
	# Create a pie chart showing how a student spends 24 hours of their day.
	# Make a line chart that shows temperature 
    # changes during the day (morning, noon, evening, night).

import matplotlib.pyplot  as plt

# 1. Bar Chart Creation:
countries = ["Nigeria", "Ethiopia", "Egypt", "Tanzania", "Kenya"]
population = [216522900, 120812698, 112156692,  63298550, 56215221]

# Plot
plt.bar(countries, population, color = 'violet')
plt.title("Five African Countries And their Population")
plt.xlabel("Countries")
plt.ylabel("Population")
plt.show()


# Pie Chart Creation:
my_labels = ["Sleep", "School/Classes", "Homework/Studying", "Meals", "Leisure", "Exercise/Physical Activity", "Others"]
hours = [8, 6, 3, 2, 3, 1, 1]
color = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen', 'violet', 'gray', 'brown']

# Plot
plt.figure(figsize=(9,9))
plt.pie(hours, labels=my_labels, colors=color, autopct='%1.1f%%', startangle=140)
plt.title("Student's Hours Division in a Day.")
plt.show()


# Line Chart Creation: 

time_of_the_day = ["morning", "noon", "evening", "night"]
temp = [15, 25, 20, 12] # In °C Degrees.

# Plot
plt.plot(time_of_the_day, temp, marker='o', linestyle="dashdot", color="green")
plt.title("Temperature Changes During the Day")
plt.xlabel("Time of the Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.ylim(0, 30)
plt.show()
