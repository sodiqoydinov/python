"""
github:https://github.com/sodiqoydinov
"""
def avto_info(kompaniya,model,rangi,yili,narhi=None):
    avto={'kompaniya':kompaniya,
          'model':model,
          'rang':rangi,
          'yil':yili,
          'narh':narhi}
    return avto
def avto_kirit():

    avtolar=[]
    while True:
        print("\nQuyidagi ma\'lumotni kiriting",end='')
        kompaniya=input('Ishlab chiqaruvchi: ')
        model=input('Modeli: ')
        rangi=input('Rangi: ')
        yili=input('Ishlab chiqarilgan sana: ')
        narhi=input('Narhi: ')
        avtolar.append(avto_info(kompaniya,model,rangi,yili,narhi))
        javob=input("Yana avto qo\'shasizmi? (ha/yo'q): ")
        if javob =="yo'q":
            break
def info_print(avto_info):
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()}")
    print( f"{avto_info['model' ].upper()},{avto_info['karobka']} karobka,")
    print(f"{avto_info['yil']}-yil, {avto_info['narh']}$")
    