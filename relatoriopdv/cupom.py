from fpdf import FPDF
import locale


class geranfce:
    def __init__(self,*args): 
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        self.objeto=args
  
        pdf = FPDF()
        iten=(self.objeto[0].rowCount()-9+1)
        valor=300
        # Loop para realizar as somas
        for _ in range(iten):
            valor += 8.1
        pdf = FPDF('P', 'mm', (105,valor))#coloca tamanho
        pdf.add_page()
        pdf.set_auto_page_break(False)
        ##########
        pdf.image('icone/pdv.png', x=5, y=pdf.get_y()-13, w=25)
        pdf.set_font('Arial', '', 10)
        pdf.cell(25)#move para lado
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
        pdf.ln(7)#cabeçari
        ##########
        pdf.set_font('Arial', '', 10)
        pdf.cell(-7)
        pdf.cell(35, 6, 'DESCRIÇAO', 1, 0, 'L')
        pdf.cell(15, 6, 'QTD:', 1, 0, 'L')
        pdf.cell(25, 6, 'VL Unid:', 1, 0, 'L')
        pdf.cell(25, 6, 'Vl Total:', 1, 0, 'L')
  
        pdf.ln(9)
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
            pdf.cell(-7)
            pdf.cell(30, 8, str(f'{descricao}'[0:40]),0)#descricao
            pdf.cell(1)
            pdf.cell(25, 8, str(f'{qtitensvenda}'),0,0,'C')#quantidade
            pdf.cell(1)
            pdf.cell(20, 8, str(f'R$ {prunitario}'),0,0,'C')
            pdf.cell(1)
            pdf.cell(15, 8, str(f'{total}'),0,0,'C')
            pdf.line(0, pdf.get_y() + 8, 200, pdf.get_y() + 8)
            pdf.ln()
    
        pdf.set_y(-168)
        pdf.set_font('Arial', '', 10)
        pdf.cell(80, 5, 'QTD. TOTAL DE ITENS',0,ln=True,align='L')
        pdf.cell(80, -5, f"{('{:.3f}'.format(self.objeto[0].rowCount()))}",0, ln=True, align='R')
        pdf.ln(5)
        pdf.cell(80, 5, f'SUBTOTAL R$',0,ln=True,align='L')
        pdf.cell(80, -5, "0000", ln=True, align='R')
        pdf.ln(5)
        pdf.cell(80, 5, f'VALOR DESCONTO R$',0,ln=True,align='L')
        pdf.cell(80, -5, "0000",0, ln=True, align='R')
        pdf.ln(5)
        pdf.cell(80, 5, f'VALOR TOTAL R$',0,ln=True,align='L')
        pdf.cell(80, -5, f"{ locale.currency(totalvlitens, grouping=True, symbol=None)}", ln=True, align='R')
        pdf.ln(5)
        pdf.cell(30, 5, f'TROCO R$',ln=True,align='L')
        pdf.cell(80, -5, "0000",0 ,ln=True, align='R')
        pdf.ln(5)
        pdf.cell(80, 5, f'VENDEDOR: WILLOW PINTO DIAS ',ln=True,align='L')
        pdf.cell(80, 5, f'FORMA PAGAMENTO ',ln=True,align='L')
        b=str([i for i in self.objeto[1]]).replace("'","").replace('[','').replace(']','')
        pdf.multi_cell(80, 5, f'{b}',0,0,0,0)
        pdf.ln(5)
        pdf.cell(80, 5, f'',1,0,0,1)#fundo preto
        pdf.ln(10)
        pdf.multi_cell(80, 5, f'CLIENT: WILLOW PINTO DIAS ,END: RUA OSMA ,CPF:000000358895',0,0,0)
        pdf.ln(10)
        pdf.set_font('Arial', '', 8)
        pdf.cell(80, 5, f'Número: - Série:000 Emissão DT_EMISSAO: ',ln=True,align='C')
        pdf.ln(10)

        pdf.cell(80, 5, f'',1,0,0,1)
        pdf.ln(7)
        pdf.set_font('Arial', '', 15)
        pdf.cell(80, 5, f'CONTIGENCIA',ln=True,align='C')
        pdf.ln(5)
        pdf.set_font('Arial', '', 9)
        pdf.cell(80, 5, f'DEVER SER AUTORIZADA ATE 24 HORAS',ln=True,align='C')
        pdf.ln(5)
        pdf.cell(80, 5, f'',1,0,0,1)
     
        pdf.ln()
        pdf.set_y(-15)
        pdf.image('icone/qrnfce.png', 32, pdf.get_y()-25, 35)
        

        pdf.output("relatoriopdv/pdvpdf/nfce.pdf")

    
