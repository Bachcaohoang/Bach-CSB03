#BAI1
# Sử dụng dữ liệu về số lượng máy ở Bài 1, Phần 1 và giá từng hãng ở Bài 1,
# Phần 3, tính tổng giá trị của từng hãng trong kho.
shop1={
"HP": 20,
"DELL": 50,
"MACBOOK": 12, 
"ASUS": 30 
}
shop={
"HP": 600,
"DELL": 650,
"MACBOOK": 1200,
"ASUS": 400
}
total_value = {
    "HP": shop1["HP"] * shop["HP"],
    "DELL": shop1["DELL"] * shop["DELL"],
    "MACBOOK": shop1["MACBOOK"] * shop["MACBOOK"],
    "ASUS": shop1["ASUS"] * shop["ASUS"]
}

print("Total value of each firm in the warehouse:")
for x, y in total_value.items():
    print(x,y)
# #Bai2
# Sử dụng dữ liệu như trên, tính tổng giá trị của toàn bộ máy trong kho.
total = sum(total_value.values())
print("Total value of available items:", total)