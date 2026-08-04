import re
txt='python is pr language'
m=re.search('is', txt)
print(m)

m=re.search('hi', txt)
print(m)

m=re.search('^python', txt)      #  ^=starting 
print(m)

m=re.search('language$', txt)     #   $=ending
print(m)

m=re.search('language$', txt)
if (m):
    print('yeah')
else:
    print('nope')    

m=re.search('^pyg', txt)
if (m):
    print('yeah')
else:
    print('nope') 

x='phone number 0211234567 and 0216666666'

print(re.findall('\d+', x))     
print(re.findall('[0-5]+',x))
print(re.findall('[0-1]+',x))

print('-----------------')

fx='Lorem Ipsum is simply dummy text of the printing and ' \
'typesetting industry. name@example.com Lorem Ipsum has been ' \
'the last@gmail.com industrys' \
' standard mana@yahoo.com dummy text ever since '

print(re.findall('\S+@\S+', fx))           #mail finder

print('-----------------')

hx='Ipsum is simply dummy text of the printing and'
print(re.sub('\s',' & ',hx))
print(re.sub('\S',' # ',hx))
print(re.sub('\s',' % ',hx, 5))

nu='021123487659'
print(re.sub('\d','#',nu))
print(re.sub('\D','#',nu))

a='HDJDSBJSDHFGKBKDSD'
b=re.subn('D', 'X',a)
print(b)

print('-------------')
