import os
import xml.dom.minidom

# Pasta contendo os arquivos XML
pasta = 'Autorizadas'

# Lista para armazenar os valores extraídos de todos os arquivos
valores = []

# Iterar sobre os arquivos na pasta
for arquivo in os.listdir(pasta):
    if arquivo.endswith('.xml'):  # Verificar se o arquivo é XML
        caminho_arquivo = os.path.join(pasta, arquivo)  # Caminho completo para o arquivo
        
        # Analisar o arquivo XML
        dom_tree = xml.dom.minidom.parse(caminho_arquivo)
        root = dom_tree.documentElement
        
        # Encontrar o elemento 'valor' e extrair seu texto
        valor = root.getElementsByTagName('vPag')[0].firstChild.nodeValue
        
        # Adicionar o valor à lista de valores
        valores.append(valor)

# Exibir os valores extraídos
soma_valores = 0.0
for i, valor in enumerate(valores, start=1):
    print(f"{valor}")
    total=float(valor)
    soma_valores += total
print(soma_valores)