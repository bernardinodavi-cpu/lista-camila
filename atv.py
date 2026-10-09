
# ==========================================

# 1
print("Exercicio 1")
for i in range(0,11):
    print(i)

# 2
print("Exercicio 2")
for i in range(1, 11):
    print(i)

# 3
print("Exercicio 3")
for i in range(0, 21, 2):
    print(i)

# 4
print("Exercicio 4")
for i in range(1, 20, 2):
    print(i)

# 5
print("Exercicio 5")
for i in range(10, 0, -1):
    print(i)

# 6
print("Exercicio 6")
for i in range(5, 51, 5):
    print(i)

# 7
print("Exercicio 7")
for i in range(0, 31, 3):
    print(i)

# 8
print("Exercicio 8")
for i in range(100, -1, -10):
    print(i)

# 9
print("Exercicio 9")
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)

# 10
print("Exercicio 10")
soma = 0

for i in range(1, 101):
    soma = soma + i

print("Soma:", soma)

# ==========================================

# 1
print("\nCondicional 1")
numero = float(input("Digite um número: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")


# 2
print("\nCondicional 2")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 > n2:
    print("Maior:", n1)
elif n2 > n1:
    print("Maior:", n2)
else:
    print("Os números são iguais")


# 3
print("\nCondicional 3")
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")


# 4
print("\nCondicional 4")
idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Pode votar")
else:
    print("Não pode votar")


# 5
print("\nCondicional 5")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

print("Média:", media)

if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Em recuperação")
else:
    print("Reprovado")


# 6
print("\nCondicional 6")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 >= n2 and n1 >= n3:
    print("Maior:", n1)
elif n2 >= n1 and n2 >= n3:
    print("Maior:", n2)
else:
    print("Maior:", n3)


# 7
print("\nCondicional 7")
idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 64:
    print("Adulto")
else:
    print("Idoso")


# 8
print("\nCondicional 8")
dia = int(input("Digite um número de 1 a 7: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Dia inválido")


# 9
print("\nCondicional 9")
salario = float(input("Digite o salário: "))

if salario <= 1500:
    salario = salario * 1.15
elif salario <= 3000:
    salario = salario * 1.10
else:
    salario = salario * 1.05

print("Novo salário: R$", round(salario, 2))


# 10
print("\nCondicional 10")
temperatura = float(input("Digite a temperatura: "))

if temperatura < 0:
    print("Congelante")
elif temperatura <= 20:
    print("Frio")
elif temperatura <= 30:
    print("Agradável")
else:
    print("Quente")