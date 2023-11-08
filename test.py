import xml.etree.ElementTree as ET

# Crie o elemento raiz
root = ET.Element("nfeProc ")

# Crie os elementos necessários para a NFC-e, como identificação, data, etc.
identificacao = ET.SubElement(root, """nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00" """)
NFesite  = ET.SubElement(root, """NFe xmlns='http://www.portalfiscal.inf.br/nfe' """)
infNFe   = ET.SubElement(root, """infNFe versao="4.00" Id="NFe11230907895850000144650010000085739120330931" """)
# Adicione mais informações conforme necessário

# Crie o elemento "Itens" para a lista de itens
itens = ET.SubElement(root, "Itens")

# Crie 20 itens
for i in range(1, 21):
    item = ET.SubElement(itens, "Item")
    ET.SubElement(item, "Descricao").text = f"Item {i}"
    ET.SubElement(item, "Quantidade").text = "1.0"
    ET.SubElement(item, "ValorUnitario").text = f"{10.0 * i:.2f}"
    # Adicione mais informações dos itens conforme necessário

# Crie o objeto ElementTree
tree = ET.ElementTree(root)

# Salve o XML em um arquivo
with open("nfce.xml", "wb") as file:
    tree.write(file)

print("Arquivo XML gerado com sucesso.")
