#13.1
with open('HumptyDumpty.txt', 'w') as file:
    file.write("Humpty dumpty saton a wall,\n")
    file.write("humpty dumpty had a great fall.\n")
    file.write("All the king's horses and all the king's men\n")
    file.write("couldn't put Humpty together again.\n")           
print("Tập tin đã được tạo và ghi thành công.")
try:
    with open('HumptyDumpty.txt','r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Tập tin không tồn tại.")
except Exception as e:
    print("Có lỗi xảy ra: ")


#13.2
try:
    with open('HumptyDumpty.txt', 'r') as file:
        content = file.read()
        so_ky_tu = len(content)
        so_dong = content.count('\n') + 1 
        print(f"Tập tin có {so_ky_tu} ký tự.")
        print(f"Tập tin có {so_dong} dòng.")
except FileNotFoundError:
    print("Tập tin không tồn tại.")
except Exception as e:
    print("Có lỗi xảy ra: ")   


#13.3
def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f'Đã ghi nội dung vào tập tin {file_name}')
        read_and_print_file(file_name)

    except Exception as e:
        print(f'Lỗi: {e}')
def read_and_print_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            print(f'Nội dung của tập tin {file_name} sau khi ghi:')
            print(file_content)
    except FileNotFoundError:
        print(f'Tập tin {file_name} không tồn tại.')

def main():
    file_name = input('Nhập tên tập tin (.txt): ')
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    content = input('Nhập nội dung: ')

    try:
        with open(file_name, 'r') as file:
            old_content = file.read()
            if old_content:
                write_to_file(file_name, content)
            else:
                write_to_file(file_name, content)

    except FileNotFoundError:
        write_to_file(file_name, content)
if __name__ == "__main__":
    main()     


#13.4
def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f'Đã ghi nội dung vào tập tin {file_name}')
        read_and_print_file(file_name)
    except Exception as e:
        print(f'Lỗi: {e}')

def read_and_print_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            print(f'Nội dung của tập tin {file_name} sau khi ghi:')
            print(file_content)
    except FileNotFoundError:
        print(f'Tập tin {file_name} không tồn tại.')

def main():
    file_name = input('Nhập tên tập tin (.txt): ')
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    content = input('Nhập nội dung: ')

    try:
        with open(file_name, 'r') as file:
            old_content = file.read()
            if old_content:
                write_to_file(file_name, content)
            else:
                write_to_file(file_name, content)

    except FileNotFoundError:
        write_to_file(file_name, content)

if __name__ == "__main__":
    main()
def main():
    while True:
        choice = int(input("Người dùng có muốn tiếp tục ghi nữa hay không? (1 để tiếp tục, 0 để dừng): "))
        
        if choice == 1:
            print("Đang tiếp tục ghi...")
        elif choice == 0:
            print("Người dùng đã chọn dừng. Kết thúc chương trình.")
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()

#13.5
import csv

def write_csv_file(file_name, content):
    try:
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for row in content:
                writer.writerow(row)
            
            print(f"Đã ghi nội dung vào tập tin '{file_name}'.")

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
    file_name = input("Nhập tên tập tin CSV cần tạo và ghi nội dung(cuối file .csv): ")

    content = []
    while True:
        row = input("Nhập nội dung cho dòng (nhập '0' để kết thúc): ")
        if row.lower() == '0':
            break
        content.append(row.split(','))

    write_csv_file(file_name, content)

if __name__ == "__main__":
    main()



#13.6
import csv

def read_csv_file(file_name):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)             
    except FileNotFoundError:
        print(f"Tập tin '{file_name}' không tồn tại.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
def write_phone_numbers(file_name, phone_numbers):
    try:
        with open(file_name, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            for phone_number, person_name in phone_numbers:
                writer.writerow([person_name, phone_number])
            print(f"Đã ghi danh sách số điện thoại vào cuối tập tin '{file_name}'.")   
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
def main():
    file_name = input("Nhập tên tập tin CSV cần ghi số điện thoại và tên vào: ")

    phone_numbers = []
    while True:
        person_name = input("Nhập tên người (nhập 'done' để kết thúc): ")
        if person_name.lower() == 'done':
            break
        phone_number = input("Nhập số điện thoại: ")
        phone_numbers.append((phone_number, person_name))
    write_phone_numbers(file_name, phone_numbers)
    print("\nNội dung tập tin sau khi ghi:")
    read_csv_file(file_name)

if __name__ == "__main__":
    main()


  
      