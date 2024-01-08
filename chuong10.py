#10.1
print(max(3,6,8))
print(min(4,248,6))
#10.2
print(abs(-7))
#10.3
x = int(input())
n = int(input())
print(pow((pow(x,2)+1,n)))
#10.4
x = int(input())
n = int(input())
print(pow((pow(x,2)+x+1),n)+pow((pow(x,2)-x+1),n))
#10.5
def zipcode(n):
     return len(str(n)) == 6
n = int(input())     
print(zipcode(n))
#10.6
a,b,c = int(input()),int(input()),int(input())
denta = b**2 - 4*a*c
if a == 0 or denta < 0 : print("vô nghiệm")
elif denta == 0 : print("phương trình có nghiệm kép là",-b/a)
else : print(" phương trình có 2 nghiệm x1,x2 lần lượt là",(-b + denta)/a,(-b - denta)/a)
#10.7
s=input("Nhập chuỗi s: ")
s_sub=input("Nhập chuỗi con s_sub: ")
s_find=input("Nhập chuỗi s_find: ")
s_replace=input("Nhập chuỗi thay thế s_replace: ")
print("Chuỗi s :",s)
print("Loại bỏ khoảng trắng ở đầu và cuối: ",s.strip())
print("Chuỗi s_find với kí tự đầu viết hoa: ",s_find.capitalize())
print("Số lần s_sub xuất hiện trong s :",s.count(s_sub,0,16))
print("Thay thế s_find bằng s_replace : ",s.replace(s_find,s_replace))

#10.8
from datetime import datetime

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

ngay_thang_nam = datetime(nam, thang, ngay).date()

print("Ngày tháng năm vừa nhập:", ngay_thang_nam.strftime("%d - %m - %Y"))

if ngay_thang_nam.year % 4 == 0 and (ngay_thang_nam.year % 100 != 0 or ngay_thang_nam.year % 400 == 0):
    print("Năm", ngay_thang_nam.year, "là năm nhuận")
else:
    print("Năm", ngay_thang_nam.year, "không là năm nhuận")

thu_trong_tuan = ngay_thang_nam.strftime("%A")
thu_trong_tuan_vn = {"Monday": "Thứ Hai", "Tuesday": "Thứ Ba", "Wednesday": "Thứ Tư", "Thursday": "Thứ Năm", "Friday": "Thứ Sáu", "Saturday": "Thứ Bảy", "Sunday": "Chủ Nhật"}

print(ngay_thang_nam.strftime("%d - %m - %Y"), "là", thu_trong_tuan_vn[thu_trong_tuan])

so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if ngay_thang_nam.year % 4 == 0 and (ngay_thang_nam.year % 100 != 0 or ngay_thang_nam.year % 400 == 0):
    so_ngay_trong_thang[1] = 29
print("Số ngày trong tháng", ngay_thang_nam.month, "là:", so_ngay_trong_thang[ngay_thang_nam.month - 1])