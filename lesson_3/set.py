set1 = {1,2,3,4,3,5}
print(set1)

set2 = {'1', '2', '3', '4', '3', '5'}
print(set2)

set3 = set([1, 2, 3, 4, 5, 1])
print(set3.add(6))
print(set3.discard(1))
print(type(set3))
print(set3)

set4 = {7, 8, 9, 10}
set_all = set3.union(set4)
print(set_all)

set5 = set()
print(type(set5))