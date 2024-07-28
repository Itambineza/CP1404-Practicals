
# 1. Write code that asks the user for their name, then opens a file called name.txt and writes that name to it.
name = input("What is your name? ")
out_file = open('name.txt', 'w')
out_file.write(name)
out_file.close()

# 2. Write code that opens "name.txt" and reads the name then prints "Hi [name]!"
in_file = open('name.txt', 'r')
name = in_file.read().strip()  # strip to remove any extra whitespace/newline characters
in_file.close()
print(f"Hi {name}!")

# 3. Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints the result
with open('numbers.txt', 'r') as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
    result = num1 + num2
    print(result)  # This should print 59 for the given numbers

# 4. Write code that prints the total for all lines in numbers.txt
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        number = int(line)
        total += number
print(total)
