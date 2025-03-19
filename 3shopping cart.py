#shopping cart

item = input("What item?: ")
price = float(input("What is price?: "))
quantity = int(input("How many?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is {total} tk ")