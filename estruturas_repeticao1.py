# Microatividade 3: while

entrada_idade = ''

# O loop continua enquanto entrada_idade for diferente da string '0'
while entrada_idade != '0':
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
    
    # Verifica se não é zero para imprimir, pois se for zero o loop vai acabar
    if entrada_idade != '0':
        print(f'Número digitado: {entrada_idade}')

print("Programa encerrado.")