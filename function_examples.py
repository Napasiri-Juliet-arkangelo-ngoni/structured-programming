#  Simple menu with multiple choices for a customer

menu = {
    "1": ("Chapati", 1000),
    "2": ("Mandazi", 500),
    "3": ("Rolex", 2500),
    "4": ("Rice_Beans", 3000),
    "5": ("Rice_Beef_Stew", 5000),
    "6": ("Soda", 2000),
    "7": ("Fresh_Juice", 2500),
    "8": ("Black_tea", 1000),
    "9":("Milk_tea", 2000),
    "10":("Cake", 2000),
    "11":("Omelets", 2500),
    "12":("Sambuusa", 1000),
    "13":("Rice_chicken_matooke", 10000),
    "14":("Rice_groundnuts_matooke", 6000)
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