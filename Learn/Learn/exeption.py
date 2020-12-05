try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError:
    print('Я тебя на ноль помножу')