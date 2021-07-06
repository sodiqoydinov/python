"""
Baxolash funksiyasi
github:https://github.com/sodiqoydinov
"""
def bahola(ismlar):
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=input(f'Talaba {ism.title()}ning bahosini kiriting:')
        baholar[ism]=int(baho)
    return baholar
talabalar=['Sodiq','Parizoda','Gulasla']
baholar=bahola(talabalar[:])
print(baholar)
