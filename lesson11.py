# タプルのアンバッキング
num_tuole = (10, 20)
print(num_tuole) # (10, 20)

x, y = num_tuole
print(x, y) # 10 20
print(type(x), type(y)) # <class 'int'> <class 'int'>

x, y = 10, 20
print(x, y) # 10 20
# 変数宣言でこのように書いているが、実際はタプルで展開している

min, max = 0, 100
print(min, max) # 0 100

# iとjの入れ替え
i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j) # 20 10
# このように書けるが長くなる。アンパッキングを使用すると簡単にかける
a = 100
b = 200
print(a, b) # 100 200
a, b = b, a
print(a, b) # 200 100

