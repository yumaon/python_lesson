num = 1
name = '1'
#一応方宣言もできるがなくてもほぼ一緒の挙動
num2 = 2
name2 = "aaa"

print("num2:", num2, type(num2)) # num2: 2 <class 'int'>
print("name2:", name2, type(name2)) # name2: aaa <class 'str'>

#方変換
new_num = int(name)
print("new_num:", new_num, type(new_num)) # new_num: 1 <class 'int'>

#方宣言をしてても自動的に型が変わる
print("num2:", num2, type(num2)) # num2: 2 <class 'int'>
num2 = name2
print("num2:", num2, type(num2)) # num2: aaa <class 'str'>

print("Hi", "Mike", sep=", ", end='.\n')

print(2 + 2)