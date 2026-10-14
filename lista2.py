#1
nome=input("Digite seu nome: ")
cidade=input("Digite sua cidade: ")
print("Olá, ", nome, "você mora em ", cidade)

#2
numero = float(input("Digite um número: "))
quadrado = numero ** 2
raiz_quadrada = numero ** 0.5
print("O quadrado de", numero, "é", quadrado)
print("A raiz quadrada de", numero, "é", raiz_quadrada)

#3
km = float(input("Digite a distância em quilômetros: "))
metros = km * 1000
print(km, "quilômetros equivalem a", metros, "metros")

#4
C=float(input("Digite a temperatura em Celsius: "))
f= C*33,8
print(C, "celcius equivalem a", f, "fahrenheint")

#5
ano=int(input("qual o ano em que você nasceu?"))
idade= 2030-ano

 #6
idade2 =int(input("qual sua idade, meu caro?"))
if idade2 >=0 <=12:
    print("Você é uma criança")
elif idade2 >=13 and idade2 <=17:
    print("Você é um adolescente")
elif idade2 >=18 <=59:
    print("adulto")
else:
    print("idoso")

 #7
num1=float(input("digite o 1° número:"))
num2=float(input("digite o 2° número:"))
num3=float(input("digite o 3° número:"))
multiplicação= num1*num2*num3
print(multiplicação)

#8
#Peça duas notas e mostre a média final. Se a média for:
média = float(input("Digite a primeira nota: "))
media2 = float(input("Digite a segunda nota: "))
media3 = float(input("Digite a terceira nota: "))
media_final = (média + media2) / 3
if media_final >= 7:
    print("Aprovado com média:", media_final)
elif media_final >= 5 and media_final < 7:
    print("Recuperação com média:", media_final)
else:
    print("Reprovado com média:", media_final)
    