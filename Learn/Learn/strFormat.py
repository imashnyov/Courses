#'Hello {}' .format(name)
name = 'world'
s = 'Hello {}'
result = s.format(name)
print(result)
#---------------------------------------------------------------------------------------------
name1='Leone'
number=100
pattern = '{} - {}'
result1 = pattern.format(name1, number)
print(result1)
#---------------------------------------------------------------------------------------------
name2='IronMan'
number2=5
pattern1='{movie} - {rating}'
result2=pattern1.format(movie=name2, rating=number2)
print(result2)
#---------------------------------------------------------------------------------------------
result3 = f'{name2} - {number2}'
print(result3)
#---------------------------------------------------------------------------------------------