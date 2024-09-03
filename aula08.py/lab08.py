...
lista = []

nome1 = input('Digite um nome: ')
lista.append(nome1)

nome2 = input('Digite um nome: ')
lista.append(nome2)

lista.sort()

if nome1 in list:
    print(f'Sim, o {nome1}  está adicionado na lista')
else: 
    print('Não, o {nome2} não está na lista')    
...
print(30*'-', ' BOLETIM ESCOLAR ',20*'-')

