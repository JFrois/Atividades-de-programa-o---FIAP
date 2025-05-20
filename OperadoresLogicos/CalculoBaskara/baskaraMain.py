def main():
    'Transporte-se no tempo e volte para a época de escola! Lembra do dia em que aprendeu a encontrar o valor de X nas equações de 2º grau? Aquelas que tinham uma carinha parecida com Ax² + Bx + C = 0?Aquela fórmula que aprendemos como fórmula de Bhaskara (mas que não foi ele quem criou) deixou saudades (ou pesadelos terríveis).Vamos dar um presente ao seu “eu” do passado e criar um programa no qual o usuário só tenha que escrever os valores de A, B e C e nosso programa vai se encarregar de fazer os cálculos.A primeira etapa que aprendemos na escola é calcular o delta por meio da fórmula: B² - 4 . A . C. Depois, caso o delta seja positivo, existem dois valores para x. Caso seja zero, existe apenas um valor. E caso seja negativo, informamos que não há valor real para x.'

    'Para fazer a verificação de cada uma das condições e, posteriormente, realizar os cálculos necessários, podemos utilizar um desvio condicional encadeado ou utilizar o elif. Vamos dar uma olhada em como ficaria a estrutura em cada um dos casos?'

    'Agora, dentro dos desvios, incluiremos os cálculos de x. A fórmula que aprendemos na escola é 𝑥 =−𝑏±√𝑏2−4𝑎𝑐2𝑎que já calculamos anteriormente., na qual o que está dentro da raiz é o delta E por falar em raiz, cada linguagem de programação possui sua função própria para realizar essa operação. No caso do Python, precisamos importar a classe mathe depois usar a função math.sqrt.Para importar a classe math, escrevemos na primeira linha do nosso script: import math.'

    #Import math
    import math

    #Usuário insere os valores de A, B e C
    A = float(input("Por favor, insira o valor de A: "))
    B = float(input("Por favor, insira o valor de B: "))
    C = float(input("Por favor, insira o valor de C: "))

    #Calculo de delta
    delta = B**2 - 4*A*C
    print(f"O valor de delta é {delta}")

    #Verificação de delta   

    if delta > 0:
        x1 = (-B + math.sqrt(delta)) / (2*A)
        x2 = (-B - math.sqrt(delta)) / (2*A)
        print(f"Os valores de x são {x1} e {x2}")
        
    elif delta == 0:
        x = -B / (2*A)
        print(f"O valor de x é {x}")
        
    else:
        print("Não existe valor real para x")
        
if __name__ == '__main__':
    main()