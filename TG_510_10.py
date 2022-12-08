X2QQQQQwk
infile=open('text509_4.txt','r')
line=infile.readline()
while line!='':
    line=infile.readline()
    line=line.rstrip('\n')
    line=infile.readline()
infile.close()

text=str(line)
new_text=text.split()
print(new_text)

myset=set()

for i in new_text:
    myset.add(i)
print(myset)

total=0
dict1=dict.fromkeys(myset,[])

infile=open('text509_4.txt','r')
line=infile.readline()
while line!='':
    line=infile.readline()
    total=total+1
    line=infile.readline()
            
infile.close()
print(total)

