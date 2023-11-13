from fpdf import FPDF
import locale


class geranfce:
    def __init__(self): 

        pdf = FPDF()
  
       
        pdf = FPDF('P', 'mm', (105,300))#coloca tamanho
        pdf.add_page()
        print(pdf.get_y())
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
        pdf.set_font('Arial', '', 5)
        pdf.cell(-7)
        pdf.cell(35, 6, 'DESCRIÇAO', 1, 0, 'L')
        pdf.cell(15, 6, 'QTD:', 1, 0, 'L')
        pdf.cell(25, 6, 'VL Unid:', 1, 0, 'L')
        pdf.cell(25, 6, 'Vl Total:', 1, 0, 'L')

        pdf.ln(9)
        pdf.set_font('Arial', '', 8) 

        for i in range(3):
            pdf.cell(-7)
            pdf.cell(35, 6, str(f'itensitensitensitensitensiten'[0:40]),0)#descricao
            pdf.cell(1)
            pdf.cell(15, 6, str(f'00'),0,0,'C')#quantidade
            pdf.cell(1)
            pdf.cell(25, 6, str(f'vlw'),0,0,'C')#quantidade
            pdf.cell(1)
            pdf.cell(25, 6, str(f'vlw'),0,0,'C')#quantidade
            pdf.line(0, pdf.get_y() + 8, 200, pdf.get_y() + 8)
            pdf.ln(3)
            pdf.ln()
        pdf.set_font('Arial', '', 10)
        
        pdf.ln(5)
        pdf.set_y(-125)
        pdf.cell(80, 5, 'QTD. TOTAL DE ITENS',ln=True,align='L')
        pdf.cell(80, -5, f"000",1,ln=True, align='R')
        pdf.ln(5)
        pdf.cell(80, 5, f'SUBTOTAL R$',ln=True,align='L')
        pdf.cell(80, -5, "0000",1, ln=True, align='R')
        pdf.ln(5)
        pdf.cell(80, 5, f'VALOR DESCONTO R$',ln=True,align='L')
        pdf.cell(80, -5, "0000",1 , ln=True, align='R')
        pdf.ln(5)
        pdf.cell(80, 5, f'VALOR TOTAL R$',ln=True,align='L')
        pdf.cell(80, -5, f"0000",1, ln=True, align='R')
        pdf.ln(5)
        pdf.cell(30, 5, f'TROCO R$',0,ln=True,align='L')
        pdf.cell(80, -5, "0000",1, ln=True, align='R')
        pdf.ln(5)
        pdf.cell(80, 5, f'VENDEDOR: ',pdf.page_no(),ln=True,align='L')
        pdf.cell(80, -5, "0000",1, ln=True, align='R')
        pdf.ln(5)
        pdf.cell(80, 5, f'ok: ',1,0,0,1)
        pdf.ln(5)
        pdf.cell(80, 5, f'ok: ',1,0,0,1)
        pdf.ln(5)
        pdf.cell(80, 5, f'ok: ',1,0,0,1)
        pdf.ln(5)
        som=['DINHEIRO','DUPLICATA','PIX']
        b=str([i for i in som]).replace("'","").replace('[','').replace(']','')
        
        pdf.multi_cell(80, 5, f'{str(b)}',1,0,0,0)
        pdf.ln(0)


        pdf.set_y(-25)
        pdf.image('icone/qrnfce.png', 25, pdf.get_y()-25, 50)
        

        pdf.output("nfce.pdf")

    
geranfce()