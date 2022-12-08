codes={'B':'A','b':'a','C':'B','c':'b','D':'C','d':'c','E':'D','e':'d','F':'E','f':'e',
       'G':'F','g':'f','H':'G','h':'g','I':'H','i':'h','J':'I','j':'i','K':'J','k':'j',
       'L':'K','l':'k','M':'L','m':'l','N':'M','n':'m','O':'N','o':'n','P':'O','p':'o',
       'Q':'P','q':'p','R':'Q','r':'q','S':'R','s':'r','T':'S','t':'s','U':'T','u':'t',
       'V':'U','v':'u','W':'V','w':'v','X':'W','x':'w','Y':'X','y':'x','Z':'Y','z':'y',
       'A':'Z','a':'z','@':'.','$':',','%':'!','*':'?','+':' ','-':'[','^':']'}
#создать новый список, прочитать файл в список, преобразовать его в строку
new=[]
infile=open('text508_3_code.txt','r')
text=infile.readlines()
infile.close()
text=str(text)
print(text)

#расшифровать текст
for i in text:
        value=codes.get(i,' ' )
        new.append(value)




#преобразовать в строку из списка       
index=0
new_text=''
while index<len(new):
        num=new[index]
        new_text=new_text+num
        index=index+1
            
print(new_text)        
