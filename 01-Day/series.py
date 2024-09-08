import pandas as pd

idades = [30, 42, 90, 34]
series_idades = pd.Series(idades)

# Calcula a média das idades:
media_idades = series_idades.mean() 
print("Média das idades:", media_idades)

# Calcula a variância:
series_idades.var()
variancia_idades = series_idades.var()
print(variancia_idades)

# Calcula a mediana:
series_idades.median()
mediana = series_idades.median()
print(mediana)

# Descrição geral
series_idades.describe()
descricao = series_idades.describe()
print(descricao)
