print('Bem vindo à Escola Vai na Web!')

verificador_de_continuidade = input('Deseja iniciar a avaliação? s-sim n-não: ')        
while verificador_de_continuidade == 's':
    
    nota_do_aluno = (int)(input('Por favor, insira a nota do aluno: '))
    
    if nota_do_aluno >= 6:
        print('O aluno foi aprovado!')
    else:
        print('O aluno foi reprovado.')
    verificador_de_continuidade = input('Deseja continuar? s-sim n-não: ')        
    


