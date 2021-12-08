times = ("Athletico-PR", "Fortaleza", "Bragantino", "Palmeiras", "Atlético-MG", "Fluminense", "Bahia", "Atlético-GO","Santos","Flamengo","Corinthians","Ceará","Internacional","Juventude","Sport","Cuiabá","Chapecoense","São Paulo","América-MG","Grêmio")

print(f"\nOs Cinco Primeiros Colocados: {times[0:5]}\n")
print(f"Os 4 Ultimos Colocados: {times[16:]}\n")
print(f"Os Times Em Ordem Alfabetica: {sorted(times)}\n")
chape = times.index("Chapecoense")
sao = times.index("São Paulo")
print(f"A Chapecoense esta na posição: {chape+1}°a Posição\n")
print(f"O São PAulo Esta na posição: {sao+1}\n")
