#Bai1
# Cho một đơn hàng đặt mua 5 máy ASUS. Tính tổng giá trị đơn hàng
# shop={
# "HP": 600,
# "DELL": 650,
# "MACBOOK": 1200,
# "ASUS": 400
# }
# x = shop["ASUS"]
# y = x*5
# print('Total price:',y)
#   Bai2
# Lặp lại Bài 1, Phần 4 với hãng máy và số lượng nhập từ người dùng
# a =str(input("Input a brand:"))
# b = int(input("Input amount:"))
# x = shop[a]
# y = x*b
# print('Total price:',y)
#Bai3
# Kết hợp với dữ liệu về số lượng máy thuộc từng hãng ở Bài 1, Phần 1., thực
# hiện xuất kho bằng cách trừ đi số máy của hãng có trong kho với số lượng
# máy trong đơn hàng.
# Chương trình bao gồm các chức năng:
# - Nhận thông tin xuất kho gồm hãng máy và số lượng nhập từ người dùng.
# - In ra tổng giá trị xuất kho.
# - Cập nhật số lượng máy trong kho.
# - In ra số màn hình số lượng từng loại máy trong kho sau khi cập nhật.
# shop1={
# "HP": 20,
# "DELL": 50,
# "MACBOOK": 12,
# "ASUS": 30
# }
# shop={
# "HP": 600,
# "DELL": 650,
# "MACBOOK": 1200,
# "ASUS": 400
# }
# a =str(input("Input a brand:"))
# b = int(input("Input amount:"))
# x = shop[a]
# y = x*b
# print('Total price:',y)
# shop1[a] -=b
# for x,y in shop1.items():
#     print(x,y)