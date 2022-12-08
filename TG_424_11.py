import random

ROWS=3
COLS=3


values=[[0,0,0],
        [0,0,0],
        [0,0,0]]
            
    
for r in range(ROWS):
    for c in range(COLS):
        values[r][c]=random.randint(1,9)
print(values)
                
def main(values):
    a=True
    
    for r in range(ROWS):
        for c in range(COLS):
            if values[r][c]<=9:
                if values[r][c]>=1:
                    a=True
                else:
                    a=False
            else:
                a=False
            
    if a==True:
        print('Таблица содержит значения от 1 до 9')
    else:
        print('Таблица должна содержать значение от 1 до 9')
    
       
    if (values[0][0]+values[1][1]+values[2][2])==15:
        if (values[2][0]+values[1][1]+values[0][2])==15:
            if (values[0][0]+values[0][1]+values[0][2])==15:
                if (values[1][0]+values[1][1]+values[1][2])==15:
                    if (values[2][0]+values[2][1]+values[2][2])==15:
                        a=True
                    else:
                        a=False
                else:
                    a=False
            else:
                a=False
        else:
            a=False
                        
    else:
         a=False
         
    if a==True:
        print('Таблица является магическим квадратом Ло Шу')
    else:
        print('Таблица не является магическим квадратом Ло Шу')
                    
                
            
        
        
main(values)


            
