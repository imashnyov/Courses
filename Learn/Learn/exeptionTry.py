m = input('Введите массу:')
def calc(m):
    #100 : 10 = m :x
    try:
        m = int(m)
    except Exception as e:
        print(e)
    else:
        return 10 * m / 1000
    finally:
        print('Количество соли в вашем мясе равно:')
print(calc(m))