import random

vitórias = 0
derrotas = 0
dinheiro_total = 0
dinheiro_maquina = 0

while True:
    try:
        qtd_deposito = float(input('Vamos jogar. Digite um valor inicial para depositar: '))
        if qtd_deposito > 0:
            break
        else:
            print('\nDigite apenas valores numéricos com centavos divididos por um ponto')
    except ValueError:
        print('\nDigite apenas valores numéricos com centavos divididos por um ponto')

dinheiro_total += qtd_deposito

print(f'\nSeu depósito inicial: {dinheiro_total}')
print('\nO jogo funciona da seguinte maneira, você escolhe jogar e o computador tenta achar uma palavra chave em um banco de dados, se a palavra for achada você ganha, se não você perde...')

def jogo():
    global vitórias, derrotas, dinheiro_total, dinheiro_maquina

    while True:
        try:
            aposta = float(input('\nDigite um valor para apostar: '))
            if aposta > dinheiro_total:
                print(f'\nDinheiro insuficiente, você tem: {dinheiro_total}')
            elif aposta <= 0:
                print('\nAposte um valor maior que zero.')
            else:
                break
        except ValueError:
            print('\nDigite apenas valores numéricos.')

    try:
        perg_rodadas = int(input('\nQuantas rodadas deseja jogar?: '))
    except ValueError:
        print('\nDigite apenas valores inteiros.')
        return True

    rodadas = 0

    while rodadas < perg_rodadas:
        probabilidade = random.random()

        if dinheiro_total >= aposta:
            if probabilidade < 0.55:
                print('Você perdeu :)')
                dinheiro_total -= aposta
                derrotas += 1
                dinheiro_maquina += aposta
            else:
                print('Você ganhou :(')
                dinheiro_total += aposta
                vitórias += 1
                dinheiro_maquina -= aposta
        else:
            break

        rodadas += 1
        print(f'Saldo atual: {dinheiro_total:.2f}\n')

        if dinheiro_total <= 0:
            while True:
                perg_semgrana = input('Sem saldo, deseja depositar ou sair?(D/S): ').strip().lower()
                if perg_semgrana == 'd':
                    try:
                        deposito_pos = float(input('Quanto deseja depositar?: '))
                        if deposito_pos > 0:
                            dinheiro_total += deposito_pos
                            print(f'Depósito efetuado com sucesso, seu saldo: {dinheiro_total}')
                            break
                        else:
                            print('Deposite um valor maior que zero')
                    except ValueError:
                        print('Digite apenas valores numéricos.')
                elif perg_semgrana == 's':
                    return False
                else:
                    print('Digite somente D ou S')

            if dinheiro_total > 0:
                break

    while True:
        perg1 = input('Deseja jogar novamente? (S/N): ').strip().lower()
        if perg1 == 's':
            return True
        elif perg1 == 'n':
            return False
        else:
            print('Digite somente S ou N!')

while True:
    if not jogo():
        print('\nObrigado por jogar!')
        print(f'Seu saldo final: {dinheiro_total}')
        print(f'Total de vitórias: {vitórias} | Total de derrotas: {derrotas} | Total de dinheiro ganhado pelo cassino: {dinheiro_maquina}')
        break
