import random
def MadMax(N, Tele = []):
    num = 0
    index = 0
    try:
        mid = N // 2
    except ZeroDivisionError:
        print("Деление на 0 !!!")
        
    zchange = True 
    while(zchange):
        zchange = False 
        for i in range(N-1):
            if Tele[i] > Tele[i+1]:
                Tele[i], Tele[i+1] = Tele[i+1], Tele[i]
                zchange = True
                
    for i in range(N):
        try:
            if Tele[i] > num:
                num = Tele[i]
                index = i
        except IndexError:
            print("Индекс за пределами массива!")
    Tele[index] = Tele[mid]
    Tele[mid] = num
    
    xchange = True 
    while(xchange):
        xchange = False 
        for i in range(mid):
            if Tele[i] > Tele[i+1]:
                Tele[i], Tele[i+1] = Tele[i+1], Tele[i]
                xchange = True
                
                
    ychange = True
    while(ychange):
        ychange = False
        for j in range(mid+1,N-1):
            if Tele[j] < Tele[j+1]:
                Tele[j], Tele[j+1] = Tele[j+1], Tele[j]
                ychange = True
    return Tele
