from fpdf import FPDF



class rl_nfcecupom:
    def __init__(self,Tablewo=None,valortotal=None,dataHora=None): 
       
       
        pdf = FPDF()
        pdf = FPDF('P', 'mm', (100, 220))#coloca tamanho
        pdf.add_page()
        pdf.set_auto_page_break(False)
        pdf.set_font('Arial', '', 8)
        # Tabela com os dados da NFC-e
        pdf.ln(10)
        pdf.cell(25, 10, 'Descrição', 0)
        pdf.cell(25, 10, 'Quantidade', 0)
        pdf.cell(25, 10, 'Valor Unitário', 0)
        pdf.cell(25, 10, 'Valor Total', 0)
        pdf.line(0, pdf.get_y() + 8, 200, pdf.get_y() + 8)
        pdf.ln()        
        for i in range(Tablewo.rowCount()):
            descriçao=(Tablewo.item(i, 1).text())
            qnt=(Tablewo.item(i, 2).text())    
            valorunid=(Tablewo.item(i, 3).text()).replace('R','').replace('$','')
            valort=(Tablewo.item(i, 4).text()).replace('R','').replace('$','')
            pdf.cell(25, 10, f'{descriçao}', 0)
            pdf.cell(25, 10, f'{qnt}', 0)#quantidade
            pdf.cell(25, 10, f'R${valorunid} ', 0)#valor
            pdf.cell(25, 10, f'{valort}', 0)
            pdf.line(0, pdf.get_y() + 8, 200, pdf.get_y() + 8)
            pdf.ln()
       
        pdf.ln(5)
        
        pdf.cell(20, 10, f'Quantidade item', 0, 1, 'C')
        pdf.cell(160, -10, f'00000', 0, 1, 'C')
        pdf.ln(5)
        pdf.cell(10, 10,'Valor Total R$' , 0)
        pdf.cell(140, 10, f'{str(valortotal)}', 25, 2, 'C')
        
        final=(pdf.get_y()+20)  
        pdf.image('C:/Users/User/Documents/GitHub/softhouse/assets/telainicial/qr.png', 25, final, w=50) 
        # Salvando o PDF
        pdf.output('itens.pdf', 'F')

