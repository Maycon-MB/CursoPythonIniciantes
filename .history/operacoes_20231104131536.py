faturamento = 1000
custo = 700

novas_vendas = 300

faturamento = faturamento + novas_vendas
lucro = faturamento - custo
imposto = faturamento * 0.1 # multiplicar
print(faturamento)
print(lucro)
margem_lucro = lucro / faturamento
print(margem_lucro)