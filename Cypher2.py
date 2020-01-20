g = int(input('Dame tu g: '))
n = int(input('Dame tu n: '))
x = int(input('Dane tu x: '))
y = int(input('Dame tu y: '))

b = ((g**x)%n)
a = ((g**y)%n)

Alice = ((a**x)%n)
Bob = ((b**y)%n)

print('Bob ', Bob, 'Alice ', Alice)