def area(b,h):
    print("-"*20)
    print(f"A área de um terreno {b} x {h} é {b*h}m².")


print ("Controle de terrenos")
area(float(input('Comprimento (m): ')),float(input('Largura (m): ')))