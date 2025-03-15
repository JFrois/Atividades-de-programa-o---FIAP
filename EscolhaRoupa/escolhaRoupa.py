'A loja virtual FIAP Wear, que vende roupas personalizadas da instituição, disponibilizou no mês do seu aniversário o cupom NIVER10, que concede 10% de desconto no valor total de uma compra feita no site.'
'Caso o cliente digite o cupom corretamente, deverá ser informado do valor final da compra já com o desconto aplicado. Caso digite o cupom de maneira incorreta, deverá ser informado do valor da compra sem o desconto.Esse problema claramente pede o uso de um if composto! Afinal de contas,temos uma única condição (o cupom digitado ser igual a “NIVER10”) e duas ações, sendo uma para cada resultado da condição.'

#Definição da variável cupom
cupom = 'NIVER10'

#Definição da variável desconto
desconto = 0.9

#Mensagens de agradecimento
mensagemIncial = print("Bem-vindo à FIAP Wear!")
mensagemFinal = ("Obrigado por comprar na FIAP Wear!")

#Solicitação do valor do produto
valorProduto = float(input('Digite o valor do produto: '))

#Solicitação do cupom de desconto
cupomDigitado = input('Digite o cupom de desconto: ').upper()

if cupomDigitado == cupom:
    valorDescontado = valorProduto * desconto
    print(f'Valor final da compra compra com desconto: R${valorDescontado}')
else:
    print(f'O valor da sua compra sem desconto é de R${valorProduto}')
print(mensagemFinal)