nome = input("Digite aqui seu nome:")
email = input("Digite aqui seu email:")



# pegar o 1º nome do usuário
posicao = nome.find(" ")
primeiro_nome = nome[:posicao]
print(primeiro_nome)

# construa uma mensagem: Usuário (nome) cadastro com sucesso com o email X
print(f"Usuário {primeiro_nome}cadastrado com sucesso com o email {email}")

# construa uma mensagem: Enviamos um link de confirmação para o email f****@gmail.com
primeira_letra =  email[0]
print(f"Enviamos um link de confirmação para o email {primeira_letra}****{servidor}")