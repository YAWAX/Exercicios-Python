print('-='*20)
print("Analisador de Triangulos")
print('-='*20)

r1 = float(input("Digite o comprimento de uma reta : "))
r2 = float(input("Digite o comprimento de uma reta : "))
r3 = float(input("Digite o comprimento de uma reta : "))

#Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor
# que a soma das medidas dos outros dois 

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("È POSSIVEL FORMAR UM TRIANGULO: ")

else:
    print("Não È Possivel formar um triangulo: ")
