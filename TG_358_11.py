def main():
    file=open('web-page.html','w')
    print('Введите имя пользователя и его характеристику')
    name=input('Имя: ')
    spec=input('Описание: ')

    file.write('<html>'+'\n')
    file.write('<head>'+'\n')
    file.write('</head>'+'\n')
    file.write('<body>'+'\n')
    file.write(''+'<center>'+'\n')
    file.write(''+'<h1>')
    file.write(name)
    file.write('</h1>'+'\n')
    file.write(''+'</center>'+'\n')
    file.write(''+'<hr />'+'\n')
    file.write('')
    file.write(spec+'\n')
    file.write(''+'<hr />'+'\n')
    file.write('</body>'+'\n')
    file.write('</html>'+'\n')

    file.close()
    print('Данные сохранены в файл web-page.html')
main()


    
