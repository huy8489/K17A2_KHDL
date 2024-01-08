x = int(input("Nhập một số nguyên dương: "))
def so_nguyen_to(n):
    if n <= 1:
        so_nguyen_to = False
    else:
        so_nguyen_to = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                prime = False
                break
if so_nguyen_to(x):
    print(f"{x} là số nguyên tố")
else:
    print(f"{x} không phải là số nguyên tố")