f1=open('content.txt','w+')
f1.write('MY NAME IS PYTHON')
f1.seek(0)
data1=f1.readline()
data1=data1.lower()
print(len(data1))
r=data1.split()
s=0
for i in r:
    if i=='python':
        s+=1
print(s)
        
