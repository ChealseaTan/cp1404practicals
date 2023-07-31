# 1.)
# Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
# Remember to close your file.
name = input("Enter name: ")
out_file = open('name.txt', 'w')
print(name, file=out_file)
out_file.close()

# 2.)
# (In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name (as above)
# then prints, "Your name is Bob"( or whatever the name is in the file).
in_file = open("name.txt", "r")
user_name = in_file.read()
print(f"Your name is {user_name}")

# 3.)
# Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, which should be... 59.
in_file = open("numbers.txt", "r")
number_one = int(in_file.readline().strip())
number_two = int(in_file.readline(2).strip())
in_file.close()
total = number_one + number_two
print(total)

# 4.)
# Now write a fourth block of code that prints the total for all lines in numbers.txt or
# a file with any number of numbers.
