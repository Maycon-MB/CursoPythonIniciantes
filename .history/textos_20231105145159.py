faturamento = 1000
custo = 700

lucro = faturamento - custo

#print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")

#print ("Faturamento: " + str(faturamento) + ", Custo: " + str(custo) + ", Lucro: " + str(lucro))

email = "EMAIL_falso@gmail.com"

print(email.lower())
print(email.find("@")) # -1, se não encontrar o elemento. Se encontrar: a posição

posicao = email.find("@")
servidor = email[posicao+1:]
print(servidor)

# tamanho de um texto
tamanho = len(email)
print(tamanho)

#trocar um pedaço do texto
email_trocado = email.replace("gmail.com", "hotmail.com")
print(email_trocado)

nome = "joao lira"
print(nome.capitalize()) #capitalize põe a primeira palavra do texto em maiúsculo
print(nome.title()) #title transforma as primeiras letras de cada palavra em maiúsculo

# especiais - formatação numérica
margem = lucro / faturamento
print(f"Faturamento: R${faturamento:,.2f}\n, Custo: {custo}, Lucro: {lucro}") 
print(f"Margem: {margem:.1%}")