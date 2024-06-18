def caixa_eletronico(valor):
    if valor < 10 or valor > 600:
        print("Valor inválido para saque.")
        return
    
    notas = [100, 50, 10, 5, 1]
    quantidade_notas = []
    
    for nota in notas:
        qtd_notas = valor // nota
        quantidade_notas.append(qtd_notas)
        valor -= qtd_notas * nota
    
    print(f"Notas fornecidas:")
    for i in range(len(notas)):
        if quantidade_notas[i] > 0:
            print(f"{quantidade_notas[i]} nota(s) de {notas[i]} reais")

# Exemplo de uso
saque = int(input("Digite o valor que deseja sacar (entre 10 e 600 reais): "))
caixa_eletronico(saque)