# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3.
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

def soma(x,y):
    return print(x+y)
def subtracao(x,y):
    return print(x-y)
def multiplicacao(x,y):
    return print(x*y)
def divisao(x,y):
    return print(x/y)

print("\n******************* Python Calculator *******************")
print("Selecione a opção desejada: ")
print("[1] Soma ")
print("[2] Subtração ")
print("[3] Multiplicação ")
print("[4] Divisão ")

opcao = input('Digite a operação desejada: ')
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if opcao == "1":
    soma(num1,num2)
elif opcao == "2":
    subtracao(num1,num2)
elif opcao == "3":
    multiplicacao(num1,num2)
elif opcao == "4":
    divisao(num1,num2)
else:
    print("Opção inválida. Tente novamente!")

