#bai 1
skills = [
    {"Name": "Tackle", "Minimum level": 1, "Damage": 5, "Hit rate": 0.3},
    {"Name": "Quick Attack", "Minimum level": 2, "Damage": 3, "Hit rate": 0.5},
    {"Name": "Strong Kick", "Minimum level": 4, "Damage": 9, "Hit rate": 0.2}
]

level = 2

print("Cho phép:")
for i in range(len(skills)):
    print(f"Skill {i+1}: {skills[i]['Name']}")

while True:
    choice = int(input("Choose skill by number: "))
    if 1 <= choice <= len(skills):
        skill = skills[choice - 1]
        if skill["Minimum level"] <= level:
            print(f"You chose {skill['Name']}.")
            print(f"Damage: {skill['Damage']}")
            break
        else:
            print(f"Cannot deploy. Required level {skill['Minimum level']}.")
            break
    else:
        print("Invalid choice. Please choose again.")
import random

skills = [
    {"Name": "Tackle", "Minimum level": 1, "Hit rate": 0.8, "Damage": 10},
    {"Name": "Quick Attack", "Minimum level": 1, "Hit rate": 0.9, "Damage": 15},
    {"Name": "Strong Kick", "Minimum level": 2, "Hit rate": 0.7, "Damage": 20}
]

level = 2

print("Choose a skill:")
i = 1
for skill in skills:
    print(f"{i}. {skill['Name']}")
    i += 1

while True:
    choice = int(input("Enter the number of your chosen skill: "))
    if 1 <= choice <= len(skills):
        chosen_skill = skills[choice - 1]
        if chosen_skill["Minimum level"] <= level:
            if random.random() < chosen_skill["Hit rate"]:
                print(f"You chose {chosen_skill['Name']}.")
                print(f"Damage: {chosen_skill['Damage']}")
            else:
                print(f"You chose {chosen_skill['Name']}.")
                print("Missed.")
            
        else:
            print(f"Cannot deploy. Required level {chosen_skill['Minimum level']}.")
    else:
        print("Invalid choice. Please choose again.")