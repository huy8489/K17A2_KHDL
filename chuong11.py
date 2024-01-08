# BT 11.1
""" 
độ dài danh sách a là 3
độ dài danh sách b là 2
độ dài danh sách c là 0
độ dài danh sách d là 2
"""


# BT 11.2
teams = [['Steven', 'Neena', 'Lex', 'Alexander', 'Bruce'], ['David', 'Jack', 'Bill', 'Tom', 'Mike'], ['Alexander', 'Adam', 'Payam', 'Kevin', 'Sigal', 'Mike']]
print(teams[2][1])



# BT 11.3
List_of_animals =  ['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo'] 
n = input(" I want to find")
print("List of animals :  ['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo']")
print("Number of animals",len(List_of_animals))
if n in List_of_animals:
    print("There is ",n,"list of animals")
else:
    print("There isn't ",n,"list of animals")
  
#11.4
    mylist=[]
while True:
    val=int(input("Nhập giá trị : "))
    a=int(input("Tiếp tục nhập giá trị ? 1:Có,0:Không "))
    mylist.append(val)
    if a==0:
        x=int(input("Nhập giá trị cần tìm x:"))
        break
print('List:',mylist) 
print('Tổng các giá trị trong list:',sum(mylist))
print(x,'xuất hiện',mylist.count(x),'trong list')
if max(mylist)==x:
    print(x,'lớn hơn tất cả các số trong list')
else:
    print(x,'không lớn hơn tất cả các số trong list')
newlist=[int(i) for i in mylist if int(i)>x]
print('Các số lớn hơn',x,'trong list',newlist)


#  11.5
list=[]
x=int(input("Nhập giá trị:"))
list.append(x)
i=1
while i==1:
          y=int(input("Tiếp tục nhập giá trị? 1:Có, 0:Không"))
          if y==1:
                  x=int(input("Nhập giá trị:"))
                  list.append(x)
          elif y==0:
                  break
print("list:",list)
sum=0
for num in list:
        sum+=num
print("Tổng các giá trị trong list:",sum)
x=int(input("Nhập giá trị cần tìm:"))
find = x in list
if find=="True":
        print(x,"xuất hiện",list.count(x),"lần trong list")
for i in list:
        if i>x:
          print(x,"không lớn hơn tất cả các số trong list")
          break
new_list=[]
for i in list:
        if i>x:
               new_list.append(i)
print("Các số lớn hơn",x,"trong list:",new_list)   
# 11.6
chieu_cao=[74,74,72,72,73,69,69,71,76,71]
def doi(x):
    return x*0.0254
ccmoi = [doi(x) for x in chieu_cao]
print('Đổi inch sang m:',ccmoi)
print('In 3 chiều cao đầu tiên:',ccmoi[0:3])
print('In 3 chiều cao cuối cùng:',ccmoi[-3:])
print("Chiều cao max:",max(ccmoi))
print("Chiều cao min:",min(ccmoi))
print("Chiều cao trung bình:",sum(ccmoi)/len(ccmoi))
ccmoi.sort()
print('Chiều cao tăng dần:',ccmoi)
ccmoi.sort()
ccmoi.reverse()
print('Chiều cao giảm dần:',ccmoi)

# 11.8   
def has_lucky_number(nums):
  for num in nums:
    if num % 7 == 0:
      return True
  return False
nums = [2, 6, 7, 9]
print(has_lucky_number(nums))
 #11.9
arrivals=['Adela','Fleda','Owen','May','Mona','Gilbert','Ford']
def party_late(arrivals,name):
    if name==arrivals[-1]:
        return False
    elif name==arrivals[0]:
        return False
    elif name==arrivals[1]:
        return False
    elif name==arrivals[2]:
        return False
    elif name==arrivals[3]:
        return False
    else:
        return True
print(party_late(arrivals,name='Gilber'))
print(party_late(arrivals,name='Ford'))
print(party_late(arrivals,name='Mona'))
#11.10
def menu_is_boring(meals):
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
meals_1 = ['Redneck Ribs', 'Prawn Star', 'San Quentin Squid', 'Fist Full of Pizza', 'Honky Tonk Chicken']
meals_2 = ['Redneck Ribs', 'Prawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']
print(menu_is_boring(meals_1))
print(menu_is_boring(meals_2))
#11.11
a=['red','green','yellow','blue','black','white','pink','orange','red','blue']
print("Tuple :",a)
x=int(input('Nhập số từ 0 đến 9: '))
y=int(input('Nhập số từ -1 đến -9: '))
z=input('Nhập chuỗi cần tìm: ')
print("Tuple[",x,"] =",a[x])
print("Tuple[",y,"] =",a[y])
print(z,"xuất hiện trong tuple",a.count(z),"lần")
#11.12
a=(3,1,2,4)
print("Tuple a: ",a)
b=(5,7,6,8)
print("Tuple b: ",b)
x=list(a+b)
c=tuple(x)
print("Tuple c: ",c)
x.sort()
d=tuple(x)
print("Tuple d: ",d)
print("Tuple[3]=",d[3])
print("3 phần tử cuối cùng của tuple d :",d[-3:])










