# faturamento = 1000
# custo = 1200

# lucro = faturamento - custo

# if lucro > 0:
#     # Tudo que você quer que aconteça se a condição for verdadeira 
#     print("Lucro:", lucro)
# else:
#     # Tudo que você quer que aconteça se a condição for falsa
#     print("Prejuizo!!!!!")
#     print(lucro)

# produtos = ["iphone", "ipad", "airpod"]
# novo_produto = input("Digite um novo produto:")    
# novo_produto = novo_produto.lower()

# if novo_produto in produtos:
#     print("Produto já cadastrado.")
# else:
#     print("Produto cadastrado com sucesso!")
#     produtos.append(novo_produto)

# print(produtos)

# acima de 15000 -> 500 de bônus
# acima de 10000 -> 150 de bônus
# acima de 5000 -> 50 de bônus

# vendas = 10000

# if vendas > 15000:
#     bonus = 500
# elif vendas > 10000:
#     bonus = 150
# elif vendas > 5000:
#     bonus = 50   
# else:
#     bonus = 0

# print("Bônus:", bonus)

# acima de 15000 -> 500 de bônus
# acima de 10000 -> 150 de bônus
# acima de 5000 -> 50 de bônus
# vendas da empresa > 50000

vendas = 17000
vendas_empresa = 60000
meta_empresa = 50000

if vendas > 15000 and vendas_empresa > meta_empresa:
    bonus = 500
elif vendas > 10000 and vendas_empresa > meta_empresa:
    bonus = 150
elif vendas > 5000 and vendas_empresa > meta_empresa:
    bonus = 50   
else:
    bonus = 0

print("Bônus:", bonus)

# segunda maneira de fazer, só que utilizando if not

if not vendas_empresa > meta_empresa:
    bonus = 0
else:
    if vendas > 15000:
        bonus = 500
    elif vendas > 10000:
        bonus = 150
    elif vendas > 5000:
        bonus = 50
    else:
        bonus = 0       

print("Bônus:", bonus)        

# exercício desafios
# sistema de consulta de preço

precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

input("Digite seu produto:")