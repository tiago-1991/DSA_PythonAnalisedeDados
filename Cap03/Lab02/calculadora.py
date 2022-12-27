#Calculadora em Python

print("************************ Python Calculator ************************")

print("Selecione o número da operação Desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite a opção (1/2/3/4):"))


if opcao == 1:
    um = int(input("Digite o Primeiro Número:"))
    dois = int(input("Digite o Segundo Número:"))
    soma = um+dois
    print("O Resultado é ",soma)

elif opcao == 2:
    um = int(input("Digite o Primeiro Número:"))
    dois = int(input("Digite o Segundo Número:"))
    subtracao = um-dois
    print("O Resultado é ",subtracao)

elif opcao == 3:
    um = int(input("Digite o Primeiro Número:"))
    dois = int(input("Digite o Segundo Número:"))
    mult = um*dois
    print("O Resultado é ",mult)

elif opcao == 4:
    um = int(input("Digite o Primeiro Número:"))
    dois = int(input("Digite o Segundo Número:"))
    divisao = um/dois
    print("O Resultado é ",divisao)

else:
    print("opção inválida")


