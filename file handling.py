print("hello") 
f=open('test.txt','r') 
print(f.read())


t=open('test.txt','a+')
t.writelines("gagan") 
print(t.read(4)) 
t.seek(4) 
print(t.read(6)) 
print(t.read(10)) 
t.seek(0) 
l=t.readlines() 
for x in l:
 print(l) 
print(t.writable())
