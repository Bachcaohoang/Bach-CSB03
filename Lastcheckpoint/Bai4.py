
ordered_dishes = []
while True:
    dish = input("Please choose a dish: ")

    if dish in ordered_dishes:
        print(f"You chose {dish} already. Anything  {dish}.")
    else:
        ordered_dishes.append(dish)
        print(f"{dish} added to your order.")

    response = input("Great choice! Anything else? (y/n): ")
    if response.lower()!= "yes":
        break
print("Your order:")
for dish in ordered_dishes:
    print(dish)