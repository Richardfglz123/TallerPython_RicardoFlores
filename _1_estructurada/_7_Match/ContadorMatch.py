import sys
if __name__ == '__main__':
    lista=[1,2,3,5,6,12,45,2,8,4,6,16,10,1,60,1,6,10,4,7,3,10,-1,4,10,1]
    totales=[0,0,0,0,0,0,0,0,0,0]
    adoptados:int=0
    for elemento in lista:
        match elemento:
            case 1: totales[0]+=1
            case 2: totales[1]+=1
            case 3: totales[2]+=1
            case 4: totales[3]+=1
            case 5: totales[4]+=1
            case 6: totales[5]+=1
            case 7: totales[6]+=1
            case 8: totales[7]+=1
            case 9: totales[8]+=1
            case 10: totales[9]+=1
            case _: adoptados +=1

    i:int=1
    for n in totales:
        print(f"{i}.- {n}")
        i+=1
        print(f"Adoptados: {adoptados}")