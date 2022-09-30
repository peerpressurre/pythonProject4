num1 = int(input('enter first number->'))
num2 = int(input('enter second number->'))
res = ''

if num1 == num2:
    res = 'Numbers are equal'
elif num1 < num2:
    res = num1, num2
elif num1 > num2:
    res = num2, num1

print(f'{res}')