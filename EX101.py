from datetime import date

def voto(nascimento):
    ano = date.today().year
    idade = ano - nascimento
    if idade < 16:
        return f'Com {idade} Anos: Não Vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} Anos: Voto Opcinal.'
    else:
        return f'Com {idade} Anos: Voto Obrigatorio.'

print(voto(2000))
