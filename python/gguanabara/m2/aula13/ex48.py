soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma do total entre os {} múltiplos de 3, é {} !!!'.format(cont, soma))
