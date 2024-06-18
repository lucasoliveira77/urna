def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

# Exemplo de uso
numero = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {numero} é {calcular_fatorial(numero)}")