from sys import argv

script, input_file = argv  #import argument from command line

def print_all(f): #define print_all fucntion to read file
    print(f.read())
    return 2

def rewind(f): #define rewind function to go back to start of the file
    f.seek(0)

def print_a_line(line_count, f): # define print_a_line function to print just one line each time
    print(line_count, f.readline())

current_file = open(input_file) #pass the imported file to variable current_file

print("First let's print the whole file:\n")

x = print_all(current_file) # print the file

# print(f"{x}")   print the return value

print("Now Lets rewind, kind of like a tape.")

rewind(current_file)  # rewind the file

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
