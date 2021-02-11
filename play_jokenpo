import time
import random


def jokenpo():
    print('=-'*15, '\033[1;31mVAMOS JOGAR PEDRA, PAPEL OU TESOURA!\033[m', '=-'*15)
    print('Vai iniciar a contagem!')
    print('\033[1;32mJO...\033[m')
    time.sleep(1.0)
    print('\033[1;32mKEN...\033[m')
    time.sleep(1.0)
    print('\033[1;32mPO!!!\033[m')
    print('=-'*30)
    gesto_escolhido = input('pedra, papel ou tesoura? ').lower()
    gestos = ['pedra', 'papel', 'tesoura']
    gesto_maquina = random.choice(gestos)
    print('A máquina escolheu: \033[1;31m{}!!!\033[m'.format(gesto_maquina.upper()))
    print('=-'*30)
    if gesto_escolhido == 'pedra' and gesto_maquina == 'tesoura':
        print('\033[0;32mVOCÊ VENCEU!\033[m')
    elif gesto_escolhido == 'pedra' and gesto_maquina == 'papel':
        print('\033[1;31mVOCÊ PERDEU!\033[m')
    elif gesto_escolhido == 'pedra' and gesto_maquina == 'pedra':
        print('\033[1;33mEMPATE!\033[m')
    elif gesto_escolhido == 'papel' and gesto_maquina == 'pedra':
        print('\033[0;32mVOCÊ VENCEU!\033[m')
    elif gesto_escolhido == 'papel' and gesto_maquina == 'tesoura':
        print('\033[1;31mVOCÊ PERDEU!\033[m')
    elif gesto_escolhido == 'papel' and gesto_maquina == 'papel':
        print('\033[1;33mEMPATE!\033[m')
    elif gesto_escolhido == 'tesoura' and gesto_maquina == 'papel':
        print('\033[0;32mVOCÊ VENCEU!\033[m')
    elif gesto_escolhido == 'tesoura' and gesto_maquina == 'pedra':
        print('\033[1;31mVOCÊ PERDEU!\033[m')
    elif gesto_escolhido == 'tesoura' and gesto_maquina == 'tesoura':
        print('\033[1;33mEMPATE!\033[m')

    elif gesto_escolhido == 'pedra' and gesto_maquina == 'pedra':
        print('\033[1;33mEMPATE!\033[m')
    else:
        print('INVALIDO')
        jokenpo()
    play_again = str(input('Deseja jogar outra vez? (s/n) '))
    if play_again == 's' or play_again == 'S':
        print('\033[1;32mIniciando novamente...\033[m')
        jokenpo()
    else:
        print('\033[1;31mJogo Encerrado.\033[m')


jokenpo()
