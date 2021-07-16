"""
github:https://github.com/sodiqoydinov
"""
a=int(input("Son kiriting:\n"))
b=int(input("Sonning darajasini kiriting:\n"))
if b%4!=0:
    w=b%4
    e=a**w
    print(f"{a}ning {b}-darajasining oxirgi raqami {e} bilan tugaydi")
elif b%4==0:
    r=a**4
    print(f"{a}ning {b}-darajasining oxirgi raqami {r} bilan tugaydi")
    