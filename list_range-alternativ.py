"""
github:https://github.com/sodiqoydinov
"""
def oraliq(min,max,qadam=1):
    sonlar=[]
    while min<max:
        sonlar.append(min)
        min+=qadam
    return sonlar
#print(oraliq(1,101))
#Ushbu funksiya pythonda list range ni o'rniga undan qulayroq tarzda yasalgan