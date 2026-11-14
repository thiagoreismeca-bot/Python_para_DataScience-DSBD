# Armazena o preço na Variável 'preco' e substiui vírgula por ponto para conversão float

preco = "350,84"
preco_n = float(preco.replace(',','.'))
print(f'{preco_n}')

