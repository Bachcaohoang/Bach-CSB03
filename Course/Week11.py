# f = open("csb03,txt","a")
# f.write('bla bla')
# f.close()

# f = open("csb03,txt","r")
# print(f.readline())

import os
# # os.remove('d:\Lập trình\Lập bài tập\THUCHANH\Bach-CSB03\Course/csb03.txt')
# if os.path.exists("d:\Lập trình\Lập bài tập\THUCHANH\Bach-CSB03\Course/csb03.txt"):
#   print('exist')
# else:
#   print("The file does not exist")
#os.remove("d:\Lập trình\Lập bài tập\THUCHANH\Bach-CSB03\Course/csb03.txt")

# with open("d:\Lập trình\Lập bài tập\THUCHANH\Bach-CSB03\Course/csb03.txt",'r') as f:#khi hoàn thành xong nó sẽ tự đóng file
#     print(f.read())
# Bài 1. Tạo một file tên names.txt với nội dung sau:
# - Nikki Roysden   
# - Mervin Friedland
# - Aron Wilkins
# Sau đó viết chương trình đọc và in ra màn hình dữ liệu từ file names.txt với định dạng như bên dưới:
# List of names:
# - Nikki Roysden   
# - Mervin Friedland
# - Aron Wilkins

# f = open("d:\Lập trình\Lập bài tập\THUCHANH\Bach-CSB03\Course/names.txt", "r")
# print('List of names:\n',f.read())

# Bài 2. Yêu cầu người dùng nhập vào tên một text file.
# Nếu file tồn tại, in ra màn hình nội dung file.
# Ngược lại, in ra màn hình File not found.
a = input("nhâp tên file:")
import os
os.remove(f"d:\Lập trình\Lập bài tập\THUCHANH\Bach-CSB03\Course/{a}")
if os.path.exists(f"d:\Lập trình\Lập bài tập\THUCHANH\Bach-CSB03\Course/{a}"):
    print('exist')
else:
    print("The file does not exist")

# Bài 3. Tạo một file theo cú pháp tên_bạn.txt. Ghi nội dung của file bằng câu lệnh write với dung: 
# Họ tên học sinh
# Lớp đang học
# Trường
# Đọc file sau khi ghi xong
'''
f = open("d:\Lập trình\Lập bài tập\THUCHANH\Bach-CSB03\Course/tên_bạn.txt","w")
f.write("Họ tên học sinhg")
f.close()

f = open("d:\Lập trình\Lập bài tập\THUCHANH\Bach-CSB03\Course/tên_bạn.txt", "r")
print(f.read())
'''
