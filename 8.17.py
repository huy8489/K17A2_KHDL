def uoc_chung_lon_nhat(a, b):
    while b:
        a, b = b, a % b
    return a
def boi_chung_lon_nhat(a, b):
    return abs(a * b) // uoc_chung_lon_nhat(a, b)
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
result = boi_chung_lon_nhat(a, b)
print(f"Bội chung lớn nhất của ({a}, {b}) là: {result}")