# 辞書型
d = { 'x' : 10, 'y' : 20 }
print(d) # {'x': 10, 'y': 20}
print(type(d)) # <class 'dict'>
print(d['x']) # 10
print(d['y']) # 20
d['x'] = 'xxxx'
print(d['x'])

d = dict(a = 10, b = 20)
print(d) # {'a': 10, 'b': 20}

print(d.keys(), d.values()) # dict_keys(['a', 'b']) dict_values([10, 20])

d2 = {'x': 1000, 'j': 500, 'a': 1999}
print(d2) # {'x': 1000, 'j': 500, 'a': 1999}

d.update(d2)
print(d) # {'a': 1999, 'b': 20, 'x': 1000, 'j': 500}
print(d['a']) # 1999
print(d.get('a')) # 1999

# print(d['T']) 存在しないキーを指定したこの場合はエラーになる
print(d.get('T')) # None この場合はNoneとかえってくる。エラーにはならない

if d.get('T'):
    print("y")
else:
    print('n')

pop_a = d.pop('a')
print(pop_a) # 1999
print(d) # {'b': 20, 'x': 1000, 'j': 500}
del  d['j']
print(d) # {'b': 20, 'x': 1000}

d.clear()
print(d) # {}

# del d
# print(d) この場合はエラー

d = {'a': 1999, 'b': 20, 'x': 1000, 'j': 500}

print('a' in d) # True
print('T' in d) # False
