list1 = [1,2,3,4,5,1]
fz = frozenset(list1)
print(type(fz))
print(fz)

fz_len = len(fz)
print(fz_len)
print((1 in fz), (1 not in fz))
