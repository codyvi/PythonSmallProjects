p = int(input('Dame el multiplicador: '))
msj = input('Dame el string: ')

dec = ''

for x in msj.upper():
    dec += chr( ( ( ( ord(x) - ord('A') ) * p ) % 26) + ord('A') )



print('La respuesta es:', dec.lower())