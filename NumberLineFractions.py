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

def number(num):
    if num.find("/") == -1:
        return int(num)
    numWhole = int(num[:num.index(" ")])
    numNum = int(num[num.index(" ") + 1:num.index("/")])
    numDen = int(num[num.index("/") + 1:])

    if numWhole < 0:
        num = Fraction(numWhole.__abs__() * numDen + numNum, numDen) * -1
        return num
    else:
        num = Fraction(numWhole * numDen + numNum, numDen)
        return num

def convert(num):
    if type(num) is float:
        return num
    else:
        whole = num.numerator // num.denominator
        remainder = num.numerator % num.denominator
        if remainder == 0:
            return str(whole)
        else:
            return f"{whole} {Fraction(remainder, num.denominator)}"

def main():
    str_num1 = input("Start Point: ")
    str_num2 = input("End Point: ")
    numPoints = int(input("Number of Points: "))

    no1 = number(str_num1)
    no2 = number(str_num2)
    answer = calculate(no1, no2, numPoints)
    mixedAnswer = [convert(i) for i in answer]

    x = 1
    for j in range(numPoints):
        print(f"Point {x}: ", mixedAnswer[j])
        x += 1

if __name__ == "__main__":
    main()