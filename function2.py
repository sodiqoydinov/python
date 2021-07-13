"""
github:https://github.com/sodiqoydinov
"""
def ism(ism,yosh,hozirgi_yil=2021):
    '''Ism va yoshni so\'rab uning tug\'igan yilini hisoblaydigan funksiya'''
    print(f'Foydalanuvchi ismi:{ism.title()}')
    print(f'Foydalanuvchi tug\'ilgan yili:{hozirgi_yil-yosh}')
ism('sodiq',16,2021)
#2)
def son(a):
    """Foydalanuvchidan son olib uning kvadrati va kubini qaytaruvchi funksiya"""
    print(f'{a} ning kvadrati {a**2} ga teng')
    print(f'{a} ning kubi {a**3} ga teng')
son(2) 
#3)
def sonlar(b):
    """Son olib uning toq yoki juftligini aniqlaydigan funksiya"""
    if b%2==0:
        print(f'{b} soni juft son')
    else:
        print(f'{b} soni toq son')
sonlar(112)
sonlar(111)
#4)
def taqqoslash(c,d):
    """ 2 ta son olib,ulardan kattasini konsolga chiqaruvchi funksiya"""
    if c>d:
        print(f'{c} soni {d} sonidan katta')
    elif c==d:
        print(f'{c} soni va {d} sonlari teng')
    else:
        print(f'{d} soni {c} sonidan katta')
taqqoslash(123,1234)
taqqoslash(1,1)
taqqoslash(4598,1111)
#5)
def daraja(x,y):
    ''' X va Y sonlarini olib,x ning y chisini topuvchi funksiya'''
    print(f'{x**y} ga teng')
daraja(1,1)
#6)
def bolinish(n):
    """ 2 dan 10 gacha bo\'lgan sonlarga qoldiqsiz bo\'linishini tekshiruvchi funksiya"""
    z=list(range(2,11))
    for s in z:
        if n%s!=0:
            print(f'{n} {s} ga qoldiqli bo\'linadi')
        else:
                print(f'{n} {s} ga qoldiqsiz bo\'linadi')
bolinish(100)