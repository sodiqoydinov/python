"""
github:sodiqoydinov
"""
import math
x=400
print(math.sqrt(x)) #Ildizni hisoblash

import random as r
son=r.randint(0,100)  # random tarzda raqamni tanlab berish
print(son)

ismlar=['Sodiq','Gulasal','Parizoda']
ism=r.choice(ismlar) # random tarzda so'zni tanlab berish
print(ism)


x=list(range(0,51,5))
print(x)
print(r.choice(x)) # 0 dan 50 gacha 5 qadamlab son tanlab berish

x=list(range(11))
print(x)
r.shuffle(x) # 0 dan 10 gacha bo'lgan sonlarni tartibini o'zgartirish
print(x)
