#Tipos primitivos
#int,float,str(string),bool(boolean)

#Crie um programa que que leia dois números e mostre a soma deles

n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
soma = n1 + n2 #vira n1 e n2 não n1+n2

print("A soma entre os números é:", soma)
print("A soma é :{}".format(soma)) #sintaxe do python 3 mais atual

n = input("Digite algo:")
print("O tipo primitivo é:",type(n))
print("Só tem espaços?", n.isspace())
print("É um número?",n.isnumeric())