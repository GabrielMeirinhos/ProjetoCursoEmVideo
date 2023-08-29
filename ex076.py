produtos=('Notebook gamer',4399.99,
          'Mouse razer viper',639.32,
          'Teclado redragon',239.90,
          'Fita LED',249,
          'Cesta organizadora',56,
          'Headset kraken',438,
          'Smart Tv Philco',1119.45,
          'Cama box viuva',1484.89,
          'Estante prateleira',397
          'windows',815.99)
print('_\033[1m'*45)
print(f'{"Lista de Compras": ^45}')
print('_'*45)
tot = 0
y = ('Valor total')
for x in range (0,len(produtos)):
    if x%2 ==0:
        print(f"{produtos[x]:.<30}R${produtos[x + 1]: >8.2f}")
    if x%2 !=0:
        tot+=produtos[x]
print('_'*45)
print (f'{y:.<30}R${tot: >8.2f}')
print('_'*45)