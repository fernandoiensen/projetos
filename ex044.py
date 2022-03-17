import random
itens = ('Pedra', 'Papel', 'Tesoura')
com = random.randint(0, 2)
print('''Selecione uma opção! 
[0] Pedra! 
[1] Papel! 
[2] Tesoura! ''')
jog = int(input('Qual a sua jogada? '))
print('O computador escolheu {}'.format(itens[com]))
print('O jogador escolheu {}'.format(itens[jog]))
if com == 0:
    if jog == 0:
        print('Empate! ')
    elif jog == 1:
        print('Jogador Ganhou! ')
    elif jog == 2:
        print('Computador ganhou! ')
    else:
        print('Jogada inválida! ')
elif com == 1:
    if jog == 0:
        print('Computador Ganhou!')
    elif jog == 1:
        print('Empate! ')
    elif jog == 2:
        print('Jogador ganhou! ')
    else:
        print('Jogada inválida! ')
elif com == 2:
    if jog == 0:
        print('Jogador ganhou! ')
    elif jog == 1:
        print('Computador ganhou!')
    elif jog == 2:
        print('Empate!')
    else:
        print('Jogada inválida')