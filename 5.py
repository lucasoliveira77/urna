import math

def calculadora():
    while True:
        print("Selecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Raiz Quadrada")
        print("6. Potenciação")
        print("0. Sair")
        
        escolha = int(input("Digite sua escolha: "))
        
        if escolha == 0:
            break
        elif escolha == 5:
            numero = float(input("Digite o número para calcular a raiz quadrada: "))
            resultado = math.sqrt(numero)
        elif escolha == 6:
            base = float(input("Digite a base: "))
            expoente = float(input("Digite o expoente: "))
            resultado = base ** expoente
        else:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if escolha == 1:
                resultado = num1 + num2
            elif escolha == 2:
                resultado = num1 - num2
            elif escolha == 3:
                resultado = num1 * num2
            elif escolha == 4:
                if num2 == 0:
                    print("Erro! Divisão por zero.")
                    continue
                resultado = num1 / num2
            else:
                print("Opção inválida.")
                continue
        
        print(f"Resultado: {resultado}\n")
    
# Exemplo de uso
calculadora()