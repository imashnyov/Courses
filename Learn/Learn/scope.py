def a(name):
    print(locals())

a('Privet ueba')

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print('----------------------------------- Name Spaces ------------------------------------------')
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

name1 = 'Eroha'

def b():
    name1 = 'pupkin'
    age = 12
    print('Функция b пространство имен', locals())

print('Внешнее пространство имен', locals())

b()

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print('----------------------------------- Name Spaces 2 ------------------------------------------')
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

lvl = 'in Global'

def c():
    #lvl = 'in Enclosed'

    def e():
        #lvl = 'in Local'
        print(lvl)
        print(locals())

    e()

c()