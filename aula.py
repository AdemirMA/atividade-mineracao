def saudacao():
    print("Olá mundo")

#chamando a funcao
saudacao()

def saudacao_personalizada(nome):
    print("Olá, ", nome + "!")

saudacao_personalizada("Maria")

def soma(a, b):
    resultado = a + b
    return resultado
total = soma(3, 5)
print(total)

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro, divisão por zero!"
    else:
        return x / y
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação: ")
print("1. Somar ")
print("2. Subtrair ")
print("3. Multiplicar ")
print("4. Dividir ")

escolha = input("Digite sua escolah (1/2/3/4): ")

if escolha == '1':
    print(num1, "+" , num2, "=", somar(num1, num2))
elif escolha == '2':
    print(num1, "-" , num2, "=", subtrair(num1, num2))
elif escolha == '3':
    print(num1, "*" , num2, "=", multiplicar(num1, num2))
elif escolha == '2':
    print(num1, "/" , num2, "=", dividir(num1, num2))
else: 
    print("Escolha inválida")