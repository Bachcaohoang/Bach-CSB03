#Bai1:
# Sử dụng dữ liệu từ Bài 1, Phần 1. Không thay đổi khai báo, 
#thêm 1 loại máy mới là TOSHIBA, có số lượng 10 vào dictionary.
# In ra màn hình số lượng từng loại máy trong kho.
# shop={
# "HP": 20,
# "DELL": 50,
# "MACBOOK": 12,
# "ASUS": 30
# }
# shop["TOSHIBA"]=10
#for x,y in shop.items():
    #print(x,y)
#Bai2:
# Thực hiện lại Bài 1, Phần 2 với thông tin loại máy và số lượng được nhập bởi
# người dùng.
# shop={
# "HP": 20,
# "DELL": 50,
# "MACBOOK": 12,
# "ASUS": 30
# }
# a =str(input("Input a brand:"))
# b = int(input("Input amount:"))
# shop[a]=b
# for x,y in shop.items():
#     print(x,y)
#BAi3
# Sử dụng dữ liệu từ Bài 1, Phần 1. Không thay đổi khai báo, tăng số lượng
# máy DELL lên 60 và giảm số MACBOOK về 2.
# In ra màn hình số lượng từng loại máy trong kho
# shop={
# "HP": 20,
# "DELL": 50,
# "MACBOOK": 12,
# "ASUS": 30
# }
# shop["DELL"]+= 10
# shop["MACBOOK"] -=10
# for x,y in shop.items():
#     print(x,y)
#Bai4:
# Sử dụng dữ liệu từ Bài 1, Phần 1. Tính tổng số máy từ tất cả các hãng có
# trong kho.
# shop={
# "HP": 20,
# "DELL": 50,
# "MACBOOK": 12,
# "ASUS": 30
# }
# total_machines = sum(shop.values())
# print("Total number of machines in stock:", total_machines)