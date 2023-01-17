
text = bytes('привет'.encode())
bytes_ = b'test'
print(type(text))
print(text)

a = 'Chris'
b = bytes(a, encoding='utf-8')
print(type(b))
print(b)

a = b.decode()
print('Original String =', a)

list1 = [1, 2, 3, 4]
b = bytes(list1)
print(b)



