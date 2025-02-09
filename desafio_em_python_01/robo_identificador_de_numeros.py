print("Bem vindo ao RobC4 somador da Escola Vai na Web!")

verifica_repeticao = input("Deseja iniciar a operaC'C#o? s/sim n/nao: ")
while verifica_repeticao == "s" or verifica_repeticao == "sim":

    valor_01 = (int)(input("Por favor, insira o primeiro valor: "))
    valor_02 = (int)(input("Por favor, insira o segundo valor: "))

    soma = valor_01 + valor_02
    print(f"O valor da soma entre {valor_01} e {valor_02} C) igual a {soma}.")

    verifica_repeticao = input("Deseja continuar? s/sim n/nao: ")
