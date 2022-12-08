
def main():
    
    ROWS=4
    COLS=2
    x=0
    

    values=[[0,0],
            [0,0],
            [0,0],
            [0,0]]
    
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c]=1*(10**x)
        values[r][c]=2*(10**x)
        x=x+1

    
    


    print(values)

main()


