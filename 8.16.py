def uoc_chung_lon_nhat(a, b):
    while b:
     a, b = b, a % b
     return a
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
result = uoc_chung_lon_nhat(a, b)
print(f"Ước chung lớn nhất của ({a}, {b}) là: {result}")