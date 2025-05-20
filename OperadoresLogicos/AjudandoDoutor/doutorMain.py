def main():
    """
    O doutor Henry Jones Junior estabeleceu uma regra com seus alunos da disciplina de Arqueologia:
    todos os que obtiverem nota maior do que 8,5 na prova semestral serão convidados para uma visita de campo na América do Sul.
    O programa solicita RM, e-mail e nota do aluno, e imprime "ENVIANDO CONVITE" se a nota for maior que 8.5.
    """

    rm = input('Digite o RM do aluno: ')
    email = input('Digite o e-mail do aluno: ')
    nota = float(input('Digite a nota do aluno: '))

    if nota > 8.5:
        print('ENVIANDO CONVITE')
    else:
        print('NOTA INSUFICIENTE')

if __name__ == '__main__':
    main()