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

print()