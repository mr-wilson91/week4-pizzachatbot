userName = input("\nEnter your name: ").lower()

if userName == "tyquan wilson":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
else:
    print(f"\nHello, {userName}. Nice to meet you!")

# Gather Pizza Order Info
size = input("What size pizza? (small, medium, large): ").lower()
flavor = input("What flavor? (cheese, pepperoni, veggie, etc.): ").lower()
crustType = input("What crust type? (thin, regular, stuffed): ").lower()
quantity = int(input("How many pizzas do you want?: "))
orderType = input("Delivery or carryout?: ").lower()

# Price Based on Size
if size == "small":
    pizzaCost = 8.99
elif size == "medium":
    pizzaCost = 14.99
elif size == "large":
    pizzaCost = 17.99
else:
    pizzaCost = 14.99  # Default value

# Delivery Fee Logic
if orderType == "delivery":
    deliveryFee = 5.00
else:
    deliveryFee = 0.00

# Tax and Total
salesTax = 1.10
total = (pizzaCost * quantity * salesTax) + deliveryFee

# Order Summary
print("-" * 40)
print(f"Thank you, {userName.title()}, for your order.")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:.2f}.")

# Discount Logic
if total >= 50:
    print("Congratulations! You've been awarded a $10 Off coupon for your next order.")
else:
    print("Order over $50 will receive a free $10 Off coupon!")
print("-" * 40)