def Notas(* Valores, situação=bool):
    """
    :param Valores: Notas Do Aluno
    :param situação: Situação Que O Aluno Se Encontra Com Base Na Sua Média
    :return: Um Dicionario Contendo Tais Informações """
    Dicionario = dict()
    Dicionario['Total'] = len(Valores)
    Dicionario['Maior'] = max(Valores)
    Dicionario['Menor'] = min(Valores)
    Media = f"{sum(Valores) / Dicionario['Total']:.2f}"
    Dicionario['Média'] = float(Media)
    if situação:
        if Dicionario['Média'] > 7:
            Dicionario['Situação'] = 'Boa'
        elif 4 < Dicionario['Média'] < 6:
            Dicionario['Situação'] = 'Razoavel'
        else:
            Dicionario['Situação'] = 'Ruim'

    return Dicionario


Resp = Notas(1.3, 5.6, 8.9, 9.7, 1.3, 5.5)
print(Resp)
