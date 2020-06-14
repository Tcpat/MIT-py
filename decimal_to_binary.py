number = int(input("Enter a number: "))
list = []
while number>0:
    a = number%2
    b = number//2
    list += str(a)
    number = b
list = list[::-1]
number = ""
for i in range(len(list)):
    number += list[i]
number = int(number)
print("In binary it would be " + str(number))
