def maior(lst):
    pos = aux = 0
    while pos < len(lst):
        for i,v in enumerate(lst):
            if i == 0 :
                aux = v
            elif aux < v:
                aux = v
        pos+=1
    print("-="*30)
    print("Analisando os valores passados...")
    for i,v in enumerate(lst):
            print(f'{v}',end=" ")
    print(f'Foram informados {len(lst)} valores ao todo.')
    print(f'o maior valor foi {aux}')

maior([2,9,4,5,7,1])
maior ([0,4,7])
maior([1,2])
maior([6])
maior([])