dict1 = {1: 'Ch', 2: 'ris'}
print(type(dict1))
print(dict1)

dict2 = dict({3: 'Au', 4: 'rum'})
print(type(dict2))
print(dict2)

a = dict2[3]
print(a)
b = dict2.get(4)
print(b)

dict2[5] = 'OH9'
print(dict2)
del dict2[3]
print(dict2)