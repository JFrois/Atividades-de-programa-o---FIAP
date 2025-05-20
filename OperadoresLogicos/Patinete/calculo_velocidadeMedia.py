def main():
    #Nesta atividade precisamos calcular a velocidade média de um patinete.
    #Para isso, precisamos da distância percorrida e do tempo que levou para percorrer essa distância.

    #Variáveis
    mensagemIncial = print("Olá, seja bem-vindo a nossa calculadora de velocidade média!")
    distancia = float(input("Por favor, digite a distancia percorrida em metros: "))
    tempo = float(input("Agora, digite o tempo que levou para percorrer essa distância em segundos: "))

    #Cálculo
    velocidadeMedia = distancia / tempo

    #Saída
    print(f"A velocidade média do patinete foi de {velocidadeMedia:2} m/s")

if __name__ == '__main__':
    main()