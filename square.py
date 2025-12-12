def area(a):
    '''
    Возвращает площадь квадрата

        Параметр:
            a (float): длина стороны квадрата

        Возвращаемое значение:
            area (float): площадь квадрата
    '''
    if(type(a)!=int and type(a)!=float):
        return -1
    if(a<0):
        return -1
    return a * a


def perimeter(a):
    '''
        Возвращает периметр квадрата

            Параметр:
                a (float): длина стороны квадрата

            Возвращаемое значение:
                perimeter (float): периметр квадрата
    '''
    if(type(a)!=int and type(a)!=float):
        return -1
    if(a<0):
        return -1
    return 4 * a
