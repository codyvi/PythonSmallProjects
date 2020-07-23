def contiene(x,y,z):
    counter = 0
    for i in x:
        if y == i:
            counter += 1
        if counter == z:
            return True
    return False


arreglo = [4, 5, 2, 4, 5, 9, 9, 4, 4]

print(contiene(arreglo,9,2))