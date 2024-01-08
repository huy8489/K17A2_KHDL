# câu 1
def sign(n):
    return 1 if n > 0 else -1 if n < 0 else 0
n = float(input("Nhập số:"))
print(sign(n))

# câu 2
def can(year):
    can_list = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    c = (year + 6) % 10
    return can_list[c]
def chi(year):
    chi_list = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
    i = (year + 8)% 12
    return chi_list[i]

def get_lunar_year(year):
    return can(year) + " " + chi(year)
year = int(input("Nhập năm dương lịch: "))
print("Năm", year, "lịch âm là năm", get_lunar_year(year))

# câu 3
def BMI(c,b):
    bmi = c / (b ** 2)
    bmi = round(bmi, 2)
    print("Chỉ số BMI của bạn là:", bmi)
    if bmi < 18.5:
        print("Bạn nhẹ cân.")
    elif 18.5 <= bmi < 25:
        print("Bạn bình thường.")
    else:
        print("Bạn béo phì.")
can_nang = float(input("Nhập cân nặng của bạn (kg): "))
chieu_cao = float(input("Nhập chiều cao của bạn (m): "))
BMI(can_nang,chieu_cao)

#câu 4
def tinh_S(n, x):
    return (x**2 + 1)**n 
n = float(input("Nhập n:"))
x = float(input("Nhập x :"))
print("S =", tinh_S(x, n))

# câu 5
def tinh_A(n, x):
    return (x**2 + x + 1)**n + ( x**2 - x + 1)**n
n = float(input("Nhập n:"))
x = float(input("Nhập x:"))
print("A =", tinh_A(x, n))

# câu 6
def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    flag = False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            flag = True
            break
    if flag:
        return False
    else:
        return True
n = int(input("Nhập số:"))
print(kiem_tra_so_nguyen_to(n))
  
#câu 7
def phan_nguyen(a, b):
    return a // b
a = int(input("Nhập a :"))
b = int(input("Nhập b :"))
print("Phần nguyên là:",phan_nguyen(a, b))

#câu 8
def kiem_tra_so_hoan_hao(n):
    flag=True
    if n<0:
        return flag
    else:
        sum=0
        for i in range(1,n):
            if n%i==0:
                sum+=1
            if sum==n:
                flag=True
                return flag


n = int(input("Nhập n :"))
if(kiem_tra_so_hoan_hao(n)):
    print(n,"là số hoàn hảo")
else:
    print(n,"không là số hoàn hảo")


#câu 9
r,a,b = float(input("Nhập r:")),float(input("Nhập a:")),float(input("Nhập b:"))
dien_tich_tron = lambda r: 3.14 * r**2
chu_vi_tron = lambda r: 2 * 3.14 * r
dien_tich_hcn = lambda a, b: a * b
chu_vi_hcn = lambda a, b: 2 * (a + b)
print("Diện tích hình tròn:", dien_tich_tron(r))
print("Chu vi hình tròn:", chu_vi_tron(r))
print("Diện tích hình chữ nhật:", dien_tich_hcn(a, b))
print("Chu vi hình chữ nhật:", chu_vi_hcn(a, b))