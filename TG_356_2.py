def main():
    infile=open('my_name.txt','r')
    file_contents=infile.read()
    infile.close()
    print(file_contents)

main()
