list_ = []
print(list_)
list_.append(1)
list_.append(2)
list_.pop(1)
print(list_)
list_.insert(0, 5)
print(list_)

list_1 = [1, 2, 3, 4, 5]
print(list_1[3])
list_2 = list_1
list_2 = [1, 2, 3, 4, 5]
list_2.append(25)

print(list_1, list_2)
print(id(list_1), id(list_2))