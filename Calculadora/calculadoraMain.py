"Primeira atividade:" 
"Criar de forma simplzes uma calculadora que a partir do preenchimento do usuário já realizar as 4 operações matemáticas básica"

#Mensagem inicial de apresentação 
print("Seja bem vindo a calculadora de operações matemáticas básicas!\nA paritr de agora você poderá realizar as 4 operações matemáticas básicas de forma simples e rápida.\n")

#Entrada de dados do usuário
primeiro_valor = float(input("Por favor, digite o primeiro número deseja realizar a operação: "))

segundo_valor = float(input("Por favor, digite o segundo número deseja realizar a operação: "))

#Operações matemáticas
soma = primeiro_valor + segundo_valor
subtracao = primeiro_valor - segundo_valor
multiplicacao = primeiro_valor * segundo_valor
divisao = primeiro_valor / segundo_valor

#Saída de dados
print(f"\nA soma dos valores é: {soma}")
print(f"A subtração dos valores é: {subtracao}")
print(f"A multiplicação dos valores é: {multiplicacao}")
print(f"A divisão dos valores é: {divisao}")