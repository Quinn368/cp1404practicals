CODE_OF_COLOR = {
    "Amber": "ffbf00",
    "AliceBlue": "f0f8ff",
    "Apricot": "fbceb1",
    "Aqua": "00ffff",
    "Aquamarine1": "7fffd4",
    "Baby Blue": "89cff0",
    "Baby Pink": "f4c2c2",
    "Banana Yellow": "ffe135",
    "Champagne": "f7e7ce",
    "Cherry Blossom Pink": "ffb7c5"}
print(CODE_OF_COLOR)

color_name = input("Enter color code: ").title()
while color_name != '':
    if color_name in CODE_OF_COLOR:
        print(f"{color_name} is {CODE_OF_COLOR[color_name]}")
    else:
        print("Invalid color code")
    color_name = input("Enter color code: ").title()
