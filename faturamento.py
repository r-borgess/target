import json

with open('dados.json') as json_file:
    dados = json.load(json_file)

# Cálculo do menor e maior valor de faturamento
valores = [dado['valor'] for dado in dados if dado['valor'] > 0]
menor_faturamento = min(valores)
maior_faturamento = max(valores)

# Cálculo da média mensal de faturamento
soma_faturamento = sum(valores)
num_dias_mes = len(valores)
media_mensal = soma_faturamento / num_dias_mes

# Cálculo do número de dias em que o faturamento diário foi superior à média mensal
dias_acima_media = sum(1 for dado in dados if dado['valor'] > media_mensal)

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias acima da média mensal: {dias_acima_media}")