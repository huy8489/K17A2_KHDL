x=int(input("Nhập năm: "))
if (x % 4 == 0 and x % 100 != 0) or (x% 400 == 0):
        print("Năm đó là năm nhuận.")
else:
        print("Năm đó không phải là năm nhuận.")

