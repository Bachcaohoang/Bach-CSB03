# def total(a,b):
#   return a+b
# print(total(1,2))
# file example_module.py

# def sum (a, b):
#     sum = a + b chẵn và in "Đâ
#     print(f"Tong cua {a} va {b} la: {sum}")

# 1. Viết Function tìm số lớn hơn trong 2 số 
# 2. Định nghĩa hàm có thể chấp nhận input là số nguyên 
# và in "Đây là một số chẵn" nếu nó là một số lẻ" nếu là số lẻ.
# 3. Viết function kiểm tra năm đó có phải năm nhuận hay không 
# 4. Viết function tính tổng một array nhập từ bàn phím. 
# Nếu trong array tồn tại phần tử không phải là số, thì bỏ qua phần tử đó 
# 5. Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau bởi dấu phẩy 
# và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.
#5

# input_string = input("Enter a string of words separated by commas: ")
# def sort_words(input_string):
#     words_list = input_string.split(',')
#     words_list = [word.strip() for word in words_list]
#     words_list.sort()
#     sorted_string = ', '.join(words_list)
#     return sorted_string

# sorted_string = sort_words(input_string)
# print(sorted_string)

#1
# def number(a, b):
#     return max( a,b)
# a = float(input("Nhap so a :"))
# b = float(input("Nhap so b :"))
# so_lon_hon = number(a,b)
# print(f"Số lớn hơn trong hai số là: {so_lon_hon}")

#3
# def la_nam_nhuan(nam):
#     if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
#         return True
#     else:
#         return False

# nam = int(input("Nhập 1 năm: "))
# if la_nam_nhuan(nam):
#     print(f"{nam} là năm nhuận.")
# else:
#     print(f"{nam} không phải là năm nhuận.")
