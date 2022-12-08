new=''
infile=open('text509_4.txt','r')
text=infile.readlines()
infile.close()

text2=str(text)
text3=text2.replace(',',' ')
text4=text3.replace('.',' ')
text5=text4.replace('[',' ')
text6=text5.replace(']',' ')
text7=text6.lower()
text8=text7.strip()
text9=text8.rstrip('\n')

new_text=text9.split()
new_text2=str(new_text)

myset=set()
myset2=set([new_text2])


for i in new_text:
    myset.add(i)



myset3=myset2-myset
print(myset2)

