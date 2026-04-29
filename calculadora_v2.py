"""
Trabalho Prático - DGT2817
Calculadora Refatorada v2
Utiliza funções, estruturas condicionais e de repetição.
"""

#Definição das Funções de Cálculo

def adicao(num1, num2):
    """Realiza a soma de dois números."""
    return num1 + num2

def subracao(num1, num2):
    """Realiza a subtração de dois números."""
    return num1 - num2

def multiplicacao(num1, num2):
    """Realiza a multiplicação de dois números."""
    return num1 * num2

def divisao(num1, num2):
    """Realiza a divisão de dois números, tratando erro de divisão por zero."""
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2

#Função Principal da Calculadora

def calculadora(num1, num2, operacao):
    """
    Recebe dois números e uma operação (símbolo ou nome).
    Chama a função correspondente e retorna o resultado.
    """
    #Normaliza a operação para minúsculas para facilitar a comparação
    op = operacao.lower()
    
    resultado = 0
    
    #Estrutura condicional para identificar a operação desejada
    if op == '+' or op == 'adicao' or op == 'soma':
        resultado = adicao(num1, num2)
    elif op == '-' or op == 'subtracao' or op == 'sub':
        resultado = subracao(num1, num2)
    elif op == '*' or op == 'x' or op == 'multiplicacao' or op == 'mult':
        resultado = multiplicacao(num1, num2)
    elif op == '/' or op == 'divisao' or op == 'div':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida! Use +, -, *, / ou os nomes das operações."
        
    return resultado

#Execução do Programa Loop Principal

def main():
    saida = ''
    
    print("=== CALCULADORA PYTHON v2 ===")
    print("Seja bem vindo a matemática básica!")
    print("Operações aceitas: + (adição), - (subtração), * (multiplicação), / (divisão)")
    print("Ou digite os nomes: adicao, subtracao, multiplicacao, divisao")
    print("Digite 'n' ou 'N' para sair.\n")

    #Laço while: executa enquanto a variável 'saida' for diferente de 'n'
    while saida.lower() != 'n':
        try:
            #Entrada de dados
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            op = input("Digite a operação desejada (+, -, *, /): ")
            
            #Chama a função calculadora e armazena o retorno
            resultado = calculadora(n1, n2, op)
            
            #Saída de dados
            print(f"Resultado da operação: {resultado}")
            
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            
        print("-" * 30)
        #Pergunta se deseja continuar
        saida = input("Deseja realizar outra operação? (S/N): ")
        print("\n")

    print("Programa encerrado. Obrigado por usar!")

#Ponto de entrada do script
if __name__ == "__main__":
    main()