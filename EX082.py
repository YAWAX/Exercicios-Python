numeros = []
par = []
impar = []
sair = ''
while sair != 'N':
    n = int(input("Valor: "))
    numeros.append(n)
    par.append(n) if n % 2 == 0 else impar.append(n)
    sair = str(input("Deseja Continuar: ")).upper()

print(f"Conteudo Da Lista: {numeros}\nNumeros Pares Da Lista: {par}\nNumeros Impar Da Lista: {impar}")
