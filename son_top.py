"""
GetHub >>> Sodiq7898
Birinchi o'yinim
"""
import random as r
a=r.randint(1,10)
c=0
d=True
print('Keling son topish o\'yinini o\'ynaymiz\n Men 1 dan 10 gacha son o\'yladim u qaysi son')
while d:
    c+=1
    g=int(input('Son kiriting:'))
    if g>a:
        print("Xato men o'ylagan son bundan kichik edi.Yana urinib ko'ring")
    elif g<a:
        print("Yo'q men o'ylagan son bundan katta\n Yana urinib ko'ring")
    else:
        d=False
print("Topdingiz")
print(f"Siz {c}ta taxmin bilan topdingiz")

print("Endi siz 1 dan 10 gacha son o'ylang men topishga harakat qilaman")   
t=0
x=1
z=10
a2=r.randint(x,z)
f=input("O'ylab bo'lgan bo'lsangiz istalgan raqam ni kiriting\n>>>")
if f:
    while True:
        t+=1
        a2=r.randint(x,z)
        y=input(f"Siz {a2} sonini o'yladingiz:agar to'g'ri bo'lsa t harfini ,men o'ylagan son bundan katta (+), kichikroq(-)\n ".lower())
        if y=='+':
            x=a2+1
        elif y=='-':
            z=a2-1
        else:
            break
    print(f"Men {t} ta taxmin bilan topdim!")    
if c==t:
    print("Durrang")
elif c>t:
    print("Siz yutqazdingiz")
else:
    print("Siz Yutdingiz")
