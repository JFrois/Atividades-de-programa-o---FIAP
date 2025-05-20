
def main():
    'O doutor Henry Jones Junior estabeleceu uma regra com seus alunos da disciplina de Arqueologia: todos os que obtiverem nota maior do que 8,5 na sua prova semestral serão convidados para uma visita de campo na América do Sul.'
    'Nosso programa deve solicitar o e-mail e a nota do aluno, exibindo a mensagem “ENVIANDO CONVITE” caso a nota do aluno satisfaça a condição proposta.Utilizando apenas um if simples, podemos resolver esse problema rapidamente! Basta solicitarmos a digitação dos dados, converter a nota para números reais (float) e verificar se ela atende à condição do professor Jones.'

    rm = input('Digite o RM do aluno: ')
    email = input('Digite o e-mail do aluno: ')
    nota = float(input('Digite a nota do aluno: '))

    if nota > 8.5:
        print('ENVIANDO CONVITE')
    else:
        print('NOTA INSUFICIENTE')

if __name__ == '__main__':
    main()