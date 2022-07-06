import re
hand=input('Enter the file name:')
handle=open(hand)
total=0
for line in handle:
     s=re.findall('[0-9]+',line)
     for i in s:
         total+=int(i)
    
print(total)