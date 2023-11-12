import locale

# Configurando a localização para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Número inteiro
numero_inteiro = 10

# Convertendo para número real (float)
numero_real = float(numero_inteiro)

# Formatando como dinheiro brasileiro
numero_formatado = locale.currency(numero_real, grouping=True, symbol=None)

# Exibindo o resultado
print(numero_formatado)
