
senha_cadastrada = "123456"
email_cadastrado = "usuario@email.com"


max_tentativas = 3

for _ in range(max_tentativas):

    email_usuario = input("Digite seu email: ")
    senha_usuario = input("Digite sua senha: ")


    if email_usuario == email_cadastrado and senha_usuario == senha_cadastrada:
        print("Acesso permitido!")
        break
    else:
        print("Email ou senha incorretos. Tente novamente.")
else:
    print("Limite de tentativas excedido. Conta bloqueada.")