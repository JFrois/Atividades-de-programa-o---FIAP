from AjudandoDoutor import doutorMain
from Calculadora import calculadoraMain
from CalculoBaskara import baskaraMain
from EscolhaRoupa import escolhaRoupa
from Patinete import calculo_velocidadeMedia

def main():
    print('Escolha uma opção:')
    print('1 - Ajudando doutor')
    print('2 - Calculadora')
    print('3 - Calculo baskara')
    print('4 - Escolha roupa')
    print('5 - Patinete')
    
    try:
        opcao = int(input('Opção: '))
    except ValueError:
        print('Por favor, insira um número válido.')
        return

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
    else:
        print('Opção inválida!')

if __name__ == '__main__':
    main()