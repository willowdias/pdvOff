from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton,QTableWidgetItem, QShortcut,QMessageBox
from layout.Estoque import*
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QDoubleValidator
from database.sqlitequery import*
class Estoque_cadastro(QDialog):
    def __init__(self,*args):
        super().__init__()
        self.ui = Ui_form_estoque()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Drawer| Qt.FramelessWindowHint)
        self.showFullScreen()
        #adiciona action menu
   
        validator = QDoubleValidator()
        validator.setDecimals(0)  # Set to 0 to allow only integers
        self.ui.linencm.setValidator(validator)
        self.ui.linecfopsaida.setValidator(validator)
        self.ui.linecstsaida.setValidator(validator)
        
        #movimenta entre telas
        self.ui.bt_incluir.clicked.connect(self.mudatela)
        self.ui.bt_estoque.clicked.connect(self.mudatela)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.alteraTela)
        #grava produto
        self.ui.bt_grava.clicked.connect(self.incluirCliente)
        #gera codigo produto
        self.geraidProduto()
        #busca PRoduto estoque
        self.ui.line_buscaPRodutoestoque.editingFinished.connect(self.buscProduto)
        #seleciona altera estoque
        self.ui.bt_alterar.clicked.connect(self.SelecionaProdutoEstoque)
        self.ui.tab_estoque.doubleClicked.connect(self.SelecionaProdutoEstoque)
        #pergunta fecha sistema
        self.ui.bt_closeSistema.clicked.connect(self.FechaSistema)
        #verifica Se produto Cadastro
        self.ui.line_cod_barra.editingFinished.connect(self.VerificaPRodutoExiste)
        #seleciona fotos
        self.ui.lb_fotos.mouseDoubleClickEvent = lambda event:self.selecionaFoto()
    def FechaSistema(self):
        reply = QMessageBox.question(self, 'Pergunta', 'Você gostaria de Fecha?', 
                                    QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()
      
    def alteraTela(self):
        current_index = self.ui.stackedWidget.currentIndex()
        next_index = (current_index + 1) % self.ui.stackedWidget.count()

        self.ui.stackedWidget.setCurrentIndex(next_index)
        self.timer.stop()
    def mudatela(self):
        self.timer.start(1000) 
    
    def VerificaPRodutoExiste(self):
        self.codigoBarra=self.ui.line_cod_barra.text()
        banco=db.select(f'''select codigo_barra from tb_estoque where codigo_barra='{self.codigoBarra}' ''')
        codigo=[i for i in banco]
        if not banco:
            pass
        else:
            if codigo[0][0]!=self.codigoBarra:
                print("nao existe")
            else:
                
                self.ui.line_cod_barra.clear()
                self.ui.line_cod_barra.setFocus()
            QMessageBox.information(self,'Codigo barra',f'Codigo Barra Existe {codigo[0][0]}')
    def geraidProduto(self):
        banco=db.select('SELECT id FROM tb_estoque ORDER BY id DESC LIMIT 1 ')
        if not banco:
            banco=1
        self.ui.line_codigo.setText(str(banco[0][0]))
    def selecionaFoto(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Caminho Banco dfb", ":", "Image Files (*.PNG);;All Files (*)") # Ask for file
        if fileName: #caminho banco
            original_pixmap =QPixmap(f"{fileName}")
            self.ui.lb_fotos.setPixmap( original_pixmap.scaled(420,320))
    def incluirCliente(self):
        try:
            descricao=self.ui.line_descricao.text()
            codbarra=self.ui.line_cod_barra.text()
            quant=self.ui.db_quantidade.value()
            custo=self.ui.dbcusto.value()
            venda=self.ui.dbvenda.value()
            permitirdesconto='N'
            ativo='N'
            if self.ui.ch_pr_desconto.isChecked():
                permitirdesconto='S'

            if self.ui.ch_ativo.isChecked():
                ativo='S'

            while True:
                if descricao=='':
                    QMessageBox.information(self,'Descricao',"Descriçao em branco")
                    self.ui.line_descricao.setFocus()
                    break
                if codbarra=='':
                    QMessageBox.information(self,'Descricao',"Codigo barra em branco")
                    self.ui.line_cod_barra.setFocus()
                    break
                else:
                    inserirestoque=f""" INSERT INTO tb_estoque (codigo_barra,
                    descricao,quant,custo,venda,pr_desconto,ativo)
                    values {f'{codbarra}',f'{descricao}',f'{quant}',f'{custo}',
                    f'{venda}',f'{permitirdesconto}',f'{ativo}'};"""
                    db.insert(inserirestoque)
                    QMessageBox.information(self,'Cadastro','Produto Cadastrado com sucesso')
                break
        except Exception as e:
            QMessageBox.information(self,'Erro Cadastro Estoque',f'{e}')
    def buscProduto(self):
        descricao=self.ui.line_buscaPRodutoestoque.text()
        banco=db.select(f'''select *from tb_estoque where descricao like '{descricao}%'  ''')
        self.ui.tab_estoque.setRowCount(0)
        if descricao=="":
            self.ui.tab_estoque.setRowCount(0)
            banco=''
        if descricao=='*':
            banco=db.select(f'''select *from tb_estoque''')
        for a,b in enumerate(banco):
            self.ui.tab_estoque.insertRow(a)
            self.ui.tab_estoque.setItem(a, 0, QTableWidgetItem(str(b[0])))#codigobarra
            self.ui.tab_estoque.setItem(a, 1, QTableWidgetItem(str(b[1])))#codigobarra
            self.ui.tab_estoque.setItem(a, 2, QTableWidgetItem(str(b[2])))#descricao
            self.ui.tab_estoque.setItem(a, 3, QTableWidgetItem(str(b[3])))#quantidade
            self.ui.tab_estoque.setItem(a, 4, QTableWidgetItem(f'R$ {str(float(b[8]))}'))#custo
            self.ui.tab_estoque.setItem(a, 5, QTableWidgetItem(f'R$ {str(float(b[9]))}'))#venda
        for row  in range(self.ui.tab_estoque.rowCount()):
            for col in range(0,6):
                self.ui.tab_estoque.item(row ,col).setTextAlignment(Qt.AlignCenter)
        
        self.ui.tab_estoque.setColumnWidth(0, 5)#codigo barra
        self.ui.tab_estoque.setColumnWidth(1, 80)#descricao
        self.ui.tab_estoque.setColumnWidth(6, 200)#descricao
    def SelecionaProdutoEstoque(self):#seleciona produto tabela alera estoque
        seleciona=self.ui.tab_estoque.selectedItems()[0].text()
        self.mudatela()
        self.ui.line_codigo.setText(str(seleciona))


 