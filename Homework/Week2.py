#B1
""""
π = 3.1416
Radius=int(input("Nhập bán kính"))
Perimeter = (Radius*2)*π 
Area = (Radius^2)*π
print(Perimeter,Area)
"""
#B2
'''
import math
x= int(input('Nhập độ dài cạnh hình vuông:'))
Ly=  math.sqrt(x ** 2 + x ** 2)
print(Ly)
'''
#B3
'''
Name=input('Account name:')
Gmail=input('Domain name:')
Fullname= Name+Gmail
print('Full email:',Fullname)
'''
#B4
'''
day = input("Date in MM/DD/YYYY format: ")
print(day)
'''

#B5
'''
Money=float(input('Deposit:'))
Year =float(input('Year:'))
LAI=(Money*(105/100)**10)
print(LAI)
'''
#B6
'''
from turtle import*
forward(200)
left(90)  
pencolor('#de5246')  
forward(150)
left(125)
forward(125)
left(-70)
forward(125)
left(125)
forward(150)
penup()
goto(0,150)
pencolor('#000000')
pendown()
left(90)
forward(200)
mainloop()
'''
#B7
'''
from turtle import*
pencolor('#cf8f03') 
left(45)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
penup()
goto(50,0)
pendown()
pencolor('#0b2c3c') 
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
mainloop()
'''