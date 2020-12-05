dict0 = {'apple':'red', 'bananas': 'yellow', 'limon':'yellow'}
for k in dict0.keys():
    print(k)

for k in dict0.values():
    print(k)

for k in dict0.items():
    print(k)

print(dict0['bananas'])

dict0['bananas']='green'
print(dict0)