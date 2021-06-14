from math import radians , cos , tan , sin 

angulo = int(input("Digite o angulo que você deseja: "))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tangente = tan(radians(angulo))
print("O ângulo de {} tem seno de {:.2f}".format(angulo , seno))
print("O Angulo de {} tem cosseno de {:.2f}" .format(angulo , cos))
print("O angulo de {} tem tangente de {:.2f}" .format(angulo , tangente))
