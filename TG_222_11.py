
weight=int(input('Введите массу тела '))
print('Месяц\tМасса тела')
for month in range(1,6,1):
    weight=weight-1.5
    print(month,'\t',format(int(weight)))

