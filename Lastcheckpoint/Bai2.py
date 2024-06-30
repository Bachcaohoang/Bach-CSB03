
a = float(input("Input  number: a: "))
b = float(input("Input  number: b: "))
c = float(input("Input  number: c: "))

delta = b**2 - 4*a*c

if delta > 0:
    root1 = (-b + delta**0.5) / (2*a)
    root2 = (-b - delta**0.5) / (2*a)
    print(f"The roots are {root1} and {root2}")
elif delta == 0:
    root = -b / (2*a)
    print(f"The root is {root}")
else:
    real_part = -b / (2*a)
    print(f"The roots are {real_part}  and {real_part}")