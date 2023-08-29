def contador(a,b,c):
    print ("=-"*30)
    aux = a
    bux = b
    if c ==0:
        c=1
    if a>b and c>0:
        c = -c
    if a>b and c<0:
        b-=2

    if c < 0:
        print(f"Contagem de {aux} até {bux} de {-c} em {-c}")
        for x in range (a,b+1,c):
            print (f"{x} ",end='')
    if c > 0:
        print(f"Contagem de {aux} até {bux} de {c} em {c}")
        for x in range (a,b+1,c):
            print (f"{x} ",end='')
    if c ==0:
        print(f"Contagem de {aux} até {bux} de {1} em {1}")
        for x in range (a,b+1,1):
            print (f"{x} ",end='')

    print('FIM!')

contador (1,10,1)
contador(10,0,-2)
print("=-" * 30)
print('Agora é sua vez de personalizar a contagem!')
contador(a=(int(input("Início: "))),b=(int(input("Fim: "))),c=(int(input("Passo: "))))