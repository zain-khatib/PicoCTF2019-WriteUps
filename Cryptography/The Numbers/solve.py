

a=[16,9,3,15,3,20,6,'{',20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,'}']

data=''
for num in a:
    if type(num) is int:
        data+=chr(ord('a')+num-1)
    else:
        data+=num

with open('flag.txt','w') as f:
    f.write(data)        

