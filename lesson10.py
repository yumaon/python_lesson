# タプル
t = (1, 2, 3, 4 ,1,2)
print(t) # (1, 2, 3, 4, 1, 2)
print(type(t)) # <class 'tuple'>

# t[0] = 100 というように値を書き換えることはできない
# 以下のように取得はできる
print(t[0]) # 1
print(t[2:5]) # (3, 4, 1)
print(t.index(1)) # 0
print(t.index(1, 1)) # 4
print(t.count(1)) # 2
# print(help(tuple))

# タプルにリストを入れる
t = ([1, 2, 3], [4, 5, 6])
print(t)  # ([1, 2, 3], [4, 5, 6])
# t[0] = 1 書き換えはできない
# しかし以下は可能
t[0][0] = 100
print(t) # ([100, 2, 3], [4, 5, 6])
t = 1, 2, 3 # このように記述してもtupleになる
print(type(t)) # <class 'tuple'>
t = 1, # これだけでtupleになる
print(t, type(t)) # (1,) <class 'tuple'>
t = ()
print(type(t)) # <class 'tuple'>
t = (1)
print(t, type(t)) # 1 <class 'int'> これはintになる
t = ('test')
print(t, type(t)) # test <class 'str'> 文字列も同じでstrになる
# 一つしか入れないtupleはほとんどないが、入れるとしたらカンマをつける必要がある
t = (1,)
print(t, type(1)) # (1,) <class 'int'>
# タプルの値を変える変えることはできないが、以下のように新しく定義することができる
new_tuple = (1, 2, 3) + (4, 5, 6)
print(new_tuple, type(new_tuple)) # (1, 2, 3, 4, 5, 6) <class 'tuple'>