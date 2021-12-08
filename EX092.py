import datetime
Ficha = dict()

year = datetime.date.today().year
Ficha['Nome'] = str(input("Nome: "))
Ficha['Nascimento'] = (int(input("Ano De Nascimento: ")))
Ficha['CTPS'] = int(input("Carteira De Trabalho: "))

if Ficha['CTPS'] > 0:
    Ficha['Contratação'] = int(input("Ano De Contratação: "))
    Ficha['Salário'] = float(input("Salário: R$ "))
    Ficha['Aposentar'] = (Ficha['Contratação'] - Ficha['Nascimento']) + 35

Ficha['Nascimento'] = year - Ficha['Nascimento']
print()

for k, v in Ficha.items():
    print(f"{k:<10}{v:>10}")
