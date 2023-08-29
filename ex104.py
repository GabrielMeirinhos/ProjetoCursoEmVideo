def leiaint(num=0):
    while True:
        if num.isnumeric():
            break
        else:
            print("ERRO! Digite um número válido.")
            num=input("Digite um número: ")
    return num
while True:
    try:
        n=leiaint(input("Digite um número: "))
        print(f"Você acabou de digitar o número {n}.")
        break
    except:
        print("ERRO!")