try:
    x=float('abc123')
    print(x)
except IOError:
    print('Этот программный код вызвал ошибку IOError')
except ZeroDivisionError:
    print('Этот программный код вызвал ошибку ZeroDivisionError')
except:
    print('Произошла ошибка')
print('Конец')
