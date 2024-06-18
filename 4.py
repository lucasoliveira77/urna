def converter_para_12h(hora, minuto):
    periodo = 'AM'
    if hora >= 12:
        periodo = 'PM'
        if hora > 12:
            hora -= 12
    if hora == 0:
        hora = 12
    return hora, minuto, periodo

# Exemplo de uso
while True:
    hora = int(input("Digite a hora (formato 24h): "))
    minuto = int(input("Digite os minutos: "))
    
    hora12, minuto, periodo = converter_para_12h(hora, minuto)
    
    print(f"{hora}:{minuto} é {hora12}:{minuto} {periodo}")
    
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break