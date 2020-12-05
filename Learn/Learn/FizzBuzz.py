def fizz_buzz(i):
    if not (i % 3) and not (i % 5):
        return 'FizzBuzz'
    elif not i % 3:
        return 'Fizz'
    elif not i % 5:
        return 'Buzz'
    else:
        return i

for i in range (1,100):
    print(fizz_buzz(i))
