# Declaração das variáveis de distância e combustível gasto a partir do input do usuário
distancia = float(input("Digite a distância percorrida em quilômetros: "))
combustivel = float(input("Digite os litros de combustível gasto: "))

# Declaração da variável de consumo médio a partir da razão entre os valores anteriormente recebidos e impressão na tela
consumo_medio = (distancia / combustivel)
print(f"O consumo médio do veículo é: {consumo_medio} km por litro")