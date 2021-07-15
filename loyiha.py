"""
github:https://github.com/sodiqoydinov
"""
from colorama import Fore,Back
q=str(input("Salom menga istalgan matningizni kiriting va u matnning orqa fondagi rangi va matnning rangini o'zgartiring:\n"))
print("Avval matnning rangini belgilang")
e=(Fore.BLACK + '0')
e+=(Fore.BLUE + '1')
e+=(Fore.CYAN + '2')
e+=(Fore.GREEN + '3')
e+=(Fore.LIGHTBLACK_EX +'4')
e+=(Fore.LIGHTBLUE_EX +'5')
e+=(Fore.LIGHTCYAN_EX + '6')
e+=(Fore.LIGHTGREEN_EX +'7')
e+=(Fore.LIGHTMAGENTA_EX +'8')
e+=(Fore.LIGHTRED_EX +'9')
e+=(Fore.LIGHTWHITE_EX +'10')
e+=(Fore.LIGHTYELLOW_EX +'11')
e+=(Fore.MAGENTA +'12')
e+=(Fore.RED +'13')
e+=(Fore.RESET +'14')
e+=(Fore.WHITE +'15')
e+=(Fore.YELLOW +'16')
print(e)
print("Istalgan raqamni bossangiz kiritgan matiningiz o'sha ranga o'tadi")
try:
    r=int(input("Rangni tanlang:\n"))
    if r==0:
        print(Fore.BLACK +q)
    elif r==1:
        print(Fore.BLUE +q)
    elif r==2:
        print(Fore.CYAN +q)
    elif r==3:
        print(Fore.GREEN +q)
    elif r==4:
        print(Fore.LIGHTBLACK_EX +q)
    elif r==5:
        print(Fore.LIGHTBLUE_EX +q)
    elif r==6:
        print(Fore.LIGHTCYAN_EX +q)
    elif r==7:
        print(Fore.LIGHTGREEN_EX +q)
    elif r==8:
        print(Fore.LIGHTMAGENTA_EX +q)
    elif r==9:
        print(Fore.LIGHTRED_EX +q)
    elif r==10:
        print(Fore.LIGHTWHITE_EX +q)
    elif r==11:
        print(Fore.LIGHTYELLOW_EX +q)
    elif r==12:
        print(Fore.MAGENTA +q)
    elif r==13:
        print(Fore.RED +q)
    elif r==14:
        print(Fore.RESET +q)
    elif r==15:
        print(Fore.WHITE +q)
    elif r==16:
        print(Fore.YELLOW +q)
except ValueError:
    print('Siz faqat 1 dan 16 gacha sonlarni kiritishingiz mumkin')
print('Endi orqa foniga rang bering')
print('Bu yerda orqa fon rangini tanlash tekst rangini tanlsh kodi bilan bir xil (masalan:1 ni bossangiz orqa fon ham ko\'k ranga o\'tadi)')
try:
    y=int(input('Rangni tanlang:\n'))
    if r==0:
        print(Back.BLACK +q)
    elif r==1:
        print(Back.BLUE +q)
    elif r==2:
        print(Back.CYAN +q)
    elif r==3:
        print(Back.GREEN +q)
    elif r==4:
        print(Back.LIGHTBLACK_EX +q)
    elif r==5:
        print(Back.LIGHTBLUE_EX +q)
    elif r==6:
        print(Back.LIGHTCYAN_EX +q)
    elif r==7:
        print(Back.LIGHTGREEN_EX +q)
    elif r==8:
        print(Back.LIGHTMAGENTA_EX +q)
    elif r==9:
        print(Back.LIGHTRED_EX +q)
    elif r==10:
        print(Back.LIGHTWHITE_EX +q)
    elif r==11:
        print(Back.LIGHTYELLOW_EX +q)
    elif r==12:
        print(Back.MAGENTA +q)
    elif r==13:
        print(Back.RED +q)
    elif r==14:
        print(Back.RESET +q)
    elif r==15:
        print(Back.WHITE +q)
    elif r==16:
        print(Back.YELLOW +q)
except ValueError:
    print('Siz faqat 1 dan 16 gacha sonlarni kiritishingiz mumkin')