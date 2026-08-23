pi=3.14
def area(r):
    return pi*r*r
def circumference(r):
    return pi*2*r
def main():
    r=8
    print(area(r))
    print(circumference(r))
main()   

print('------------------')

y=8
def g():
    global y
    y=2
    print(y)
g()   
print(y)

print('--------------------')

def z(d):
    d['a']-=1
    d['b']+=1
my_dict={'a':5,'b':9}
z(my_dict)
print(my_dict['a'])
print(my_dict['b'])  

print('--------------------')

def h(a,b):
    print(a,b)
h(7,3)    

print('--------------------')

def switch(t):
    u={4:'four', 8:'eight'}
    return u.get(t,'nothing')
print(switch(4))
print(switch(8))
print(switch(9))

print('--------------------')

def reverse_string(x):
    i=''.join(reversed(x))
    return i
print(reverse_string('mettitherich'))

print('--------------------')

def f(x):
    return x * 7
print(f(7))

print('--------------------')

x = lambda y : y + 6
print(x(9))

print('--------------------')

add = lambda x , y :x * y
print(add(5 , 7))

print('--------------------')

add = lambda x , y : (x+y , x-y)
print(add(34 , 67))

print('--------------------')

my_list = ['kami' , 'sami']
u = []
for i in my_list:
    y = i.upper()
    u.append(y)
print(u)  
print(list(map(str.upper,my_list)))   #wow

print('--------------------')

name = ['korosh' , 'arash']
score = [18 , 15]
print(list(zip(name , score)))
print(list(map(lambda x , y : (x,y) , name , score)))

print('--------------------')

new_list = ['a' , 'c' , 'G' , 'r']
y = []
for i in new_list:
    y.append(ord(i))
print(y)    
print(list(map(ord, new_list)))    

print('--------------------')

a = [5, 8, 9]
b = [4, 3, 2]
print(list(map(lambda x, y : x*y, a, b)))

print('--------------------')

scores = [8, 4, 12, 15, 18, 19, 20]
#print(scores(filter(lambda x : x > 9 , scores)))    wrong
print(list(filter(lambda x: x > 9, scores)))

print('--------------------')

nw = ['radar', 'madam', 'ava', 'sina']
palindrome = lambda x: (x== ''.join(reversed(x)))
print(list(filter(palindrome , nw)))

print('--------------------')

nlist = [8, 4, 2, 3, 6, 5]
nlist.sort()
print(nlist)

print('--------------------')

d = {'raha':12, 'maral':17, 'ziba':19, 'karen':18, 'arash':15}
print(sorted(d.items(), key= lambda x : x[1]))

print('--------------------')

with open ('d:/myfile.txt','w') as myfile:
    line1='hello world\n'
    line2='welcome\n'
    myfile.write(line1)
    myfile.write(line2)

print('--------------------')
with open ('d:/myfile.txt','r') as myfile:
    print(myfile.read())
print('--------------------')

name1='d:/myfile.txt'
name2='d:/newfile.txt'
with open (name1, 'r') as f1 , open(name2, 'w') as f2:
    for line in f1:
        f2.write(line)

import os
m='d:/myfile.txt'
print(os.path.exists(m))
os.remove(m)

lama1='d:/x.txt'
lama2='d:/y.txt'
lama3='d:/z.txt'

with open(lama1, 'w') as f1:
    f1.write('welcome to paris\n')
    f1.write('have a nice day madam\n')
with open(lama2, 'w') as f2:
    f2.write('here you go\n')
    f2.write('do you want to drink a coffee\n')
    f2.write('great idea you are ridiculous\n')

with open (lama1) as f1, open(lama2) as f2:
    da1=f1.read()
    da2=f2.read()

with open(lama3,'w') as f3:
    f3.write(da1+da2)        