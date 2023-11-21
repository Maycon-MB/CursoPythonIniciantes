faturamento = 1000
custo = 700

lucro = faturamento - custo

#print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")

#print ("Faturamento: " + str(faturamento) + ", Custo: " + str(custo) + ", Lucro: " + str(lucro))

email = "EMAIL_falso@gmail.com"

#print(email.lower())
#print(email.find("@")) # -1, se não encontrar o elemento. Se encontrar: a posição

posicao = email.find("@")
servidor = email[posicao+1:]
#print(servidor)

# tamanho de um texto
tamanho = len(email)
#print(tamanho)

#trocar um pedaço do texto
email_trocado = email.replace("gmail.com", "hotmail.com")
#print(email_trocado)

nome = "joao lira"
#print(nome.capitalize()) #capitalize põe a primeira palavra do texto em maiúsculo
#print(nome.title()) #title transforma as primeiras letras de cada palavra em maiúsculo

# especiais - formatação numérica
margem = lucro / faturamento
#print(f"Faturamento: R${faturamento:,.2f}\nCusto: {custo}\nLucro: {lucro}") 
#print(f"Margem: {margem:.1%}")

#exercícios
nome = "Maycon Bruno Montes Gomes Constancio"
email = "fakeMaycon@gmail.com"

# descubra o servidor do email
posicao = email.find("@")
servidor = email[posicao+1:]
print(servidor)

# pegar o 1º nome do usuário
primeiro_nome = nome.find("B")
posicao_nome = nome[+1primeiro_nome:]
print(posicao_nome)

# construa uma mensagem: Usuário (nome) cadastro com sucesso com o email X
print(f"Usuário {nome} cadastrado com sucesso com o email {email}")

# construa uma mensagem: Enviamos um link de confirmação para o email f****@gmail.com
print("Enviamos um link de confirmação para o email f****@gmail.com")