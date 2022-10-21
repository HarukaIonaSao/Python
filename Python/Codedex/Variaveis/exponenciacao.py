# notação **  score = 2 ** 2

peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua alt: "))
imc = peso / (alt ** 2)
print("O seu IMC é:  {}!".format(imc))
#ou
print(imc)
