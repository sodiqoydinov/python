"""
github:https://github.com/sodiqoydinov
"""
def malumotlar(ismi,familiyasi,tugilgan_yili,email_manzili='',telefon_raqami=''):
    malumot={'ism':ismi,
             'familiya':familiyasi,
             "tugilg'ilgan_yil":tugilgan_yili,
             'email_manzil':email_manzili,
             'telefon_raqam':telefon_raqami
             }
    return malumot
print('Mijozlar haqida ma\'lumotlarni kiriting:')
mijoz=[]
while True:
    print("Quyidagi ma'lumotlarni kiriting: ")
    i=input("Ismingiz: ")
    f=input('Familiya: ')
    t=input("Tug'ilgan yil: ")
    e=input("Email manzili: ")
    t2=input("Telefon raqami: ")
    mijoz.append(malumotlar(i,f,t,e,t2))
    a=input("Yana mijoz qo'shasizmi (ha/yo'q): ")
    if a=="yo'q":
        break
print("Mijozlar haqida ma'lumotlar':")
print('Ismingiz:',i.title(),'\nFamiliyangiz:',f.title(),"\nTug'ilgan_yilingiz:",t.title(),'\nEmail manzilingiz:',e.title(),'\nTelefon raqamingiz:',t2.title())

   
    
    
        
  
             
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    