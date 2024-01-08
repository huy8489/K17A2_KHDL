#bài 1.4
#yêu cầu 1 
a=(5-3)/2
print(a)
#yêu cầu 2
a=8-(3*2)-1-1
print(a)



# bài 1.5
so_luong = 100
don_gia = 5000
thanh_tien = so_luong * don_gia
print("Số lượng: ", so_luong)
print("Đơn giá: ", don_gia)
print("Thành tiền: ", thanh_tien)



# bài 1.6
alice_candies = 121
bob_candies = 77
carol_candies = 109
total_candies = alice_candies + bob_candies + carol_candies
candies_per_person = total_candies // 3
to_smash = total_candies % 3
print("Số lượng kẹo dư ra là:", to_smash)


# bài 1.7
doC=27
doF=9/5*doC+32
print(doC,"độ C=",doF,"độ F")


#bài 1.8
s1="Hello"
s2="Python"
s3="programming language"
do_dai_s1 = len(s1)
do_dai_s2 = len(s2)
do_dai_s3 = len(s3)
index = 2
s4 = s1[2:5]
s2_lap = s2 * 2
print("Chiều dài của chuỗi s1 là:", do_dai_s1)
print("Chiều dài của chuỗi s2 là:", do_dai_s2)
print("Chiều dài của chuỗi s3 là:", do_dai_s3)
print("Chuỗi s4 là:", s4)
print("Chuỗi s2 lặp lại 2 lần là:", s2_lap)


#bài 1.9
lai_suat = float(input("Nhập lãi suất năm (%): "))
tien_gui = float(input("Nhập số tiền gửi: "))
so_thang = int(input("Nhập số tháng gửi: "))
lai_suat_thang = lai_suat /100/ 12
tien_lai =(tien_gui * so_thang) * (lai_suat_thang)
tien_von_cong_lai=tien_lai+tien_gui
print("Tiền lãi:", tien_lai)
print("Tiền vốn cộng lãi:", tien_von_cong_lai)
