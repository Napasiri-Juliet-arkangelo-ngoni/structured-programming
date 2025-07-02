# Menu simple avec choix multiple pour un client

menu = {
    "1": ("Chapati", 1000),
    "2": ("Mandazi", 500),
    "3": ("Rolex", 2500),
    "4": ("Rice + Beans", 3000),
    "5": ("Rice + Beef Stew", 5000),
    "6": ("Soda", 2000),
    "7": ("Fresh Juice", 2500)
}

print("STUDENT MEAL SPOT MENU")
print("Affordable. Delicious. For Students.")
print("Please select the dishes you want by typing their numbers.")
print("Type 'done' when you finish ordering.")

# Afficher le menu
for number, (dish, price) in menu.items():
    print(number + ".", dish, "-", price, "UGX")

order = []
total = 0

while True:
    choice = input("Enter dish number (or 'done' to finish): ")
    if choice.lower() == "done":
        break
    elif choice in menu:
        dish, price = menu[choice]
        order.append(dish)
        total += price
        print("Added", dish, "to your order.")
    else:
        print("Invalid choice, please try again.")

print()
print("Your order:")
for dish in order:
    print("-", dish)

print("Total to pay:", total, "UGX")
print("Thank you for ordering! 😊")