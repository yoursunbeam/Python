print('Год\tПлата за обучение')
payment=45000
for year in range(1,6,1):
    payment=payment*1.03
    print(year,'\t',format(int(payment)))
