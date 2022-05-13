produtos = ('Cafe', 18.99, 'Arroz', 15.09, 'Feijao', 06.95, 'Sal', 01.99, 
            'Farinha', 06.85, 'Açucar', 03.99, 'oleo', 08.25, 'Vinagre', 01.99, 
            'Macarrao', 03.99, 'Molho-de-tomate', 01.98, 'Bolacha-recheada', 01.98,
            'Farinha-de-milho', 06.95)
print('-' * 40)
print(f'{"Lista de preços":^40}')
print('-' * 40)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='' )
    else:
        print(f'R$ {produtos[c]:>5}', end='\n')
print('-' * 40)