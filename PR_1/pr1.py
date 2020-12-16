abc1 = 'abcdefghijklmnopqrstuvwxyz'
abc2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc3 = 'абвгдежзийклмнопрстуфхцчшщъьыэюя'
abc4 = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
s = (input("Ввевдите язык (ru/en)"))
n = int(input("Введите сдвиг: "))
st = input("Введите строку: ")
res = ''
if (s == 'ru'):
    for i in st:
        if ( ord(i) >= 410 ):
            res += abc4[(abc4.index(i) + n) % len(abc4)]
        else:
            res += abc3[(abc3.index(i) + n) % len(abc3)]
else:
    for i in st:
        if ( ord(i) >= 41 ):
            res += abc2[(abc2.index(i) + n) % len(abc2)]
        else:
            res += abc1[(abc1.index(i) + n) % len(abc1)]

print(res)