bang_gia = {
    "Bậc 1": {"kwh": 0, "đơn giá": 1678},
    "Bậc 2": {"kwh": 51, "đơn giá": 1734},
    "Bậc 3": {"kwh": 101, "đơn giá": 2014},
    "Bậc 4": {"kwh": 201, "đơn giá": 2536},
    "Bậc 5": {"kwh": 301, "đơn giá": 2834},
    "Bậc 6": {"kwh": 401, "đơn giá": 2927}
}
def hoa_don_dien(kwh):
    tong_gia = 0
    for i in range(bang_gia):
        if kwh <=bang_gia[i]["kwh"]:
            tong_gia += kwh * bang_gia[i]["đơn giá"]
            break
        else:
            kwh -= bang_gia[i]["kwh"]
            tong_gia += bang_gia[i]["kwh"] * bang_gia[i]["đơn giá"]
    return tong_gia
kwh = float(input("Nhập số Kwh tiêu thụ: "))
tong_gia = hoa_don_dien(kwh)
print("Tổng tiền điện phải trả là:", tong_gia)