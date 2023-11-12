from fpdf import FPDF
import locale


class geranfce:
    def __init__(self,*args): 
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        self.objeto=args
        pdf = FPDF()
        iten=(self.objeto[0].rowCount()-22+1)
        valor=300
        # Loop para realizar as somas
        for _ in range(iten):
            valor += 8.1
        print(iten,valor) 
        pdf = FPDF('P', 'mm', (105,valor))#coloca tamanho
        pdf.add_page()
        print(pdf.get_y())
        pdf.set_auto_page_break(False)
        ##########
        pdf.image('icone/pdv.png', x=5, y=pdf.get_y()-13, w=25)
        pdf.set_font('Arial', '', 10)
        pdf.cell(25)
        pdf.cell(75, 5, 'EMPRESSA: SISTEM WILLOW',ln=True,align='L')
        pdf.cell(25)
        pdf.cell(65, 5, 'CNPJ:0000000000000',ln=True,align='L')
        pdf.cell(25)
        pdf.cell(65, 5, 'IE:000000000000000',ln=True,align='L')
        pdf.cell(25)
        pdf.cell(65, 5, 'END:RUA DO PIONEIRO',ln=True,align='L')
        pdf.cell(25)
        pdf.cell(65, 5, 'CIDADE:SAO PAULO',ln=True,align='L')
        pdf.cell(25)
        pdf.cell(65, 5, 'TEL:(69)9270-2408',ln=True,align='L')
        pdf.ln(6)#cabeçari
        ##########
        pdf.set_font('Arial', '', 10)
        pdf.cell(25, 6, 'DESCRIÇAO', 0, 0, 'L')
        pdf.cell(25, 6, 'QTD:', 0, 0, 'L')
        pdf.cell(25, 6, 'VL Unid:', 0, 0, 'L')
        pdf.cell(25, 6, 'Vl Total:', 0, 0, 'L')
        pdf.line(0, pdf.get_y() + 8, 200, pdf.get_y() + 8)
        pdf.ln()
        pdf.set_font('Arial', '', 8) 
       
        totalvlitens=0#soma quantidade veze valor preco unitario
      
        for i in range(self.objeto[0].rowCount()):#essa opçapega quantidade iten linha
            codbarra=self.objeto[0].item(i, 0).text()#codbarra
            descricao=self.objeto[0].item(i, 1).text()#descricao
            qtitensvenda=float(self.objeto[0].item(i, 2).text())#quantidade
            unid=self.objeto[0].item(i, 3).text()#unidade
            prunitario=float(str(self.objeto[0].item(i, 4).text()).replace('R', '').replace('$', ''))#preco unitario
            
            total=self.objeto[0].item(i, 5).text()#total

            totalvlitens+=float(qtitensvenda*prunitario)#somavalores  
            pdf.cell(30, 8, str(f'{descricao}'[0:22]), 0)#descricao
            pdf.cell(25, 8, str(f'{qtitensvenda}'), 0)#quantidade
            pdf.cell(20, 8, str(f'{prunitario}'), 0)
            pdf.cell(15, 8, str(f'{total}'), 0)
            pdf.line(0, pdf.get_y() + 8, 200, pdf.get_y() + 8)
            pdf.ln()
       
        pdf.set_font('Arial', '', 10)
        pdf.set_y(-80)
        pdf.cell(80, 5, 'QTD. TOTAL DE ITENS',pdf.page_no(),ln=True,align='L')
        pdf.cell(80, -5, f"{('{:.3f}'.format(self.objeto[0].rowCount()))}",pdf.page_no(), ln=True, align='R')
        pdf.ln(5)
        pdf.cell(80, 5, f'SUBTOTAL R$',pdf.page_no(),ln=True,align='L')
        pdf.cell(80, -5, "0000",pdf.page_no(), ln=True, align='R')
        pdf.ln(5)
        pdf.cell(80, 5, f'VALOR DESCONTO R$',ln=True,align='L')
        pdf.cell(80, -5, "0000",pdf.page_no() , ln=True, align='R')
        pdf.ln(5)
        pdf.cell(80, 5, f'VALOR TOTAL R$',pdf.page_no(),ln=True,align='L')
        pdf.cell(80, -5, f"{ locale.currency(totalvlitens, grouping=True, symbol=None)}",pdf.page_no(), ln=True, align='R')
        pdf.ln(5)
        pdf.cell(30, 5, f'TROCO R$',pdf.page_no(),ln=True,align='L')
        pdf.cell(80, -5, "0000",pdf.page_no(), ln=True, align='R')
        pdf.ln(5)
        pdf.cell(80, 5, f'VENDEDOR: ',pdf.page_no(),ln=True,align='L')
        pdf.cell(80, -5, "0000",pdf.page_no(), ln=True, align='R')
        
        pdf.ln()
        pdf.set_y(-20)
        pdf.image('icone/qrnfce.png', 25, pdf.get_y()-30, 50)
        

        pdf.output("relatoriopdv/pdvpdf/nfce.pdf")

    
