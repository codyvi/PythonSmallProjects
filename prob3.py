import numpy 

def mismaDiferencia(x):
    arr = numpy.array(x)
    #print(arr)
    arrDiff = numpy.absolute(numpy.diff(arr))
    #print(arrDiff)
    arrDiff = numpy.ceil(arrDiff)
    result = numpy.all(arrDiff == arrDiff[0])
    #print(arrDiff)
    
    if result:
        return True 
    
    return False

print(mismaDiferencia([44, 37, 30, 23 ]))