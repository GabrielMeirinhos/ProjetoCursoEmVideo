def ajuda():
    print("+="*30)
    print(f"SISTEMA DE AJUDA PyHELP")
    print("+="*30)
    global r
    r = input('Função ou Biblioteca > ')
    if r == "fim":
        return print("FIM")
    print("+="*30)
    return(help(r))


while True:
    ajuda()
    if r == "fim":
        break