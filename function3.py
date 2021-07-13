"""
github:https://github.com/sodiqoydinov
"""
def toliq_ism_yasa(ism,familiya):
    toliq_ism=f'{ism} {familiya}'
    return toliq_ism
talaba=toliq_ism_yasa('olim','hakimov')
talaba2=toliq_ism_yasa('hakim','olimov')
print(f'Darsga kelmagan talabalar:{talaba} va {talaba2}')
print(f'{talaba} darsga kechikib keldi')
#2)
def toliq_ism_yas(ism,familiya,otasining_ismi=''):
    if otasining_ismi:
        toliq_ism=f'{ism} {otasining_ismi} {familiya}'
    else:
        toliq_ism=f'{ism} {familiya}'
    return toliq_ism.title()
print(f'Darsga kechikib kelgan talabalar:{talaba} {talaba2}')
#3)
def avto_info(kompaniya,model,rangi,yili,narhi=None):
    avto={'kompaniya':kompaniya,
          'model':model,
          'rang':rangi,
          'yil':yili,
          'narh':narhi
          }
    return avto
avto1=avto_info('GM','Malibu','Qora',2018)
avto2=avto_info('GM','Gentra','Oq',2016,15000)
avtolar=[avto1,avto2]
print('Onlayn bozordagi mavjud avtomashinalar')
for avto in avtolar:
    if avto['narh']:
        narh=avto['narh']
    else:
        narh='Noma\'lum'
    print(f"{avto['rang']} {avto['model']}.Narhi:{narh}")