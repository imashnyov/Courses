f = open('1.txt', 'w')
f.write('Привет уебок!')
f.close()

f = open('1.txt', 'r')
print(f.read())
f.close()

with open('1.txt', 'a') as f:
    f.write('бугага')
