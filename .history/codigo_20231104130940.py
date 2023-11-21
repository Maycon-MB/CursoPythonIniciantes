faturamento = 1200 # numero inteiro -> int
custo = 770

novas_vendas = 300
faturamento = faturamento + novas_vendas

taxa_imposto = 0.1 # numero decimal
mensagem = "O faturamento foi de 1000" # string = texto
teve_lucro = False #boolean

imposto = taxa_imposto * faturamento

print("Faturamento", faturamento)
print("Custo", custo)
print("Lucro", faturamento - custo - imposto)
print(mensagem, )