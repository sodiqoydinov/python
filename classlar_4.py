"""
github:https://github.com/sodiqoydinov
"""
class Avto:
    def __init__(self,model,nom,rang,yil=2021,km=0):
        self.modeli=model
        self.nomi=nom
        self.rangi=rang
        self.yili=yil
        self.km=km
    def get_info(self):
        return f'Modeli:{self.modeli} Nomi:{self.nomi} Rangi:{self.rangi} rangda Yili:{self.yili} km:{self.km}km'
    def set_model(self,almashtirish):
        self.modeli=almashtirish
    def set_nom(self,almashtirish):
        self.nomi=almashtirish
    def set_rang(self,almashtirish):
        self.rangi=almashtirish
    def set_yil(self,almashtirish):
        self.yili=almashtirish
    def update_km(self,almashtirish):
        self.km=almashtirish
class Avtosalon:
    def __init__(self,salon_nomi,manzili,sotuvdagi_avtomobillar):
        self.salon_nomi=salon_nomi
        self.manzili=manzili
        self.sotuvdagi_avtomobillar=sotuvdagi_avtomobillar
    def avto_info(self):
        return f'Salon nomi:{self.salon_nomi} manzili:{self.manzili} Sotuvdagi avtomobillar:{self.sotuvdagi_avtomobillar}'
    def set_salon_nomi(self,almashtirish):
        self.salon_nomi=almashtirish
    def set_manzili(self,almashtirish):
        self.manzili=almashtirish
    def ssa(self, *almashtirish ):#           ssa=set_sotuvdagi_avtomobillar
        self.sotuvdagi_avtomobillar=almashtirish
        
        