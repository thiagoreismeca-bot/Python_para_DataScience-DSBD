
# Exemplo 02 - Tipos de prints com os tipos de dados em Python

# Variável para armazenar o nome do aluno

nome_aluno = 'Rocky'  # Declarar variável
idade_aluno = 15      # Variável com a idade do aluno
media_aluno = 8.45    # Declaração de variável média

print('Nome do aluno %s, ele tem %d anos e sua média é %f.' %(nome_aluno,idade_aluno,media_aluno))
print('Nome do aluno %s, ele tem %d anos e sua média é %.2f.' %(nome_aluno, idade_aluno, media_aluno))
print('nome do aluno é {}, ele tem {} anos e sua média é {}.'.format(nome_aluno, idade_aluno, media_aluno))

print(f'Nome do aluno{nome_aluno}, ele tem {idade_aluno} e sua média é {media_aluno:.2f}.')


