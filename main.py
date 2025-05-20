from OperadoresLogicos import *
import OperadoresLogicos.AjudandoDoutor as doutorMain
import OperadoresLogicos.Calculadora as calculadoraMain
import OperadoresLogicos.CalculoBaskara as baskaraMain
import OperadoresLogicos.EscolhaRoupa as escolhaRoupa
import OperadoresLogicos.Patinete as calculo_velocidadeMedia
from Lacos_For_and_While import *
import Lacos_For_and_While.Alimentacao as alimentacaoMain

mensagemInicial = "Olá, seja bem-vindo ao nosso programa!"
mensagemFinal = "Obrigado por usar nosso programa!"
mensagemErro = "Desculpe, não entendi sua resposta. Tente novamente."

def menu():
    while True:
        print('Escolha uma opção:')
        print('1 - Ajudando doutor')
        print('2 - Calculadora')
        print('3 - Calculo baskara')
        print('4 - Escolha roupa')
        print('5 - Patinete')
        print('6 - Alimentação')
        print('7 - Sair')
        
        try:
            opcao = int(input('Digite sua opção: '))
            if 1 <= opcao <= 7:
                return opcao
            else:
                raise ValueError
        except ValueError:
            print(mensagemErro)
            print('----------------------------------')

def main():
    print(mensagemInicial)
    print('----------------------------------')

    while True:
        opcao = menu()
        if opcao == 7:
            print(mensagemFinal)
            print('----------------------------------')
            break
        elif opcao == 1:
            doutorMain.main()
        elif opcao == 2:
            calculadoraMain.main()
        elif opcao == 3:
            baskaraMain.main()
        elif opcao == 4:
            escolhaRoupa.main()
        elif opcao == 5:
            calculo_velocidadeMedia.main()
        elif opcao == 6:
            alimentacaoMain.main()

if __name__ == '__main__':
    main()
