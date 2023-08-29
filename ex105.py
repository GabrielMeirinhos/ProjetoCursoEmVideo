def notas (*num,sit=False):
    """
    :param num: Adicione quantas notas forem necessárias para tirar a média;
    :param sit: Opicional, se True mostrará a situação do aluno se não, não;
    :return: Retorna o Boletin do aluno
    Criado por GABRIEL MEIRINHOS B.
    """
    lista=[]
    boletins={}
    for x in num:
        lista.append(x)
    media = 0
    for i in lista:
        media+=i
    boletins = {"maior":max(num),"menor":min(num),"media":f"{media/len(lista):.2f}", "total":len(lista)}
    if sit == True:
        if media > 7:
            boletins["situação"]="Aprovado"
        elif media < 7:
            boletins["situação"]="Reprovado"

    return boletins


print(notas(10,9,7.5,10,9,10,sit=True))
help(notas)