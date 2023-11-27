import re

with open("input.txt") as f:
    lines = f.readlines()


fuel_requirements = []

def convert_to_decimal(snafu):
    decimal = 0
    for digit in snafu:
        if digit == '-':
            decimal = decimal * 5 - 1
        elif digit == '=':
            decimal = decimal * 5 - 2
        else:
            decimal = decimal * 5 + int(digit)
    return decimal

def convert_to_snafu(decimal):
    snafu = ""
    while decimal != 0:
        remainder = decimal % 5
        if remainder == 4:
            decimal += 1
            snafu = '-' + snafu
        elif remainder == 3:
            decimal += 2
            snafu = '=' + snafu
        else:
            snafu = str(remainder) + snafu
        decimal = decimal // 5
    return snafu

for line in lines:
    num = convert_to_decimal(line.strip('\n'))
    print(num)
    fuel_requirements.append(num)

total = sum(fuel_requirements)
print(total)
print(convert_to_snafu(total))