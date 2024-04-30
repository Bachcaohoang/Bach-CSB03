'''
a = int(input('NHAP SO:'))
if a>0: print('a la so duong')
elif a<0:print('a la so am')
else: print('a=0')
'''
'''
a  = int(input('NHAP SO:'))
if a%2 ==0:print('a la so chan')#%chia lay du
else:print('a la so le')

'''
""" 
i = int(input('nhap so:'))
while i < 6:
  print(i)
  i += 1
   """

'''
i= 1
g= 0
while i <= 100:
  g+=i
  i+= 1 
print(g)
'''
""" 
for x in range(1, 21):
    print(x)
  """
#B1  Viết chương trình tìm số lớn hơn trong 3 số nhập từ người dùng

""" a = int(input('nhap so1:'))
b = int(input('nhap so2:'))
c = int(input('nhap so3:'))
if a>b and a>c:print('a la so lon nhat')
elif b>a and b>c:print('b la so lon nhat')
else:
    print('c la so lon nhat') """
#cach2
""" a = int(input('nhap so1:'))
b = int(input('nhap so2:'))
c = int(input('nhap so3:'))
max =a
number =[a,b,c]
for i in number:
   if i >max:
    max =i
    print(max)
 """
#B2 Viết chương trình xác định một năm có phải năm nhuận không 
#(Năm nhuận là năm chia hết cho 4. Trong trường hợp năm chia hết cho 100 thì phải chia hết cho 400)
'''
nam = int(input('nhập năm'))
if (nam%100 == 0 & nam % 400==0) or ():
    print('nam này là năm nhuận')

else:
    print('năm này không phải là năm nhuận')
'''
#B3 Dùng vòng lặp in ra các dãy số sau (mỗi dãy số là 1 vòng lặp):
     #- 0 1 2 3 4 5 6
     #- 100 101 102 103 104 105
     #- 9 8 7 6 5 4 3 2
'''
for x in range(0, 7):
 print(x)
for y in range(100,106):
 print(y)
for z in range(9,1,-1):
 print(z)

 '''
#B4 . In ra các  số chia hết cho 3 từ 0 đến 20, mỗi số một dòng
'''
for i in range(0,20):
 if i%3==0: print(i)
'''
#B5. Tính số chữ số của một số nguyên do người dùng nhập vào

