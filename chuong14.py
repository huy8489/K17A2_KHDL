# câu 1
try:
    a = int(input("Nhập độ dài cạnh a: "))
    b = int(input("Nhập độ dài cạnh b: "))
    c = int(input("Nhập độ dài cạnh c: "))
    if  (a <= 0 and b <= 0 and c <= 0):
        raise ValueError("Các cạnh tam giác phải là số dương")
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("Không phải là tam giác")
    print("Các cạnh của tam giác là: a = ", a, ", b = ", b, ", c = ", c)
except ValueError as ex:
    print(ex)


#câu 2
lst=[]
while True:
    n = input("Nhập số nguyên dương: ")
    try:
        n = int(n)
    except ValueError:
        print("Lỗi nhập số ")
        continue
    if n < 0:
        raise ValueError("Lỗi số âm ")
    if n == 0:
        break
    if len(lst) >= 4 and n == lst[-3]:
        raise ValueError("Lỗi nhập lặp lại ")
    if len(lst) >= 5 and n % 2 == 0:
        raise ValueError("Lỗi nhập số chẵn")
    lst.append(n)
print("Danh sách các số :", lst)