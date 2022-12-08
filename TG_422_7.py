right=['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']

def main():
    file=open('student_solution.txt','r')
    answers=file.readlines()
    file.close()
    index=0
    while index<len(answers):
        answers[index]=answers[index].rstrip('\n')
        index+=1
        
    print(answers)
    
    totalright=0
    totalwrong=0
  
    wrong=[]
    questions=[]
    
    for i in range(len(right)):
        if right[i]==answers[i]:
           totalright= totalright+1
        else:
            item=answers.index(i)
            item=item+1
            questions.append(item)
            totalwrong=totalwrong+1
            wrong.append(answers[i])
            
            
            
    if totalright>=15:
        print('Поздравляем! Экзамен сдан успешно!')
    else:
        print('К сожалению, Вы не сдали экзамен')

    print('количество правильных ответов=',totalright)
    print('количество неправильных ответов=',totalwrong)
    print('номера неправильных ответов:',questions)
    
            
            
        
        
    
    


main()
