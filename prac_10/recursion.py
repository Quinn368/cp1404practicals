def do_it(n):
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

print(do_it(5))


def do_something(n):
    if n < 0:
        return
    print(n ** 2)
    do_something(n - 1)

do_something(4)


def calculate_blocks(rows):
    if rows <= 0:
        return 0
    return rows + calculate_blocks(rows - 1)


def build_pyramid():
    chosen_rows = int(input("How many rows is your pyramid: "))
    print(f"For {chosen_rows} rows, you need {calculate_blocks(chosen_rows)} blocks")


# Function to calculate the number of blocks using a loop
def calculate_blocks_loop(rows):
    total_blocks = 0
    for i in range(1, rows + 1):
        total_blocks += i
    return total_blocks

# Recursive function to calculate the number of blocks
def calculate_blocks_recursive(rows):
    # Base case: If rows is 1, return 1
    if rows == 1:
        return 1
    # Recursive case: Add the current row number and call the function recursively with rows-1
    else:
        return rows + calculate_blocks_recursive(rows - 1)

# Get the number of rows from the user
rows = int(input("Enter the number of rows for the pyramid: "))

# Calculate the number of blocks using both methods
blocks_loop = calculate_blocks_loop(rows)
blocks_recursive = calculate_blocks_recursive(rows)

# Print the results
print(f"Number of blocks using loop: {blocks_loop}")
print(f"Number of blocks using recursion: {blocks_recursive}")


calculate_blocks_recursive(6)

build_pyramid()