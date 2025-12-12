def area(a,b):
    '''
    Возвращает площадь прямоугольника

        Параметр:
            a (float): длина прямоугольника
            b (float): ширина прямоугольника

        Возвращаемое значение:
            area (float): площадь прямоугольника
    '''
    if(type(a)!=int and type(a)!=float):
        return -1
    if(type(b)!=int and type(b)!=float):
        return -1
    if((a!=0 or b!=0) and (a<=0 or b<=0)):
        return -1
    return a * b


def perimeter(a,b):
    '''
        Возвращает периметр прямоугольника

            Параметр:
                a (float): длина прямоугольника
                b (float): ширина прямоугольника

            Возвращаемое значение:
                perimeter (float): периметр прямоугольника
    '''
    if(type(a)!=int and type(a)!=float):
        return -1
    if(type(b)!=int and type(b)!=float):
        return -1
    if((a!=0 or b!=0) and (a<=0 or b<=0)):
        return -1
    return 2*(a+b)
