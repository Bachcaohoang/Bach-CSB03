shop={
    "Iphone12":28000000,
    "Samsung N10":16000000,
    "Oppo 93":7500000,
    "Vsmart":7400000,
    "Vivo":4200000
}
#1
a = input('Input name of a phone:')
print("Price of Vsmart:",shop[a])
#2
def get_phones_in_budget():
    budget = int(input("How much money do you have to buy a phone? "))
    suitable_phones = [phone for phone, price in shop.items() if price <= budget]
    if suitable_phones:
        print(f"Here are the phones with prices suitable for your budget of {budget}:")
        for phone in suitable_phones:
            print(f"- {phone}: {shop[phone]}")
    else:
        print(f"Sorry, we don't have any phones in our list that fit your budget of {budget}.")

get_phones_in_budget()