def voto(i=0):
    from datetime import date
    global idade
    data =date.today().year
    idade = data - i
    if idade >=18:
       return (f"Com {idade} anos: voto Obrigatório").upper()
    elif idade>=16 or idade>65:
        return(f"Com {idade} anos: voto Opcional").upper()
    else:
        return(f"Com {idade} anos: Não vota").upper()

x =((int(input("Qual ano que você nasceu: "))))
print(voto(x))