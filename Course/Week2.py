#a = 'hello'
#b= 'hi'
#print(a+b) dinh nhau
#print(a,b) cach nhau
#print(a[1]) vi tri so 1
#print(a[1:4])  1<=x<4
#a =16
#print(f"bach {a} hai")
#1
""" 
txt = input("Hello World")
print(txt [::-1])
 """
#: ":"vi tri dau den cuoi "-" bắt đầu cắt
#3
""" 
y= input('Nhapten')
x = y.strip()
print("HI",x,'bye')
 """
#2
""" 
a = input('Ten')
b = input('so lan')
c= a.count(b)
print(c)
 """
""" 
a = 20//5*2
print(a)
"""
#từ trái sang phải
#b1
'''
a= int(input('nha so:'))
b= int(input('nha so:'))
x= (a+b)
y= (a-b)
z= (a/b)
v=(a*b)
print('CỘNG',int(x),float(x),'trừ',int(y),float(y),"chia", int(z),float(z),"Nhan",int(x),float(x) )
'''

#b2
'''
y = int(input(""))
x = float(y)
print(y)
'''
#b3
'''
 c = float(input(""))
d = int(c)
print(d)
'''
#b4
'''
w = float(input("Nhap chieu rong: "))
l = float(input("Nhap chieu dai: "))

area = w * l
circumference = (w + l) * 2

print("Dien tich chu nhat: ", float(area), int(area))
print("Chu vi: ", float(circumference), int(circumference))
'''
'''
meal = "fruit"

money = 0

if (meal == "fruit" or meal == "sandwich") and money >= 2:
    print("Lunch being delivered")
else:
    print("Can't deliver lunch")
    '''
'''
import calendar
yy=2022
mm=12
print(calendar.month(yy,mm))
'''

#capitalize(): Chuyển đổi ký tự đầu tiên của chuỗi thành chữ hoa.
#casefold(): Chuyển đổi chuỗi thành dạng không phân biệt chữ hoa chữ thường.
##upper(): Chuyển đổi tất cả các ký tự trong chuỗi thành chữ hoa.
#lower(): Chuyển đổi tất cả các ký tự trong chuỗi thành chữ thường.
#swapcase(): Chuyển đổi chữ hoa thành chữ thường và ngược lại.
#strip(): Loại bỏ các khoảng trắng ở đầu và cuối chuỗi.
#lstrip(): Loại bỏ các khoảng trắng ở đầu chuỗi.
#rstrip(): Loại bỏ các khoảng trắng ở cuối chuỗi.
#count(substring): Đếm số lần xuất hiện của một chuỗi con trong chuỗi.
#find(substring): Trả về chỉ mục đầu tiên của chuỗi con trong chuỗi. Nếu không tìm thấy, trả về -1.
#replace(old, new): Thay thế tất cả các chuỗi con old bằng chuỗi con new.
#split(separator): Tách chuỗi thành danh sách các phần bằng cách sử dụng một chuỗi phân cách.
#join(iterable): Nối các phần tử của một iterable thành một chuỗi, phân cách bằng chuỗi gọi phương thức này.
#startswith(prefix): Kiểm tra xem chuỗi có bắt đầu bằng prefix hay không.
#endswith(suffix): Kiểm tra xem chuỗi có kết thúc bằng suffix hay không.
#isalpha(): Kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ cái không.
#isdigit(): Kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ số không.
#isspace(): Kiểm tra xem chuỗi có chứa chỉ khoảng trắng không.
#islower(): Kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ thường không.
#isupper(): Kiểm tra xem tất cả các ký tự trong chuỗi có phải là chữ hoa không.
