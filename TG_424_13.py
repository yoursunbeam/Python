
import random
def main():
    question=input('Задайте волшебному шару вопрос ')
    infile=open('ball_responses.txt','r')
    words=infile.readlines()
    
    infile.close()
    index=0
    while index<len(words):
        words[index]=words[index].rstrip('\n')
        index=index+1
    again='д'
    while again=='д':
        index=random.randint(0,11)
        print(words[index])
        again=input('Если хотите сыграть еще раз,нажмите д ')
        if again=='д':
            question=input('Задайте волшебному шару вопрос ')
        else:
            print('goodbye')
    

main()
