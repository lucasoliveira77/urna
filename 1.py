def contar_votos():
    total_eleitores = int(input("Digite o número total de eleitores: "))
    
    votos_candidato1 = 0
    votos_candidato2 = 0
    votos_candidato3 = 0
    
    for eleitor in range(total_eleitores):
        voto = int(input(f"Voto do eleitor {eleitor + 1} (1, 2 ou 3): "))
        if voto == 1:
            votos_candidato1 += 1
        elif voto == 2:
            votos_candidato2 += 1
        elif voto == 3:
            votos_candidato3 += 1
    
    print(f"Resultado da eleição:")
    print(f"Candidato 1: {votos_candidato1} votos")
    print(f"Candidato 2: {votos_candidato2} votos")
    print(f"Candidato 3: {votos_candidato3} votos")

# Exemplo de uso
contar_votos()
)