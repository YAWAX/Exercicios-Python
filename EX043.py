#Exercício Python #043 - Índice de Massa Corporal

'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
 mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

#dividindo o peso pela altura elevada ao quadrado

peso = float(input("PESO: "))
altura = float(input("ALTURA: "))
IMC = peso / (altura**2)

if IMC < 18.5:
    print("\033[0;31;40mAbaixo do peso\033[m")
    print("O Seu Imc é {:.1f}".format(IMC))
elif IMC >18.5 and IMC <25:
    print("\033[0;32;40mPeso Ideal\033[m")
    print("O Seu Imc é {:.1f}".format(IMC))

elif IMC > 25 and IMC < 30:
    print("\033[0;33;40mSobre Peso\033[m")
    print("O Seu Imc é {:.1f}".format(IMC))


elif IMC > 30 and IMC < 40:
    print("\033[0;31;40mObesidade\033[m")
    print("O Seu Imc é {:.1f}".format(IMC))

elif IMC > 40 and IMC < 110:
    print("\033[0;31;40mObesidade\033[m")
    print("O Seu Imc é {:.2f}".format(IMC))

else:
    print("OPS ALGO DEU ERRADO TENTE DE NOVO ")
