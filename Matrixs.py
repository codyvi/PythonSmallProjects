lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

tmp = 0

Mat = []

for i in range(5):
    a = []
    for j in range(4):
        a.append(lista[tmp])
        tmp += 1
    Mat.append(a)


for i in range(5):
    for j in range(4):
        print(Mat[i][j], end = " ")
    print()