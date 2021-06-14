import time
velocidade = float(input("Qual foi a velocidade do carro: "))
multa = float(input("Multa em reais: "))
print("ANALISANDO...")
time.sleep(2.5)

if velocidade <= 80:
    print("\033[0;32;40mESTAVA DENTRO DO PERMITIDO\033[m")

if velocidade > 80:
    multaTotal = (velocidade - 80) * multa
    print(f"\033[0;31;40mvocê estava a {velocidade - 80}Km/h acima do permitido, a multa é de R${multaTotal}!\033[m")

