
def goldenSection(start,end,func,epsilon=1e-4,appendix=False):
    '''Golden Section Method for exact line search'''
 
    if appendix == True:
        start0, end0 = start, end   # save initial search interval
 
    # find two insertion points using fixed ratio
    from math import sqrt
    ratio = sqrt(5) / 2 - 0.5
    intervalLen = end - start
    middleL = start + (1 - ratio) * intervalLen
    middleR = start + ratio * intervalLen
 
    iterNum = 0
    while intervalLen >= epsilon:
        # update start or end point and two insertion points
        if func(middleL) > func(middleR):
            start = middleL
            intervalLen = end - start
            middleL = middleR
            middleR = start + ratio * intervalLen
        else:
            end = middleR
            intervalLen = end - start
            middleR = middleL
            middleL = start + (1 - ratio) * intervalLen
        iterNum += 1
 
    minPoint = (start + end) / 2
    minValue = func(minPoint)
    if appendix == True:
                 print ("Метод: метод золотого сечения \ n")
                 print ("Начальный интервал: [% .2f,% .2f]; Конечный интервал: [% f,% f]"% (start0, end0, start, end))
                 print ("Точка минимального значения:% .4f; Минимальное значение:% .4f; Количество итераций:% d"% (minPoint, minValue, iterNum))
 
    return minPoint, minValue, iterNum