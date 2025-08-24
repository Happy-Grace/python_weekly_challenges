import os

# Challenge: 
# Create a program that reads a text file, processes its content, 
# and writes the results to a new file.

# 📌 Task Requirements:
    # Create a file called input.txt and write at least five lines of text into it.
    # Write a Python script to:
        # 1. Read the contents of input.txt.
        # 2. Count the number of words in the file.
        # 3. Convert all text to uppercase.
        # 4. Write the processed text and the word count to a new file called output.txt.
        # 5. Print a success message once the new file is created.


# 1. FIRST, Create a file named input.txt and writeat least five lines of text into it.
with open("C:\\Users\\Didi\\Desktop\\PLP Assignments\\Python\\python_weekly_challenges\\week4\\input.txt", "w") as my_file:
    my_file.write("Lorem ipsum dolor sit amet consectetur adipisicing elit.\n")
    my_file.write("Magnam, repellat tempora molestiae doloremque mollitia ab id\n")
    my_file.write("ratione possimus autem quaerat.\n")
    my_file.write("Placeat quod, dolorem eaque officia\n")
    my_file.write("praesentium velit cumque illum consequatur.\n")
    
# Note: 
    # The file was created directly at the same directory address path 
    # with the <file_handling.py> python script.
    # To create file = open("directory_address_path\\filename.txt", "w")

# To append into my_file
with open("C:\\Users\\Didi\\Desktop\\PLP Assignments\\Python\\python_weekly_challenges\\week4\\input.txt", "a") as my_file:
    my_file.write("This is an appended line.\n")
    my_file.write("This is another appended line.\n")
    my_file.write("This is the third appended line.\n")
    my_file.write("This is the fourth appended line.\n")
    my_file.write("This is the fifth appended line.\n")

# print("")

# 2. To read the contents of the file <input.txt>
with open("C:\\Users\\Didi\\Desktop\\PLP Assignments\\Python\\python_weekly_challenges\\week4\\input.txt", "r") as my_file:
    for line in my_file:
        line = line.rstrip()
        print(line)

print("")

# 3. Convert all text to uppercase.
with open("C:\\Users\\Didi\\Desktop\\PLP Assignments\\Python\\python_weekly_challenges\\week4\\input.txt", "r") as my_file:
    for line in my_file:
        line = line.upper()
        line = line.rstrip()
        print(line)
print("")

# 4. Count the number of words in the file.
with open("C:\\Users\\Didi\\Desktop\\PLP Assignments\\Python\\python_weekly_challenges\\week4\\input.txt", "r") as my_file:
    # Used to extraxt the name of the created file, 'import os' to use
    file_name = os.path.basename(r"C:\Users\Didi\Desktop\PLP Assignments\Python\python_weekly_challenges\week4\input.txt")
    
    # Let's read the file contents
    contents = my_file.read()

    # Then, let's split each word in the content, defaultly separated by whitespaces.
    word = contents.split()
    word_count = len(word)

print("")

# 5. Write the processed text and the word count to a new file called output.txt.
with open(r"C:\Users\Didi\Desktop\PLP Assignments\Python\python_weekly_challenges\week4\output.txt", "w") as processsed_file:
    output_content = f"The total number of words in `{file_name}` is {word_count}.\n"
    processsed_file.write(output_content)

    processed_file_name = os.path.basename(r"C:\Users\Didi\Desktop\PLP Assignments\Python\python_weekly_challenges\week4\output.txt")

    # Successful Createion Message.
    print(f"The processed file `{processed_file_name}` has successfully been created.\n")
print("")


    # new_file = open("C:\\Users\\Didi\\Desktop\\PLP Assignments\\Python\\python_weekly_challenges\\week4\\input.txt", "w")


