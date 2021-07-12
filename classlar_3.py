"""
github:https://github.com/sodiqoydinov
"""
class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.bosqich=1
        
    def get_info(self):
        return"f{self.ism} {self.familiya}.{self.bosqich}-bosqich talabasi"
    def get_name(self):
        return self.ism
    def get_lastname(self):
        return self.familiya
    def get_born(self):
        return self.tyil

class Fan:
    def __init__(self,nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]
    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni+=1

def see_methods(klass):
    return [method for method in dir(klass)  if method.startwith('__')]

talaba1=Talaba("Sodiq","Oydinov",2005)






