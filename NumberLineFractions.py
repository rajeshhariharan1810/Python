from fractions import Fraction

str_num1 = input("Start Point: ")
str_num2 = input("End Point: ")
num_points = int(input("Number of Points: "))

num1Whole = int(str_num1[:str_num1.index(" ")])
num1Num = int(str_num1[str_num1.index(" ") + 1 :str_num1.index("/")])
num1Den = int(str_num1[str_num1.index("/") + 1:])

num2Whole = int(str_num2[:str_num2.index(" ")])
num2Num = int(str_num2[str_num2.index(" ") + 1 :str_num2.index("/")])
num2Den = int(str_num2[str_num2.index("/") + 1:])

if num1Whole < 0:
    num1 = Fraction(num1Whole.__abs__() * num1Den + num1Num, num1Den) * -1
else:
    num1 = Fraction(num1Whole * num1Den + num1Num, num1Den)
if num2Whole < 0:
    num2 = Fraction(num2Whole.__abs__() * num2Den + num2Num, num2Den) * -1
else:
    num2 = Fraction(num2Whole * num2Den + num2Num, num2Den)

D = num2 - num1
d = D/(num_points + 1)

points = []
temp_point = num1

for i in range(num_points):
    points.append(temp_point + d)
    temp_point += d

x = 1
for i in range(num_points):
    print(f"Point {x}: " , points[i])
    x += 1