print("Chương trình tính tổng các số nguyên")
s = 0
while True:
    n = int(input("Nhập một số nguyên (kết thúc là số 0): "))
    if n == 0:
        break
    s += n
print("Tổng các số nguyên đã nhập là:", s)
