print('Bem vindo ao Sistema de Notas da Escola Vai na Web!')

verifica_repeticao = input('Deseja iniciar a verificação da sua classificação? s/sim n/nao: ')        
while verifica_repeticao == 's' or verifica_repeticao == 'sim':
    
    nota_do_aluno = (int)(input('Por favor, insira a sua nota: '))
    
    if nota_do_aluno >= 90 and nota_do_aluno <= 100:
        print('Parabéns, você tirou A!')
    elif nota_do_aluno >= 80 and nota_do_aluno < 90:
        print('Muito bem, você tirou B.')
    elif nota_do_aluno >= 70 and nota_do_aluno < 80:
        print('Bom trabalho, você tirou C.')
    elif nota_do_aluno >= 60 and nota_do_aluno < 70:
        print('Fique atento, você tirou D.')
    elif nota_do_aluno >= 0 and nota_do_aluno < 60:
        print('Estude um pouco mais, você tirou F.')
    else:
        print('Insira um valor de nota válido.')
        
    verifica_repeticao = input('Deseja continuar? s/sim n/nao: ')        
    