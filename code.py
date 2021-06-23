import os

lists = os.listdir()

#print(lists)
txt_list= [x for x in lists if x.endswith('.txt')]
print(txt_list)
a=0
b=0
c=0
d=0
e=0
for i in range(len(txt_list)):
    with open(txt_list[i],'r') as f:
        s=f.readlines()
        #print(s)
        #print(len(s))
        for k in s:
            if k[0]=='0':
                a+=1
            elif k[0]=='1':
                b+=1
            elif k[0]=='2':
                c+=1
            elif k[0]=='3':
                d+=1
            else:# s[i][0]==4:
                e+=1

        #print(s)
        #print(len(s))
print(a,b,c,d,e)



