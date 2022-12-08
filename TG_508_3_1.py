codes={'A':'B','a':'b','B':'C','b':'c','C':'D','c':'d','D':'E','d':'e','E':'F','e':'f',
       'F':'G','f':'g','G':'H','g':'h','H':'I','h':'i','I':'J','i':'j','J':'K','j':'k',
       'K':'L','k':'l','L':'M','l':'m','M':'N','m':'n','N':'O','n':'o','O':'P','o':'p',
       'P':'Q','p':'q','Q':'R','q':'r','R':'S','r':'s','S':'T','s':'t','T':'U','t':'u',
       'U':'V','u':'v','V':'W','v':'w','W':'X','w':'x','X':'Y','x':'y','Y':'Z','y':'z',
       'Z':'A','z':'a','.':'@',',':'$','!':'%','?':'*',' ':'+','[':'-',']':'^'}
#создать новый список, прочитать файл в список, преобразовать его в строку
new=[]
infile=open('text508_3.txt','r')
text=infile.readlines()
infile.close()
text=str(text)
print(text)

#зашифровать текст
for i in text:
        value=codes.get(i,'=')
        new.append(value)


#преобразовать в строку из списка       
index=0
new_text=''
while index<len(new):
        num=new[index]
        new_text=new_text+num
        index=index+1
            
print(new_text)        
#записать в файл
outfile=open('text508_3_code.txt','w')
outfile.write(new_text)
outfile.close()

    
