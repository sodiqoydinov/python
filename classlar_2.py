"""
Classlar biln ishlash-2
github:https://github.com/sodiqoydinov
"""
class Avto:
    __num_avto=0
    def __init__(self,make,model,rang,yil,narh):
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        Avto.__num_avto+=1
    def __repr__(self):
        return f'{self.rang} {self.make} {self.model}'
    def __eq__(self,y):
        return self.narh==y.narh
    def  __lt__(self,y):
        return self.narh<y.narh
    def __le__(self,y):
        return self.narh<=y.narh
avto1=Avto('GM','Malibu','Qora',2020,40000)
avto2=Avto('GM','Lacetti','Oq',2020,20000)
avto3=Avto('Honda','Accord','Oq',2017,40000)
print(avto1)#==avto3)

class Avtosalon:
    def __init__(self,name):
        self.name=name
        self.avtolar=[]
    def __repr__(self):
        return f'{self.name} avtosaloni'
    def add_avto(self,avto):
        if isinstance(avto,Avto):
            self.avtolar.append(avto)
        else:
            print("Avto obyektini kiriting")