from AjudandoDoutor import doutorMain
from Calculadora import calculadoraMain
from CalculoBaskara import baskaraMain
from EscolhaRoupa import escolhaRoupa
from Patinete import calculo_velocidadeMedia
from Alimentacao import alimentacaoMain

mensagemInicial = "Olá, seja bem-vindo ao nosso programa!"
mensagemFinal = "Obrigado por usar nosso programa!"
mensagemErro = "Desculpe, não entendi sua resposta. Tente novamente."

def main():
    print(mensagemInicial)
    print('----------------------------------')
    opcao = 0
    
    while opcao != 7:
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
            if opcao < 1 or opcao > 7:
                raise ValueError
        except ValueError:
            print(mensagemErro)
            print('----------------------------------')

        if opcao == 1:
            doutorMain()
        elif opcao == 2:
            calculadoraMain()
        elif opcao == 3:
            baskaraMain()
        elif opcao == 4:
            escolhaRoupa()
        elif opcao == 5:
            calculo_velocidadeMedia()
        elif opcao == 6:
            alimentacaoMain()
        else:
            print(mensagemFinal)
            print('----------------------------------')
            break
        
if __name__ == '__main__':
    main()