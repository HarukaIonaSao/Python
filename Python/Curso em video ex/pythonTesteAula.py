n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
s = n1 + n2
#print("A soma entre",n1," e ", n2, " é: ", s)
print("A soma entre {} e {} é {}".format(n1,n2,s) )

#parte 2 
#n3 = float(input("Digite um número: "))

n4 =input("Digite um valor: ")
print(type(n4))
print(n4.isnumeric())
print(n4.isalpha())#letra
print(n4.isalnum())#alfanumérico
print(n4.isupper())#uppercase
print(n4.isdigit())
print(n4.isdecimal())
print(n4.isdigit())
print(n4.islower())
print(n4.isprintable())
print(n4.isspace())