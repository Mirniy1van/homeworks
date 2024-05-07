a= int(input("введите число от 1 до 50: "))

if 1 <= a <= 50 :
    print("ok")

b = int(input("Введите любое число: "))

if a != b :
    if a > b:
        print("A > B")
    if a < b:
        print("B > A")
else:
    print("A = B")

if a <= 10 and a > b:
    print("B < 10")

if "34" > "124":
    print ("success")
if [1, 2, 3] == [1, 2, 3]:
    print("success")
if '6' != 11:
    print("success")




