# Build a program that stores a list of jokes 
# and randomly selects one to display every time the user runs it. 
# Add a fun twist with jokes about Python or programming! 🐍💡


# First import random and time built-in functions for use.


import random
import time

# List of programming & Python jokes stored in a List.
jokes = [
    "Why do Python programmers wear glasses?\nBecause they can't C!",
    "Why did the developer go broke?\nBecause they used up all their cache.",
    "What's a Python's favorite dance move?\nThe snake_case shuffle!",
    "Why was the JavaScript developer sad?\nBecause they didn't know how to 'null' their feelings.",
    "Why did the Python dev break up with the C++ dev?\nToo many class issues.",
    "I told my Python code a joke...\nIt raised an exception.",
    "How does a Python dev fix a broken heart?\nWith a try-except block.",
    "Why do Python devs make great musicians?\nThey know how to handle exceptions in harmony.",
    "Why is Python great at parties?\nIt brings all the packages!",
    "Why was the function feeling depressed?\nBecause it didn’t return anything.",
    "Why did the HTML tag break up with the head tag?\nBecause it wanted more body.",
    "Why do HTML and body never fight?\nBecause they always stay in structure.",
    "Why is HTML so chill?\nIt just lays back and lets CSS do all the styling.",
    "Why did the <div> go to therapy?\nBecause it had too many issues to contain.", 
    "Why did the CSS file go to school?\nTo improve its class!",
    "What’s a CSS developer’s favorite music genre?\nBorder-line punk.",
    "Why was the CSS designer always calm?\nBecause they knew how to keep things in line.",
    "How do you make a website blush?\nApply a little :hover magic!", 
    "Why did the database administrator leave their job?\nThey found it too relational.",
    "Why did the SQL query go to the gym?\nTo improve its joins.",
    "I would tell you a joke about a NULL value…\nBut it doesn’t exist.",
    "Why was the database afraid of commitment?\nIt had too many foreign keys.", 
    "Why did the Python file fail the test?\nBecause it had too many assert issues.",
    "What do you call a snake that writes code?\nA Python developer!",
    "Why did the Python programmer go hungry?\nBecause the food variable was undefined.",
    "How does a Python dev make toast?\ntry: bread.toast()\nexcept: order_pizza()"
]

# Cool intro
intros = [
    "🐍 Here's a byte of humor for you:",
    "💻 Need a laugh? Try this on for size:",
    "😄 Time for a chuckle, coder-style:",
    "🚀 Launching a joke in 3...2...1...",
    "📦 Unpacking today's joke module..."
]

extros = [
    "You're Welcome👊🏽!", 
    "Hope you had a good laugh😙!", 
    "Great proramming minds think alike👏!", 
    "You have a great sense of humour👍!", 
    "Scobby-dobby Doo🤸🏾!"
]

#Function to timely print out Intro and Jokes.
def crack_joke():
    print(random.choice(intros))
    time.sleep(1)  # Dramatic pause
    print( "\n" + "JOKE:")
    print(random.choice(jokes))
    time.sleep(1)

    print("\n" + random.choice(extros))


# The main function to activate/call the jokes function.
if __name__ == "__main__":
    crack_joke()
