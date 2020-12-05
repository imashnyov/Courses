movie = 'Leon'
rating = 98
result = f'Movie: {movie}, rating: {rating}'
print(result)
#-----------------------------------------------------------------------
print()
#-----------------------------------------------------------------------
movie = 'Alien'
rating = 200
result = f'Movie: {movie}, rating: {rating}'
print(result)
#------------------------------------------------------------------------
print()
#-----------------------------------------------------------------------

#vvv функции vvv
def greet():
    print('Hello world!')

greet()
#------------------------------------------------------------------------
print()
#-----------------------------------------------------------------------
#def greet1(name):
#    print('Hello,'+name+'!')
#greet1()

def greet1(name):
    result1 = f'Hello {name}'
    print(result1)

greet1('Oleg')
#-----------------------------------------------------------------------
def greet1(message, name):
    result1 = f'{message}, {name}'
    print(result1)
greet1('Goodbye', 'Oleg')
#-----------------------------------------------------------------------
def greet2(message, name):
    result2 = f'{message}, {name}'
    print(result2)
greet2(message='Goodbye', name='Oleg')
#-----------------------------------------------------------------------
def greet2(message, name):
    result2 = f'{message}, {name}'
    print(result2)
greet2(message='Goodbye', name='Oleg')
#-----------------------------------------------------------------------
def greet2(message, name='Genka'):
    result2 = f'{message}, {name}'
    print(result2)
greet2(message='Goodbye')
#-----------------------------------------------------------------------

greeting = 'Hello'
to = 'world (greetingTO)'
def greet3(message, name='Genka'):
    result3 = f'{message}, {name}'
    print(result3)
greet2(greeting, to)
#message = greeting = 'Hello'

#-----------------------------------------------------------------------

greeting = 'return1 '
to = 'return2'
def greet4(message, name='Genka'):
    result4 = f'{message}, {name}'
    return result4
g = greet4(greeting, to)
print(g)

#-----------------------------------------------------------------------

greeting = '           return3 '
to = 'return456'
def greet5(message, name='ebolik'):
    result5 = f'{message} - {name}'
    return result5

g = greet5('              tolik').title().strip()
print(g)
