thisdict={
    'class_name':'CSB03',
    'year':2024,
    "student_count":10
}
# # print(thisdict['class_name']) 
# # or
# x = thisdict['class_name']
# print(x)

#print(len(thisdict)) # độ dài
#thisdict['student_count']=9      #'change valuables'
#thisdict["new_student"] ='quynh anh' # add
#thisdict.pop('new_studnet') #delete dong cuoi
#for x in thisdict: #get key    or#for x in thisdict.keys():
  #  print(thisdict)                 #  print(x)  
#for x in thisdict: # get valuables   or for x in thisdict.values():  
  #  print(thisdict[x])                      #print(x)
#for x,y in thisdict.items(): #get key and valuable
#    print(x,y)
#new_thisdict=thisdict.copy()      #copy
#or
#new_thisdict=dict(thisdict)

my_class ={
    "student1":{
        'name':"bach",
        "age":17
    },
    "student2":{
        'name':"hieu",
        "age":17
    },
     "student3":{
        'name':"khoa",
        "age":17
    }
}
#print(my_class)
#print(my_class["student1"]["name"])
# for x in my_class.values(): #get exactly values
#     print(x['name'])
#or
# for x,y in my_class.items():
#     print(y['name'])
# for x,y in my_class.items():
#     print(x)  

#practice
# Bài I) Init dictionary - Dưới đây là thông tin về số lượng máy tính theo hãng trong 1 kho của một shop:
# HP: 20
# DELL: 50
# MACBOOK: 12
# ASUS: 30
# - Khai báo 1 dictionary để biểu diễn thông tin trên
# - Read - Hiện ra số lương MACBOOK có trong kho
# - Read - with key from input - Lặp lại câu 2 với hãng máy tính nhập bởi người dùng
# for y in shop:
#      print(shop["MACBOOK"])
#1
shop={
"HP":20,
"DELL":50,
"MACBOOK":12,
"ASUS":30
}
# print(shop)
#print(shop["MACBOOK"])
# a = input("nhập hãng máy: ")
# print(shop[a])

# Bài II) Init character dictionary - Dưới đây là mô tả một nhân vật trong 1 text adventure:
# Name: Light
# Age: 17
# Strength: 8
# Defense: 10
# HP: 100
# Bd, Bread Loaackpack: Shielf
# Gold: 100
# Level: 2
# Sử dụng 1 dictionary để mô tả nhân vật này
# - Update character dictionary - Không chỉnh sửa khai báo, thêm 50 Gold cho nhân vật này
# - Update character dictionary (2) - Không chỉnh sửa khai báo, thêm FlintStone vào Backpack của nhân vật này
# - Update character dictionary (3) - Không chỉnh sửa khai báo, thêm mô tả Pocket cho nhân vật, 
#trong Pocket chứa 1 danh sách các vật dụng bao gồm MonsterDex và Flashlight
#bai 2
"""
character = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 2
}
#1
character["Gold"] += 50
#2
character["Backpack"].append("FlintStone")
#3
character["Pocket"] = ["MonsterDex", "Flashlight"]
print(character)
"""
# Tạo một dictionary lưu trữ thông tin chi tiết về học sinh, bao gồm tên, tuổi và điểm số. Ví dụ:

# students_details = {
#     "Alice": {"age": 20, "score": 85},
#     "Bob": {"age": 22, "score": 92},
#     "Charlie": {"age": 21, "score": 78}
# }

# 1. Kiểm tra xem "David" có tồn tại trong dictionary students_details hay không. 
#Nếu có, in ra thông tin của David. Nếu không, in ra thông báo "David không có trong danh sách".
# 2. Sắp xếp các học sinh theo điểm số giảm dần và in ra màn hình.

#1
students_details = {
    "Alice": {"age": 20, "score": 85},
    "Bob": {"age": 22, "score": 92},
    "Charlie": {"age": 21, "score": 78}
}
# if "David" in students_details:
#     print(students_details["David"])
# else: print("David is not on the list")
#for i in len(students_details):
#2
sorted_students = sorted(students_details.items(), key=lambda x: (x[1]['score'], x[1]['age']))

for student, details in sorted_students:
    print(f"Name: {student}, Age: {details['age']}, Score: {details['score']}")
