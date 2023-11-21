faturamento = 1000
custo = 700

lucro = faturamento - custo

#print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")

#print ("Faturamento: " + str(faturamento) + ", Custo: " + str(custo) + ", Lucro: " + str(lucro))

email = "EMAIL_falso@gmail.com"

print(email.lower())
print(email.find("@")) # -1, se não encontrar o elemento. Se encontrar: a posição

posicao = email.find("@")
servidor = email[posicao:]
print(servidor)
nome_email = 
