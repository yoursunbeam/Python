def text(text):
    infile=open(text,'r')
    text=infile.readlines()
    infile.close()
    text=str(text)
    new_text=text.split()

    myset=set()

    for i in new_text:
        myset.add(i)

    return myset

        

first='text508_3.txt'
second='text509_4.txt'

text1=text(first)
text2=text(second)
total=text1.union(text2)
print('уникальные слова в обоих файлах',total)

inter=text1&text2
print('слова,входящие в оба файла',inter)

diff=text1-text2
print('список слов из 1 файла, не входящие во 2-й',diff)

diff2=text2-text1
print('список слов из 2 файла, не входящие во 1-й',diff2)

sym=text1^text2
print('список слов не содержащиеся одновременно обоих файлах',sym)
