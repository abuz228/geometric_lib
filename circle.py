import math


def area(r: float)->float:
    '''
    Возвращает площадь окружности

        Параметр:
            r (float): радиус окружности, для которой необходимо вычислить площадь

        Возвращаемое значение:
            area (float): площадь окружности
    '''
    if(type(r)!=int and type(r)!=float):
        return -1;
    if(r<0):
        return -1;
    return math.pi * r * r


def perimeter(r: float)->float:
    '''
    Возвращает длину окружности

        Параметр:
            r (float): радиус окружности, для которой необходимо вычислить периметр

        Возвращаемое значение:
            perimeter (float): периметр окружности
    '''
    if(type(r)!=int and type(r)!=float):
        return -1;
    if(r<0):
        return -1;
    return 2 * math.pi * r

