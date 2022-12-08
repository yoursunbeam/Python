new=''
infile=open('text509_4.txt','r')
text=infile.readlines()
infile.close()
text=str(text)
new_text=text.split()

myset=set()

for i in new_text:
    myset.add(i)
print(myset)

