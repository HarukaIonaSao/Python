nome = input("Qula é o seu nome?")
print("Prazer em conhecer, {:>20}!".format(nome))
#Nome fica á direita
print("Prazer em conhecer, {:<20}!".format(nome))
#Nome fica à esquerda
print("Prazer em conhecer, {:^20}!".format(nome))
#Nome fica centralizado
print("Prazer em conhecer, {:=^20}!".format(nome))
#Nome fica =====Nome=====


n1 = int(input("Um valor: "))
n2 = int(input("Outro valor:"))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print("A soma é: {}, \n o produto  é: {}  a divisão é : {:.2f} e ".format(s,m,d),end='>>> ')
print("a divisão inteira é : {}".format(di))
print("{} elevado a {} é : {}".format(n1,n2,e))

#É valido adicionar variáveis se formos usar o valor depois
