from fpdf import FPDF
from datetime import datetime,timedelta
class PDF(FPDF):
   
    
    def add_item(self,qtprc,objetosdicionario,valor,datavencimento,qtparcela):
        data_e_hora_atuais = datetime.now()
 
        self.image('icone/pdv.png', x=5, y=self.get_y()-3, w=20)
        self.ln(5)#cabeçario
        self.set_x(50)#mexe direita
      
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f"DUPLICATA 0{qtprc+1} ", 0, 1, 'L')#quantidade duplicata
        self.line(1, self.get_y(), self.w - 10, self.get_y())
        self.ln(4)
        self.set_fill_color(200, 220, 255)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f"VALOR: { float('{:.2f}'.format(float(valor)/int(qtparcela)))}", 0, 1, 'C',1)#valortotal
      
        self.set_font('Arial', 'B', 10)
        self.set_text_color(220, 50, 50)
        self.cell(0, 4, f"DATA VENCIMENTO: {datavencimento}", 0, 1, 'C',1)#DATA VENCIMENTO
        ############################
       
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'I', 10)
        for key, value in objetosdicionario.items():#cria as duplicata
            
            self.cell(0, 5, f"{key}: {str(value).upper()}", 0, 1, 'L')
            
        self.cell(0, 6, "__"*30, 0, 1, 'C')
        self.set_y(self.get_y())
        self.cell(0, 2, F"ASSINATURA CLIENTE: {str(objetosdicionario['Nome']).upper()}", 0, 1, 'C')
        #data emissao
        self.set_font('Arial', 'B', 12)
        self.cell(0, 5, F'DATA EMISSÃO: \n{data_e_hora_atuais.strftime("%d/%m/%Y")}', 0, 1, 'L')
        self.set_font('Arial', '', 10)
        t='-'*150
        self.multi_cell(0,5,f"""
                        O NÃO PAGAMENTO DA DIVIDA SUPRACITADA ACIMA
                        NO RELATORIO O PODE ACARRETAR INCLUSÃO DO SEU NOME NO SPC/SERASA.\n\n\n\n\n\n\n                                                                                                                                       
{t}
                        """,0,0,"C")
      
        

       
        self.ln(5)
    def footer(self):#PAGINA BAIXO
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 2, 'PAgina %s' % self.page_no(), 0, 0, 'C')
       
        
