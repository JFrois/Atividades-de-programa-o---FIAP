mensagemInicial = "Olá, seja bem-vindo ao nosso programa: Alimentação"
mensagemFinal = "Obrigado por usar nosso programa!"
mensagemErro = "Desculpe, não entendi sua resposta. Tente novamente."


def escolha():

    print(mensagemInicial)
    opcao = 0
    calorias = []
    item = []
    
    while opcao != 5:
        print("Escolha uma opção:")
        print("1. Café da manhã")
        print("2. Almoço")
        print("3. Jantar")
        print("4. Informações calóricas")
        print("5. Sair")
        
        try:
            opcao = int(input("Digite sua opção: "))
            if opcao < 1 or opcao > 5:
                raise ValueError
        
        except ValueError:
            print(mensagemErro)
            
        if opcao == 1:
            cafedaManha = input('Digite o que você comeu no café da manhã: ')
            item.append(cafedaManha)    
            ccaloriasContador = float(input('Digite a quantidade de calorias: '))
            calorias.append(ccaloriasContador)
        
        elif opcao == 2:
            almoco = input('Digite o que você comeu no almoço: ')
            item.append(almoco)
            caloriasContador = float(input('Digite a quantidade de calorias: '))
            calorias.append(caloriasContador)
        
        elif opcao == 3:
            jantar = input('Digite o que você comeu no jantar: ')
            item.append(jantar)
            caloriasContador = float(input('Digite a quantidade de calorias: '))
            calorias.append(caloriasContador)
        
        elif opcao == 4:
            soma = sum(calorias)
            media = soma / len(calorias) if calorias else 0
            print(f"Aqui estão as informações calóricas: {soma}\nMédia de calorias: {media}\n")
        
        else:
            print(mensagemFinal)
            break

def main():
    escolha()
    
if __name__ == "__main__":
    main()