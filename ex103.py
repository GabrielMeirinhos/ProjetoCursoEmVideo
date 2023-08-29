def ficha(nome,gols=0):
    if nome == "":
        nome = "<desconheido>"
    if not gols.isnumeric():
        gols = 0
    print(f"O jogador {nome.title()} fez {gols} gol(s) no campeonato.")


ficha(input("Nome do jogador: "),input("Número de gols: "))