import pandas as pd
import datetime

#Mensagens do sistema
mensagem = 'Olá, seja bem-vindo ao sistema de transações financeiras!'
mensagemErro = 'Desculpe, não entendi sua resposta. Tente novamente.'
mensagemFinal = 'Obrigado por usar nosso sistema de transações financeiras!'
mensagemTransacao = 'Transação realizada com sucesso!'
mensagemErroTransacao = 'Erro ao realizar a transação. Tente novamente.'
mensagemErroValor = 'Valor inválido. Tente novamente.'

#Função para exibição do menu
def menu():
    print(mensagem)
    print('----------------------------------')
    print('Escolha uma opção:')
    print('1 - Adicionar transação')
    print('2 - Exibir extrato')
    print('3 - Sair')
    print('----------------------------------')

#Função principal
def main():
    saldo = 0.0
    transacao = []
    opcao = 0
    
    while opcao != 3:
        menu()
        
        try:
            opcao = int(input('Digite sua opção: '))
            if opcao < 1 or opcao > 3:
                raise ValueError
        except ValueError:
            print(mensagemErro)
            return main()
            
        if opcao == 1:
            adicionar_saldo = float(input('Por favor, digite o seu saldo inicial: '))
            
            if adicionar_saldo < 0:
                    print(mensagemErroValor)
                    return main()
                
            saldo += adicionar_saldo
            valor_transacao = float(input('Digite o valor da transação: '))
            
            if valor_transacao < 0:
                print(mensagemErroTransacao)
                return main()
            
            data_transacao = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            transacao.append(valor_transacao and data_transacao)
            saldo -= valor_transacao
            print(mensagemTransacao)
            
        elif opcao == 2:
                print(f'Extrato: {saldo}')
        
        else:
            print(mensagemFinal)
            break  
    
if __name__ == '__main__':
    main()