"""
github:https://github.com/sodiqoydinov
"""
a=int(input("Birinchi sonni kiriting:\n"))
b=int(input("Ikkinchi sonni kiriting:\n"))
while a!=0 and b!=0:
    if a>b:
        a=a%b
    else:
        b=b%a
print('EKUB=',a+b)
#Berilgan sonlarning kattasini kichigiga bo’lamiz.
#Agar bo’lganda qoldiq 0 bo’linsa, u holda kichik son EKUB hisoblanadi.
#Agar qoldiq chiqsa, unda katta sonni kichik son bilan, kichik sonni qoldiq bilan almashtiramiz.
#1 punktga qaytamiz.
#Misol uchun:
#30 va 18 sonlarning EKUB ni hisoblasak.
#30 / 18 = 1 (qoldiq 12)
#18 / 12 = 1 (qoldiq 6)
#12 / 6 = 2 (qoldiq 0)
#Yakunlandi: EKUB (30, 18) = 6 ga teng.

