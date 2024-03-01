# 1
output_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=output_file)
output_file.close()

# 2
input_file = open("name.txt", "r")
name = input_file.read().strip()
input_file.close()
print(f"Your name is {name}")

# 3
input_file = open("numbers.txt", "r")
first_number = int(input_file.readline().strip())
second_number = int(input_file.readline().strip())
input_file.close()
print(first_number + second_number)

# 4
total = 0
input_file = open("numbers.txt", "r")
output_file = open("numbers.txt", "a")
for line in input_file:
    number = int(line)
    total += number
print(total, file=output_file)
input_file.close()
output_file.close()
