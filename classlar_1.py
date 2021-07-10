"""
Classlar bilan ishlash
github:https://github.com/sodiqoydinov
"""
class Shaxs:
    __kiritilgan_shaxslar_soni=0
    def __init__(self,ism,familiya,pasporti,tugilgan_yili):
        self.name=ism
        self.lastname=familiya
        self.__pasport=pasporti
        self.__tyil=tugilgan_yili
        Shaxs.__kiritilgan_shaxslar_soni+=1
    def get_info(self):
        return f"Ismi:{self.name} Familiyasi:{self.lastname} passport id :{self.__pasport} Tug'ilgan yili {self.__tyil} "
    def passport(self):
        return self.__pasport
    def get_tyil(self):
        return self.__tyil
    def get_age(self,yil):
        return yil-self.born
    
    def shaxslar_soni(cls):
        return cls.__kiritilgan_shaxslar_soni
class Talaba(Shaxs):
    def __init__(self,ism,familiya,passport,tyil,idraqam):
        super().__init__(ism,familiya,passport,tyil)
        self.__idraqam=idraqam
        self.bosqich=1
    def get_id(self):
        return self.__idraqam
    def get_bosqich(self):
        return self.bosqich
    def get_info(self):
        info=f'{self.ism} {self.familiya}'
        info+=f'{self.get_bosqich()}-bosqich. ID raqami:{self.idraqam}'

shaxs1=Shaxs('Sodiq','Oydinov','None',2005)
shaxs2=Shaxs('Mariyam','Turaqurulova','IO998101',1982)
#talaba1=Talaba('Sodiq','Oydinov','',2005,'')

