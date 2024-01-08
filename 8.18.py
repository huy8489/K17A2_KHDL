def so_hoan_hao(x):
    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong += i
    return tong == x
a= int(input("Nhập số nguyên dương x: "))
if so_hoan_hao:
    print(f"{a} là số hoàn hảo")
else:
    print(f"{a} không phải là số hoàn hảo")






