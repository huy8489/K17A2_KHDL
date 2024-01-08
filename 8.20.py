import math
def solve_equation(n):
    x = int(input("nhập x:"))
    while True:
        calculated = 1 + (x**2) / n
        real_value = math.exp(x)
        if abs(calculated - real_value) < 1e-4:
            break  
        x += 0.1  
    print(f"Giá trị của công thức với độ chính xác 10^-4: {calculated}")