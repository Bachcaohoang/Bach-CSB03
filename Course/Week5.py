"""
 #hs =['Bach','khoa','dat']
# or
student= list(('+Bach','khoa','dat','jieu','hoa','khoi'))
print(student[1])

student[1] ='bachbe'
print(student[1])

student.append('hoa')# cho vi tri cuoi
print(student)

student.insert(3,'khoa')
print(student)

mynumber = [1,2,34,4]
student.extend(mynumber)#them ket hop 2 chuoi
print(student)

student.remove('khoa')#xoa bien
print(student)

student.pop(0)#xoa vi tri
print(student)

del student[2]#xoa vi tri so2
print(student)
#del student   xoa het
#or
#student.clear()

#for i in student:print(i)

x=0
while  x<len(student):
    print(student[x])
    x+=1

total = student + mynumber# cong them list
print(total)



#tuple (ko the sua hoac xoa but co the neu cho no ve list )
tuples= ('+Bach','khoa','dat','jieu')
#or
tuplesba= tuple((1,2,3,4,5,))
print (tuples)
tuplesba= list(tuples)
print(tuplesba)
 """
#VANDUNG
#B1  
# Hỏi người dùng món ăn mà người dùng muốn. Cho món ăn vào list. In ra các món ăn trong list, mỗi món một dòng
# Hỏi người dùng muốn bỏ món ăn nào, in món đó ra và loại bỏ món khỏi list
# A = str(input("Hỏi người dùng món ăn mà người dùng muốn?"))
# B = list(("XOI","COM","NUI","BUN"))
# B.append(A)
# x=0
# while x<len(B):
#     print(B[x])
#     x+=1
# C =str(input('Hỏi người dùng muốn bỏ món ăn nào'))
# B.remove(C)
# y=0
# while y<len(B):
#     print(B[y])
#     y+=1  

#B2 Tính tổng các số trong một list (List nhập từ bàn phím)
# NumList=[]       
# evenSum=0     
# oddSum=0        
# Number=int(input("Please enter the total number of list elements: "))
# for i in range(1, Number+1):
#      value=int(input("Please enter the value of %d Eleements: " %i))
#      NumList.append(value)
# def total(x):
#      sum =0
# for i in x:
#     sum +=i
# print(total(Number))
nums = [1, 2, 3, 4, 5, 6]
def totalNums(x):
    sum = 0
    for i in x:
        sum += i
    return sum
print(totalNums(nums))                                                                                    