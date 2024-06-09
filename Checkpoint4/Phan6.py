#Bai1-
Character={
"Name": "Light",
"Age": 17,
"Strength": 8,
"Defense": 10,
"HP": 100,
"Backpack": ["Shield, Bread Loaf"],
"Gold": 100,
"Level": 2
}
#Bai2
Character["Gold"]+= 50
for x,y in Character.items():
    print(x,y)
#Bai3
Character["Backpack"].append("FlintStone")