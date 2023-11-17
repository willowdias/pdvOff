
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget, QLineEdit
from PyQt5.QtWidgets import  QMessageBox
from database.sqlitequery import*
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QShortcut
from datetime import datetime,timedelta
class pdb_funcao:
    def __init__(self,*args):
        self.objetoClass=args
        self.inicial()#essa funçao altera objeto quano inicia sistema
    
    def inicial(self):
        data_e_hora_atuais = datetime.now()
        self.objetoClass[12].setText(f'Data: {str(data_e_hora_atuais.strftime("%d/%m/%Y"))}')
        self.objetoClass[13].setText("Serven: 127.0.0.1 ")
        self.objetoClass[14].setText("usuario: willow")
        self.objetoClass[15].addAction(self.objetoClass[16])
        self.objetoClass[15].addAction(self.objetoClass[17])
        self.objetoClass[2].setColumnWidth(0, 100)#codigo barra
        self.objetoClass[2].setColumnWidth(1, 200)#descricao
        self.objetoClass[2].setColumnWidth(6, 10)#descricao
    def add_row(self):
        self.objetoClass[0].setFocus()

        quantida=self.objetoClass[1].value()
        codigobarra=self.objetoClass[0].text()
        banco=db.select(f'''select *from tb_estoque where codigo_barra = '{codigobarra}'  ''')
        # Adicione uma nova linha à tabela
        if quantida=="" or codigobarra=="":
            pass
        if not banco:
            QMessageBox.information(None,"Produto","Produto Sem Cadastro")
        else:
            
            row_position = self.objetoClass[2].rowCount()
            self.objetoClass[2].insertRow(row_position)
            self.objetoClass[2].setItem(row_position, 0, QTableWidgetItem(str(banco[0][1])))#codigo barra
            self.objetoClass[2].setItem(row_position,1, QTableWidgetItem(str(banco[0][2])))
            self.objetoClass[2].setItem(row_position, 2, QTableWidgetItem(str(quantida)))
            self.objetoClass[2].setItem(row_position,3, QTableWidgetItem(str('unidade')))
            self.objetoClass[2].setItem(row_position,4, QTableWidgetItem(f'R$ {str(float("{:.2f}".format(banco[0][8])))}'))
            self.objetoClass[2].setItem(row_position,5, QTableWidgetItem(f'R$ {str(float("{:.2f}".format(quantida*banco[0][8])))}'))
            self.objetoClass[2].setItem(row_position, 6, QTableWidgetItem(str(banco[0][10])))#desconto
        
            self.objetoClass[2].selectRow(row_position)#seleciona ultima itens da tela
            #self.objetoClass[0].clear()
            self.objetoClass[18].setValue(0)#zera desconto
            self.objetoClass[1].setValue(1)
            self.QuantidadeItensGrade()#carrega quantidade itens na grade
            self.quantidadeitenproduto()#carregaQauntiade iten por itens
            self.verificacaixaOcupado()
            self.CarregaGrade()
    def QuantidadeItensGrade(self):#somar quantidade grade
        self.objetoClass[3].setValue(self.objetoClass[2].rowCount())
    def quantidadeitenproduto(self):#somar produtos tela
        precoitens=0
        totalvenda=0
        for i in range(self.objetoClass[2].rowCount()):
            qtItensvenda=float(self.objetoClass[2].item(i, 2).text())
            precoorigemitem=float(str(self.objetoClass[2].item(i, 4).text()).replace('R', '').replace('$', ''))
            totalvenda+=float(qtItensvenda*precoorigemitem)
           
            #essa opçao a baixo mantenhe valor itens para que acha retorno
            self.objetoClass[2].setItem(i,5, QTableWidgetItem(f'R$ {str(float("{:.2f}".format(qtItensvenda*precoorigemitem)))}'))
            precoitens+=float(precoorigemitem)
        self.objetoClass[5].setValue(float(totalvenda))
        self.objetoClass[4].setValue(float(precoitens))
    def removesLinhas(self):
   
        try:
            for item in self.objetoClass[2].selectedItems():
    
                self.objetoClass[2].removeRow(item.row())
                #print(item.row()+1,item.text())
            self.QuantidadeItensGrade()
            self.quantidadeitenproduto()#carregaQauntiade iten por itens
            self.verificacaixaOcupado()
        except Exception as e:
            QMessageBox.information(None,"Erro",f"{e}")

    def CarregaGrade(self):
        for row  in range(self.objetoClass[2].rowCount()):
            for col in range(0,7):
                self.objetoClass[2].item(row ,col).setTextAlignment(Qt.AlignCenter)
    def verificacaixaOcupado(self):
        if self.objetoClass[2].rowCount()>0:
            self.objetoClass[6].setText("caixa Ocupado")
        else:
            self.objetoClass[6].setText("CAIXA LIVRE")
    def liberaDesconto(self):
        self.objetoClass[18].setFocus()
        self.objetoClass[18].selectAll()
    def DescontoNavenda(self):
       
        totalvenda=0
        original=0
        final=0
        self.quantidadeitenproduto()#soma a tabela
        for i in range(self.objetoClass[2].rowCount()):
            selecionaitendesconto=(self.objetoClass[2].item(i, 6).text())
            
            if str(selecionaitendesconto)=="N":
                original=float(str(self.objetoClass[2].item(i, 5).text()).replace('R', '').replace('$', ''))
                totalvenda=(original)
            else:
                    
                precoorigemitem=float(str(self.objetoClass[2].item(i, 5).text()).replace('R', '').replace('$', ''))
                desconto=float(self.objetoClass[18].value())*float(precoorigemitem)/100
                self.objetoClass[2].setItem(i,5, QTableWidgetItem(f'R$ {str(float("{:.2f}".format(precoorigemitem-desconto)))}'))
                final=float(str(self.objetoClass[2].item(i, 5).text()).replace('R', '').replace('$', ''))
                totalvenda=(original+final)
            
        self.CarregaGrade()
        self.objetoClass[5].setValue(float(totalvenda))
        
        
       
    def buscaProduto(self):#busca produo estoque
        line=self.objetoClass[11].text()
        banco=db.select(f'''select *from tb_estoque where descricao like '{line}%'  ''')
        self.objetoClass[7].setRowCount(0)
        if line=="":
            self.objetoClass[7].setRowCount(0)
            banco=''
        if line=='*':
            banco=db.select(f'''select *from tb_estoque''')
            
        for a,b in enumerate(banco):
            self.objetoClass[7].insertRow(a)
            self.objetoClass[7].setItem(a, 0, QTableWidgetItem(str(b[1])))#codigobarra
            self.objetoClass[7].setItem(a, 1, QTableWidgetItem(str(b[2])))#descricao
            self.objetoClass[7].setItem(a, 2, QTableWidgetItem(str(b[3])))#quantidade
            self.objetoClass[7].setItem(a, 3, QTableWidgetItem(f'R$ {str(float(b[8]))}'))#custo
            self.objetoClass[7].setItem(a, 4, QTableWidgetItem(f'R$ {str(float(b[9]))}'))#venda
            self.objetoClass[7].selectRow(0)
            self.objetoClass[7].setFocus()
    def selecionaritenestoque(self):
        try:
            item=self.objetoClass[7].selectedItems()[0].text() 
            self.objetoClass[0].setText(str(item))
            self.currenttela(False)
        except ValueError as e:
            print(e)
    def currenttela(self,event=None):#essa funçao seleciona item estoque
        if event==True:#estoquecurret
            
            self.objetoClass[8].setCurrentWidget(self.objetoClass[10]) 
            self.objetoClass[0].setFocus(False)
            self.objetoClass[1].setFocus(False)
            self.objetoClass[2].setFocus(False)
            self.objetoClass[11].setFocus() 
               
            
        else: 
            self.objetoClass[8].setCurrentWidget(self.objetoClass[9])
            self.objetoClass[7].setRowCount(0)
            self.objetoClass[0].setFocus(True)
            self.objetoClass[0].setFocus()
            self.objetoClass[1].setFocus(True)
            self.objetoClass[2].setFocus(True)
            self.objetoClass[11].clear()
            