print("Bem vindo ao Cofre Secreto da Escola Vai na Web!")

verificador_senha = (input("Por favor, insira a senha: "))
while verificador_senha != "Python123":

    print('A senha está incorreta. Tente novamente.')
    verificador_senha = (input("Insira a senha: "))

print('A senha está correta! Acesso liberado!')