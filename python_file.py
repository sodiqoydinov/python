"""
github:https://github.com/sodiqoydinov
"""
faylnomi='dars333.txt'
with open(faylnomi,'w') as fayl:
    fayl.write("I'm programmer\n")
    fayl.write("Sodiq Oydinov is the best programmer\n")
with open('dars333.txt') as file:
    a=file.read()
print(a)
import pickle
talaba1={'ismi':'Sodiq','familiyasi':'Oydinov','tyil':2005}
with open('info','wb') as file1:
    pickle.dump(talaba1,file1)

import pickle
with open('info','rb') as file1:
    talaba1=pickle.load(file1)
print(talaba1)


with open('Documents\pi_mil.txt') as file:
    pi=file.read()
pi=pi.rstrip()
pi=pi.replace('\n','')
pi=pi.replace(' ','')
a=float(pi)
t=13082005
if t in a:
    print(f'{t} bor')
else:
    print(f'{t} raqamlari mavjud emas')
    
#pi=float(pi)
#with open('Documents\pi_mil.txt') as file:
 #   pickle.dump(pi,file)
#with open('Documents\pi_mil.txt') as file:
 #   q=file.read()
#print(q)
file='Documents\pi_mil.txt'
t=str('13082005')
if file in t:
    print(t)
else:
    print('Bunday raqam yo\'q')
