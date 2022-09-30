num = int(input('enter number->'))
res = ''

if num > 0:
    res = 'Number is positive'
elif num < 0:
    res = 'Number is negative'
elif num == 0:
    res = 'Number is equal to zero'

print(f'{res}')