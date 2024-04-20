#Bai1
""" a = int(input('Nhập vào số nguyên: '))
if a % 2  ==0:
    print(a,'là số chẵn')
else:
    print(a, 'là số lẻ')
     """
#Bai2
""" number = float(input('Nhập vào số thực: '))
if number % 1 == 0:
    print('la so nguyen')
else:
    print('la so thuc') """
#Bai3
""" letter = input('Nhập vào số thực: ')
if letter.isdigit():
    print('la chu')
else:
    print('la so') """
#Bai4
""" n = int(input('nhap vao so nguyen: '))
if n % 3 == 0 and n % 5 == 0:
    print(n,'is divisible by 3 and 5')
elif n % 3 == 0 and n%5!=0:
    print(n,'is divisible by 3')
elif n % 3 != 0 and n % 5 ==0:
    print(n,'is divisible by 5')
else:
    print(n,'is not divisible by 3 or 5') """
#Bai5
""" username = 'admin'
password = '12345'
inuser = input('Username: ')
inpass = input('Password: ')
if inuser == username and inpass==password:
    print('nhap dung')
else:
    print('nhap  sai') """
#Bai6
""" a = float(input('canh 1: '))
b = float(input('canh 2: '))
c = float(input('canh 3: '))
if  a < 0 or b<0 or c<0:
    print('vui lòng nhập số dương')
elif a+b>c:
    print('day la canh cua tam giac')    
else:
    print('k phai la canh cua tam giac') """
#Bai7
""" a = float(input('Nhap vao so thuc 1: '))
b = float(input('Nhap vao so thuc 2: '))
c = float(input('Nhap vao so thuc 3: '))

mang = [a,b,c]
if a + b > c and a + c > b and b + c > a:
    if a==b==c:
        print('la tam giac can')
        from turtle import *
        pen()
        backward(a)
        left(60)
        forward(a)
        left(60)
        backward(a)
        right(60)
        mainloop()
    elif a*a+b*b == c*c or a*a+c*c == b*b or c*c+b*b == a*a:
        print('la tam giac vuong')
    else:
        print('la tam giac thuong')
else:
    print('khong phai la tam giac') """
#Bai8
""" for i in range(21):
    if i % 3 ==0:
        print(i) """
#Bai9
""" try: 
    number = int(input('Nhap vao so nguyen: '))
    print(len(str(number)))
except ValueError:
    print("Phải nhập số nguyen") """