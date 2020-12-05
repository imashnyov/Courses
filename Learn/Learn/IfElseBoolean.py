if 2 * 2 == 5:
    print('Ok')
else:
    print('Not Ok')

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print('---------------------------------------------------------------------------------------------')
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

password = '123456'
user_input = '000000'

if user_input == password:
    print('Welcome')
else:
    print('Wrong password')

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print('---------------------------------------------------------------------------------------------')
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# !=
# <=
# >=
# not
# and
# or

password2 = '123456'
user_input2 = '000000'

if (user_input2 == password2) and (2 * 2 == 4): #(user_input2 == password2) = False
    print('Welcome')
else:
    print('Wrong password')

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print('---------------------------------------------------------------------------------------------')
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

if 'a' in 'Pupkin':
    print('Hello Pupkin')
else:
    print('WROOOOONG -____-')

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print('---------------------------------------------------------------------------------------------')
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

s = '123456'

if len(s) == 10:
    print('Lenght 10')
elif len(s) == 6:
    print('Lenght 6')
else:
    print('Poshel nah')

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print('---------------------------------------------------------------------------------------------')
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

password3 = '123456'
user_input3 = ''

if user_input3:
    if user_input3 == password3:
        print('Welcome')
    else:
        print('Wrong password')
else:
    print('Input smth pleas')

print('-000---------------------------------------------------------------------------------------000-')

print('Always OK') if user_input3 else print('Wrong')

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print('---------------------------------------------------------------------------------------------')
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# 1 - 100
# 3 - Fizz
# 5 - Buzz
# 3 & 5 - FizzBuzz
# i

# -----------------------------------
# import timeit
#
# code_to_test = """
# def fizz_buzz(i):
#     if not (i % 3) and not (i % 5):
#         print('FizzBuzz')
#     elif not i % 3:
#         print('Fizz')
#     elif not i % 5:
#         print('Buzz')
#     else:
#         print(i)
#
#
# for i in range (1,100):
#     fizz_buzz(i)
# """
# elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print(elapsed_time)

# -----------------------------------
import timeit

code_to_test = """
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
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)
laDJLKJLJ
asdhkanlkjdsa
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print('---------------------------------------------------------------------------------------------')
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^