what = input('что делаем (+,-,*,/): ')
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

if what == '+':
    c = a+b
elif what == '-':
    c = a-b
elif what == '*':
    c = a*b
elif what == '/':
    c = a/b
else:
    print('x')
print('Результат: ' + str(c))
input()
