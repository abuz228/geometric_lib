def area(a, h):
    '''
    Возвращает площадь треугольника

        Параметры:
            a (float): длина одной из сторон треугольника \n
            h (float): длина высоты треугольника проведенная к стороне a

        Возвращаемое значение:
            s (float): площадь треугольника
    '''
    if(type(a)!=int and type(a)!=float):
        return -1;
    if(type(h)!=int and type(h)!=float):
        return -1;
    if((a!=0 or h!=0) and (a<=0 or h<=0)):
        return -1;
    return a * h / 2

def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника

        Параметры:
            a (float): длина одной из сторон треугольника \n
            b (float): длина второй стороны треугольника \n
            c (float): длина третьей стороны треугольника
        Возвращаемое значение:
            p (float): периметр треугольника
    '''
    if(type(a)!=int and type(a)!=float):
        return -1;
    if(type(b)!=int and type(b)!=float):
        return -1;
    if(type(c)!=int and type(c)!=float):
        return -1;
    if((a!=0 or b!=0 or c!=0) and (a<=0 or b<=0 or c<=0)):
        return -1;

    return a + b + c
