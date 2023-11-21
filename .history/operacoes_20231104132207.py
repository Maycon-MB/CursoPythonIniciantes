faturamento = 1000
custo = 700

novas_vendas = 300

faturamento = faturamento + novas_vendas # somar
imposto = faturamento * 0.1 # multiplicar
lucro = faturamento - custo - imposto # subtrair

print(faturamento)
print(lucro)
margem_lucro = lucro / faturamento #dividir
print(margem_lucro)

restituicao = imposto * 0.1
print(restituicao)

# Mod  resto da divisão
# 10 % 3
tempo_em_meses = 160
tempo_em_anos = tempo_em_meses / 12
print()