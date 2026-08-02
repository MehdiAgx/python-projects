lst = ['yes', 'no', 'yes', 'yes', 'no', 'yes', 'no']

name='d:/answer.txt'

with open (name,'w') as f:
    for i in lst:
        f.write(i)
        f.write('\n')

c1=0
c2=0

with open (name, 'r') as f:
    lines=f.readlines()
    for i in lines:
        x=i.strip()
        if x =='yes':
            c1+=1
        else:
            c2+=1
print(c1)
print(c2)

print('------------------')

a=bytes([72, 86, 75, 93, 88, 102, 81, 110])
#print(a)
print(a.decode())

import glob
print(glob.glob('d:/*'))

import csv
y = ['Name' , 'Age']
r1 = ['sami', 43]
r2= ['kami', 32]
r3= ['nami', 65]


with open ('d:/e.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(y)
    w.writerows([r1,r2,r3])

   