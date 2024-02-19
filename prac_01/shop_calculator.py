total_price = 0

number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid input")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_items = float(input("Price of item: "))
    total_price += price_of_items

if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount

print(f"Total price for {number_of_items} items is ${total_price:,.2f}")


