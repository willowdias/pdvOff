from PyQt5.QtWidgets import QApplication, QDialog,QCompleter, QPushButton,QLineEdit,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QShortcut
from PyQt5.QtGui import QKeySequence
from layout.finalizarpdv import*
from PyQt5.QtGui import QDoubleValidator
from sqlitequery import*
class Finaliza_pdv(QDialog):
    def __init__(self,*args):
        super().__init__()
        self.ui = Ui_finalizar()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Drawer| Qt.FramelessWindowHint)
        self.showFullScreen()
        #add action lineedit
        self.ui.line_nome_cliente.addAction(self.ui.actioncodCliente, QLineEdit.TrailingPosition)

        #funçao libebar buca cliente
        self.ui.actioncodCliente.triggered.connect(self.LiberaCliente)
        shortcut = QShortcut(QKeySequence("F11"), self)
        shortcut.activated.connect(self.LiberaCliente)

        self.ui.actioncodCliente.triggered.connect(self.LiberaCliente)
        shortcut = QShortcut(QKeySequence("Enter"), self)
        shortcut.activated.connect(self.inserirpagemnto)
        #funçaobusca codcliente
        self.ui.line_nome_cliente.returnPressed.connect(
            lambda:self.selecionacodCliente(self.ui.line_nome_cliente.text()))
       

        #essa funçao pega dados primeira class
        self.objeto=args
        self.valor=self.objeto[0].value()
        self.ui.db_total_venda.setValue(self.objeto[0].value())
        self.ui.db_valorDocumento.setValue(self.objeto[0].value())
        #addicionar decimal lineedit
        validator = QDoubleValidator()
        validator.setDecimals(0)  # Set to 0 to allow only integers
        self.ui.line_doc.setValidator(validator)
        #selecionar forma pagemnto
        self.ui.tb_formPAgmento.itemSelectionChanged.connect(self.selecionarformapagmento)
        self.ui.tb_formPAgmento.selectRow(0)
        self.ui.tb_formPAgmento.setFocus()
    def selecionarformapagmento(self):
        index=self.ui.tb_formPAgmento.selectedItems()[0].text()
       
        self.ui.line_doc.setText(index)
    def inserirpagemnto(self):#essa opçao pega valor inserio inserio tabwidget pagamento
        
        index=int(self.ui.line_doc.text())
        
        if index>self.ui.tb_formPAgmento.rowCount():
            QMessageBox.information(self,"Pagamento","Tipo PAgameno Nao existe")   
        elif float(self.ui.db_total_venda.value())<=0:
            pass
      
        elif self.ui.db_valorDocumento.value()>self.ui.db_total_venda.value():
            QMessageBox.information(self,"Pagamento","Valor Superior \n Valor Total") 
            self.ui.db_valorDocumento.setValue(self.ui.db_total_venda.value())    
        else:
            self.ui.tb_formPAgmento.setItem(index-1, 2, QTableWidgetItem(f'R$ {str(float("{:.2f}".format(self.ui.db_valorDocumento.value())))}'))
            self.ui.db_valorDocumento.setValue(0)
            self.ui.tb_formPAgmento.selectRow(index-1)
            self.ui.tb_formPAgmento.setFocus()
            self.caculartabelapagemnto()
    def LiberaCliente(self):#essa funaço libera busca  cliente  
        self.ui.line_nome_cliente.setFocus()
        banco=db.select('''select nome from clientes ''')
        nome=[i[0] for i in banco]#essa funçao coloca lista
        completer = QCompleter(nome, self)
        completer.setCaseSensitivity(False)
        self.ui.line_nome_cliente.setCompleter(completer)
    def caculartabelapagemnto(self):
        totalvenda=0
        for i in range(self.ui.tb_formPAgmento.rowCount()):
            valor=str(self.ui.tb_formPAgmento.item(i, 2).text()).replace('$', '').replace('R','').replace(',','.')  
            total=float(valor) 
            totalvenda+=float(total)
        
        self.ui.db_total_venda.setValue(self.valor-totalvenda)
        self.ui.db_valorDocumento.setValue(self.ui.db_total_venda.value())
    def selecionacodCliente(self,nome):
        banco=db.select(f'''select id from clientes where nome='{nome}' ''')
        codigo=[i[0] for i in banco]
        self.ui.line_cod_cliente.setText(str(codigo[0]))
      