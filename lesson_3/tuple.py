tuple1 = (5, 2, 4, 3, 1,)
print(type(tuple1))
print(tuple1[-2])
print((3 in tuple1), (7 in tuple1))
print(sorted(tuple1))

tuple2 = 1,
print(type(tuple2))

tuple3 = ('A', ' ', 'B', 'A', ' ', 'C')
print(tuple3.count('A'))
tuple3 = ''.join(tuple3)
print(tuple3)

tuple4 = list(tuple3)
print(tuple4)


