n=int(input("Nhập một số nguyên : "))
A = sum(i for i in range(n + 1) if i % 2 != 0)
print("A =", A)
B = sum(i for i in range(n + 1) if i % 2 == 0)
print("B =", B)
C = 1
for i in range(1, n + 1):
    C *= i
print("C =", C)
D = 1
for i in range(1, n + 1):
    if i % 3 == 0:
        D *= i
print("D =", D)
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
E = sum(i for i in range(2, n + 1) if is_prime(i))
print("E =", E)
total = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total -= 1 / i
    else: 
        total += 1 / i
print("F =", total)