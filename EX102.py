def fatorial(num, Show=bool):
    """
    Num = Número A Ser fatorado
    Show = Opcional para Mostrar a Conta
    """
    
    
    Valores = list() 
    Valores.clear()
    
    f = 1
    for c in range(num, 0, -1):
        f *= c
        Valores.append(f)   

    if Show == True:
        for r in Valores:
            print(r, end=' x ')

    else:
        print(f)


fatorial(5, False)
fatorial(10, True)
