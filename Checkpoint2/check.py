#Phần 1. Thời gian: 10 phút
#1. Init color list:Viết chương trình khởi tạo một list chứa ít nhất 3 string
#đại diện cho 3 màu. Ví dụ: “blue”, “red", “teal", “green”
#a=list(("blue","red","green"))

#2. Print colorlist
#Sử dụng lại list ở Bài 1, viết chương trình in ra tất cả các màu trong list.
# a=list(("blue","red","green"))
# print('Color list:\n',a)

# 3. Update color
# list
# Sử dụng lại list ở Bài 1, viết chương trình hỏi người
# dùng muốn thêm màu gì vào list. Sau khi người dùng
# nhập, thêm màu này vào cuối list.
# a =str(input("Input a new color:"))
# b=list(("blue","red","green"))
# b.append(a)
# print(b)
# Phần 2. Thời gian: 15 phút
# 1. Read color list
# Sử dụng lại list ở Phần 1, cho phép người dùng xem
# nội dung của một màu theo vị trí. Đếm thứ tự từ 1.
# a=list(("blue","red","green"))
# b =int(input("Item to delete:"))
# print(a[b])

# 2. Remove color
# Sử dụng list ở Phần 1, viết chương trình hỏi người
# dùng muốn xoá màu nào trong danh sách.
# - Nếu người dùng nhập số, thực hiện xoá theo vị trí.
# - Nếu người dùng nhập chữ, thực hiện xoá theo giá
# trị

#Phần 3. Thời gian: 15 phút
# 1. Search
# number in list
# Tạo một list chứa trên 5 số nguyên không cách đều, sau
# đó yêu cầu người dùng nhập vào một số.
# Thực hiện tìm kiếm số vừa nhập trong list vừa khởi tạo,
# trả lời câu hỏi: “Số này có trong list không, nếu có thì có
# đứng thứ mấy trong dãy?”. Đếm thứ tự từ 1.

# numbers = [5, 1, 8, 92, -1, 30]
# user_input = int(input("Enter a number: "))
# if user_input in numbers:
#     print("Yes, this number is on the list.")
#     rank = numbers.index(user_input) 
#     print(f"It is ranked {rank} in the sequence.")
# else:
#     print("No, this number is not on the list.")

# 2. Sum number in list
# Tạo 1 list chứa trên 5 số không cách đều. Tính tổng dãy
# này và in ra kết quả.
# numbers = [5, 1, 8, 92, -1, 30]
# def totalNums(x):
#     sum = 0
#     for i in x:
#         sum += i
#     return sum
# print(totalNums(numbers))   

# 3. Sum number in list (2)
# Thực hiện lại bài trên với danh sách các số nhập từ
# người dùng. Người dùng nhập 0 để kết thúc.


# Phần 4. Thời gian: 10 phút
# 1. Even filter Tạo một list chứa trên 5 số không cách đều. Lọc ra tất
# cả những số chẵn trong dãy này và in ra màn hình.
# numbers = [5, 1, 8, 92, 7, 30]
# odd_numbers = [num for num in numbers if num % 2 != 0]
# print("List of odd numbers:")
# print(odd_numbers)

# 2. Even filter (2)
# Thực hiện lại bài trên với danh sách các số nhập từ
# người dùng. Người dùng nhập 0 để kết thúc.
# Initialize an empty list to store the numbers
# numbers = []

# while True:
#     num = int(input("Enter a number (0 to end): "))
#     if num == 0:
#         break
#     numbers.append(num)
# odd_numbers = [num for num in numbers if num % 2 != 0]
# print("List of odd numbers:")
# print(odd_numbers)

# Phần 5. Thời gian: 15 phút
# 1. Init list of district names and population
# Cho thông tin về diện tích và dân số các quận của một
# thành phố như bảng.
# Quận Diện tích (km2) Dân số
# BĐ 9.224 247100
# BTL 43.35 333300
# CG 12.04 266800
# ĐĐ 9.96 420900
# HBT 10.09 318000
# Tạo 2 list chứa dữ liệu theo thứ tự từ trên xuống dưới:
# - List đầu tiên chứa tên các quận trong bảng
# - List thứ hai chứa dân số các quận trong bảng
# quan=["BĐ","BTL","CG","ĐĐ","HBT"]
# danso=[247100,333300,266800,420900,318000]

# 2. Search max &
# min population
# Trong list dân số của các quận trong bảng, tìm số thứ tự
# của quận có dân số cao nhất và quận có dân số thấp nhất.
# Đếm thứ tự từ 0

# Phần 7. Thời gian: 10 phút
# 1. Init high
# score list
# Tạo một list chứa các số nguyên đại diện cho điểm cao
# (high scores) của người chơi. Ví dụ: 78, 56, 67
# high_scores= [78, 56, 67]
# 2. Print high
# score list In ra màn hình danh sách điểm cao.
# high_scores= [78, 56, 67]
# x=0
# while  x<len(high_scores):
#     print(high_scores[x])
#     x+=1

# 3. New high
# score
# Viết chương trình thêm điểm mới của người chơi.
# high_scores= [78, 56, 67]
# new_high_scores= int(input("scores"))
# high_scores.append(new_high_scores)
# x=0
# while  x<len(high_scores):
#     print(high_scores[x])
#     x+=1


# Phần 8. Thời gian: 20 phút
# 1. Sort high score
# Thực hiện lại Bài 3 ở Phần 7 với các điểm được sắp xếp
# từ cao đến thấp.
# high_scores= [78, 56, 67]
# high_scores.sort(reverse=True)
# x=0
# while  x<len(high_scores):
#     print(high_scores[x])
#     x+=1
# 2. Sort and
# select 5 highest
# scores
# Thực hiện lại Bài 3 ở Phần 7 với các điểm từ cao đến thấp
# và chỉ hiện 5 điểm cao nhất

# high_scores= [78, 56, 67]
# new_high_scores= int(input("scores"))
# high_scores.append(new_high_scores)
# high_scores.sort(reverse=True)
# print(high_scores)
# high_scores.sort(reverse=True)
# x=0
# while  x<len(high_scores):
#     print(high_scores[x])
#     x+=1

