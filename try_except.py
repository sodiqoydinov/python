"""
try va except qisqacha misollar
github:https://github.com/sodiqoydinov
"""
yosh=input("Yoshingizni kiriting: ")
try:
    yosh=int(yosh)
    print(f"Siz {2021-yosh} yilda tug'ilgansiz")
except:
    print('Siz butun son kiritmadingiz')
user={'username':'sodiq7898',
      'status':'admin',
      'email':'sodiq7898',
      'phone':'998990327898'}
key='email'
try:
    print(f"Foydalanuvchi: {user[key]}")
except KeyError:
    print('Bunday kalit mavjud emas')

print(user['username'])

mevalar=['olma','anor','anjir','uzum']
try:
    print(mevalar[0])
except IndexError:
    print(f"Ro'yxatda {len(mevalar)} ta meva bor")
    
fayl='data.txt'
try:
    with open(fayl) as f:
        text=f.read()
except FileNotFoundError:
    print(f"{fayl} mavjud emas")


while True:
    yosh=input("Yoshingizni kiriting: ")
    if yosh.isdigit(): # isdigit-raqamlardaniboratmi yo'qmi tekshiradi
        yosh=int(yosh)
        break
print(f"Siz {2021-yosh} yilda tug'ilgansiz")
