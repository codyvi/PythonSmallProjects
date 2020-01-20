m = int(input('Dame M: '))
e = int(input('Dame e: '))
n = int(input('Dame n: '))



cipher = ((m**e) % n)

print(cipher)