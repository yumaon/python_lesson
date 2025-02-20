s = 'test'
print(s)
print("test")
print("I d'''")
print('say "I don\'t know" ')
print('hello. \nHow are you?')
print('C:\name\name') # 途中で改行されてしまう
print(r'C:\name\name') # こうすることで　C:\name\name　と出力できる
print("##########")
print("""\
line1
line2
line3\
""")
print("##########")
print('Hi' * 3 + 'Nike')
print('Py' + 'thon')
s = 'aaaaaaaaaa'\
     'bbbbbbbbbb'
print(s)

word = 'python'
print(word[0]) # p
print(word[-1]) # 最後の文字 n が出力
print(word[0:2]) # py
print(word[2:5]) # tho
print(word[:2]) # これもpy
print(word[2:]) # thon

# word[0] = 'j' これはエラーになる
word = 'j' + word[1:]
print(word) # jython エラーにならない

print(word[:]) # wordのコピー

n = len(word)
print(n)