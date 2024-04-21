#Phần 1.
#1.Full name
""" a = input('First name:')
b = input("Last name:")
print("" Your full name is "",a,b) """
#2. Capitalized name
""" a = input('Your input:')
b = a.upper()
print( "Capitalized:",b)
 """
#3.  Square number
""" a = int(input('Input a number:'))
b = float(a*a)
print('Squared input:',b)
 """
#4.  Turtle with custom radius
""" a = int(input("Input circle's radius:") )
import turtle 
t = turtle.Turtle() 
r = a
t.circle(r) 
mainloop() """
#Phần 2.
#1.  3 to 12 sequence
""" for x in range(3, 21):
 print(x)
 """
#2. 0 to n sequence
""" i = int(input('nhap so:'))
while i >-1:
  print(i)
  i -= 1 """
#3.  0 to n odd sequence
""" a = int(input("Nhap vao 1 so: "))
for b in range(1,a+1,2):
    print(b) """
#4.Polygon with custom edge number
""" import turtle 
size = int(input('nhap canh')) 
sides = int(input('nhap canh'))
for_in range(size):
 pen.forward
 pen.right(360/size) """


#Phần 3.
#1.  Larger than 13
""" i = int(input('nhap so:'))
if i<13: print("This number is not larger than 13") """
#2.Even check
""" a = int(input('Nhập vào số nguyên: '))
if a % 2  ==0:
    print(a,'là số chẵn')
else:
    print(a, 'là số lẻ') """
#3.  Days of month
""" i = int(input('nhap so:'))
if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:print("Tháng có 31 ngày")
elif i ==4 or  i==6 or i==9 or i==11:print("tháng có 30 ngày")
else:
    print("tháng có 29 or 28 ngày") """
#Phần 4.
#1.  Registration simulation
""" a = str(input('Username:'))
b = int(input('Password:'))
c = input('Email:')
print("Registered successfully.") """
#2.Registration simulation v2
""" a = str(input('Username:'))
b = int(input('Password:'))
c= int(input('Repeat password:')) 
while b!=c:
    c = int(input("Passwords not match. Please input again. "))
    if b==c:
        continue 
d= input('Email:')
print("Registered successfully.") """
#3.Registration simulation v3
""" a = str(input('Username:'))
b = (input('Password:'))
while len(b)<8:
  b= input('Độ dài tối thiểu của mật khẩu phải lớn hơn 8 ký tự')
c = input("repeat pass ")
while b!=c:
    c = (input("Invalid password. Please input again. ")) 
d= input('Email:')
print("Registered successfully.")  """


""" email_address = input("What is your email address? ")
while "@" not in email_address:
    email_address = input("Your email address must have '@' in it\nPlease write your email address again: ")
    if len(email_address) <= 6 :
        email_address = input("Your email address is too short\nPlease write your email address again: ")
    if "." not in email_address:
        email_address = input("Your email address must have '.' in it\nPlease write your email address again: ")
while "." not in email_address:
    email_address = input("Your email address must have '.' in it\nPlease write your email address again: ")
    if len(email_address) <= 6 :
        email_address = input("Your email address is too short\nPlease write your email address again: ")
    if "@" not in email_address:
        email_address = input("Your email address must have '@' in it\nPlease write your email address again: ") """

