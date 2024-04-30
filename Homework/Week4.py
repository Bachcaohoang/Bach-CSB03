# BAI1
# a =int(input("nhap:"))
# for i in range(1,a+1):
#     print(""*(a-1)+"#"*i)
# BAI2
# number = float(input("input a number: "))
# while number <= 0:
#     number = float(input("input a number: "))
# print('Input a positive number:',number,'\nthank you')
# BAI3
# n = int(input('Input a number: '))
# giaithua = 1
# if n >0:
#     for i in range(1,n+1):
#         giaithua = giaithua*i
#         i+=1
#     print(n,'!=',giaithua)
# elif n == 0:
#     print('0!=1')
# else:
#     print('invalid')
# BAI4
# n = int(input("Input number: "))
# if n < 1:
#     print("Invalid input")
# else:
#     sum_digits = 0
#     while n > 0:
#         sum_digits += n % 10
#         n //= 10
#     print(f"Sum of digits of {n} = {sum_digits}")
# BAI5
# count = 0
# num = 1000
# while count < 10:
#     if sum(int(digit) for digit in str(num)) == 9:
#         print(num)
#         count += 1
#     num += 1