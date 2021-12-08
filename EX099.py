def maior(* num):
    print("—"*30)
    
    if len(num) > 0:
        print(f"Foram Informados {len(num)}")
        print(f'Valores Recebidos: {num} \nMaior Valor Passado: {max(num)}')

    else:
        print("Nenhum Valor Foi Informado")
        print("—"*30)
    
    print()

#Programa Principal
maior(9, 2, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 1011)
maior()
