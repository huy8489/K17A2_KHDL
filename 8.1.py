a, b, c, d = int(input("Nhập a: ")), int(input("Nhập b: ")), int(input("Nhập c: ")), int(input("Nhập d: "))
a_max = a
if b > a_max:
    a_max = b
if c > a_max:
    a_max = c
if d > a_max:
    a_max = d
a_min = a
if b < a_min:
    a_min = b
if c < a_min:
    a_min = c
if d < a_min:
    a_min = d
print("Giá trị lớn nhất:", a_max)
print("Giá trị nhỏ nhất:", a_min)