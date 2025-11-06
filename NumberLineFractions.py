from fractions import Fraction

def calculate(num1, num2, num_points):
    D = num2 - num1
    d = D/(num_points + 1)

    points = []
    temp_point = num1

    for i in range(num_points):
        points.append(temp_point + d)
        temp_point += d

    return points

def number1(num1):
    if num1.find("/") == -1:
        return num1
    else:
        num1Whole = int(num1[:num1.index(" ")])
        num1Num = int(num1[num1.index(" ") + 1 :num1.index("/")])
        num1Den = int(num1[num1.index("/") + 1:])

        if num1Whole < 0:
            num1 = Fraction(num1Whole.__abs__() * num1Den + num1Num, num1Den) * -1
            return num1
        else:
            num1 = Fraction(num1Whole * num1Den + num1Num, num1Den)
            return num1

def number2(num2):
    if num2.find("/") == -1:
        return num2
    else:
        num2Whole = int(num2[:num2.index(" ")])
        num2Num = int(num2[num2.index(" ") + 1:num2.index("/")])
        num2Den = int(num2[num2.index("/") + 1:])

        if num2Whole < 0:
            num2 = Fraction(num2Whole.__abs__() * num2Den + num2Num, num2Den) * -1
            return num2
        else:
            num2 = Fraction(num2Whole * num2Den + num2Num, num2Den)
            return num2

def convert(num):
    whole = num.numerator // num.denominator
    remainder = num.numerator % num.denominator
    if remainder:
        return str(whole)
    else:
        return f"{whole} {Fraction(remainder, num.denominator)}"

str_num1 = input("Start Point: ")
str_num2 = input("End Point: ")
numPoints = int(input("Number of Points: "))

no1 = number1(str_num1)
no2 = number2(str_num2)
answer = calculate(no1, no2, numPoints)
mixedAnswer = []
for z in answer:
    mixedAnswer.append(convert(z))

x = 1
for j in range(numPoints):
    print(f"Point {x}: ", mixedAnswer[j])
    x += 1