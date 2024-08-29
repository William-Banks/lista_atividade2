# Declaração das três variáveis necessárias para o cálculo dos juros simples a partir do input do usuário
capital = float(input("Digite o capital: "))
taxa = float(input("Digite a taxa de juros mensal: "))
tempo = int(input("Digite o tempo em meses: "))

# Declaração e impressão da variável contendo o cálculo dos juros simples
juros = capital * taxa * tempo
print(f"O valor dos juros simples é: {juros}")