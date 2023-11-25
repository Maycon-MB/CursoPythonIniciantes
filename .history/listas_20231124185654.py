vendas = [100, 50, 130, 80, 120, 200]

print(vendas[-1]) # sempre que usamos a posição -1, será considerado o último conteúdo da lista, -2 o penúltimo, e assim sucessivamente

total_vendas = sum(vendas) # sum basicamente é a fórmula de soma padrão do python
print(total_vendas)
quantidade = len(vendas)
print(quantidade)
valor_max = max(vendas) 
valor_min = min(vendas)
print(valor_max, valor_min) 

posicao = vendas.index(130)
print(posicao)
print(vendas[2:])

produtos = ["iphone", "ipad", "airpod"]
precos = [4000, 8000, 2000]

#edita um item
print("iphone" in produtos)
precos[0] = precos[0] * 1.1
print(precos)

#adiciona um item com append
produtos.append("macbook")
precos.append(10000)
print(produtos)
print(precos)

#remover um item, tanto pelo nome (exemplo "macbook") quanto pela posição (posição -1 por exemplo, a última da lista)
produtos.remove("macbook")
precos.pop(-1)
print(produtos)
print(precos)