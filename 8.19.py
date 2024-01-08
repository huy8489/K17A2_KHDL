numbers = input("Nhập các số cách nhau bằng dấu cách: ")
number_list = numbers.split() 
number_list = [int(num) for num in number_list]
odd_numbers = [num for num in number_list if num % 2 != 0][::-1]
for odd_num in odd_numbers:
 print(odd_num, end=" ")