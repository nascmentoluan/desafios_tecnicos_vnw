print('Bem vindo ao Sistema Eleitoral Secreto da   Escola Vai na Web!')

verifica_repeticao = input('Deseja iniciar a verificação? s/sim n/nao: ')        
while verifica_repeticao == 's' or verifica_repeticao == 'sim':
    
    idade_do_aluno = (int)(input('Por favor, insira a sua idade: '))
    
    if idade_do_aluno >= 16:
        print('Parabéns! Você está apto a votar!')
    else:
        print('Você não está apto a votar. Aguarde mais uns(um) ano(s).')
    verifica_repeticao = input('Deseja continuar? s/sim n/nao: ')        
    