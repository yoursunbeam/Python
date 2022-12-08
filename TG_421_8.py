import random
ROWS=5
COLS=3
def main():
    values=[[0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0]]
    
    for i in range(ROWS):
        for c in range(COLS):
            values[i][c]=random.randint(1,999)
            
    print(values)
    
main()
