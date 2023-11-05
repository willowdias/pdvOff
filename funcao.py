
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget, QLineEdit
from PyQt5.QtWidgets import  QMessageBox
from sqlitequery import*
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QShortcut
class pdb_funcao:
    def __init__(self,*args):
        self.objetoClass=args
        
        
    def add_row(self):
        self.objetoClass[0].setFocus()

        quantida=self.objetoClass[1].value()
        descricao=self.objetoClass[0].text()
        banco=db.select(f'''select *from tb_estoque where codigo_barra = '{descricao}'  ''')
        # Adicione uma nova linha à tabela
        if quantida=="" or descricao=="":
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
            self.objetoClass[2].setItem(row_position,4, QTableWidgetItem(f'R$ {str(float(banco[0][8]))}'))
            self.objetoClass[2].setItem(row_position,5, QTableWidgetItem(f'R$ {str(float(quantida*banco[0][8]))}'))
            self.objetoClass[2].selectRow(row_position)#seleciona ultima itens da tela

            self.objetoClass[1].setValue(1)
            self.QuantidadeItensGrade()#carrega quantidade itens na grade
            self.quantidadeitenproduto()#carregaQauntiade iten por itens
            self.verificacaixaOcupado()
    def removeitem(self):
        self.objetoClass[2].removeRow(self.objetoClass[2].rowCount() - 1)
    def QuantidadeItensGrade(self):
        self.objetoClass[3].setValue(self.objetoClass[2].rowCount())
    def quantidadeitenproduto(self):#somar produtos tela
        soma=0
        total=0
        for i in range(self.objetoClass[2].rowCount()):
            qtd=str(self.objetoClass[2].item(i, 2).text()).replace('$', '')
            quantidade=float(qtd)
            custo=str(self.objetoClass[2].item(i, 4).text()).replace('R', '').replace('$', '')
            preco=float(custo)

            total+=float(quantidade+preco)
            soma+=float(preco)
        self.objetoClass[5].setValue(float(total))
        self.objetoClass[4].setValue(float(soma))
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


    def verificacaixaOcupado(self):
        if self.objetoClass[2].rowCount()>0:
            self.objetoClass[6].setText("caixa Ocupado")
        else:
            self.objetoClass[6].setText("CAIXA LIVRE")

    def buscaProduto(self):
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
    def currenttela(self,event=None):
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
            