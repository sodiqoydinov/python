
"""
github:sodiqoydinov
Ushbu funksiyada rekursiyadan foydalanilgan bo'lib faktarialni hisoblaydi'
"""
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
#print(fact(x)) <<<bunda x ning o'rniga faktarialini topmoqchi bo'lgan sonni qo'yamiz 
