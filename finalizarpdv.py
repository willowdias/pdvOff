from PyQt5.QtWidgets import QApplication, QDialog,QCompleter, QPushButton,QLineEdit,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QShortcut
from PyQt5.QtGui import QKeySequence
from layout.finalizarpdv import*
from PyQt5.QtGui import QDoubleValidator
from sqlitequery import*
from datetime import datetime


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
        self.valortotalvendapdv=self.objeto[0].value()
        self.ui.db_total_venda.setValue(self.objeto[0].value())
        self.ui.db_valorDocumento.setValue(self.objeto[0].value())
        #addicionar decimal lineedit
        validator = QDoubleValidator()
        validator.setDecimals(0)  # Set to 0 to allow only integers
        self.ui.line_doc.setValidator(validator)
        #selecionar forma pagemnto
        self.ui.tb_formPAgmento.itemSelectionChanged.connect(self.selecionarformapagmento)
        self.ui.tb_formPAgmento.selectRow(0)#opçao selecionar primeira linha tabpagemnto
        self.ui.tb_formPAgmento.setFocus()#foca na tabela
        #######finalizar venda
        self.ui.bt_finalizar.clicked.connect(self.finalizartb_nota)
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
    
    def caculartabelapagemnto(self):
        totalvenda=0
        for i in range(self.ui.tb_formPAgmento.rowCount()):
            valor=str(self.ui.tb_formPAgmento.item(i, 2).text()).replace('$', '').replace('R','').replace(',','.')  
            total=float(valor) 
            totalvenda+=float(total)
        
        self.ui.db_total_venda.setValue(self.valortotalvendapdv-totalvenda)#essa funçao pega valor total venda e calcular resultado
        self.ui.db_valorDocumento.setValue(self.ui.db_total_venda.value())#essa funçao pega valor total 
    def LiberaCliente(self):#essa funaço libera busca  cliente  
        self.ui.line_nome_cliente.setFocus()
        banco=db.select('''select nome from clientes ''')
        nome=[i[0] for i in banco]#essa funçao coloca lista
        completer = QCompleter(nome, self)
        completer.setCaseSensitivity(False)
        self.ui.line_nome_cliente.setCompleter(completer)
        
    def selecionacodCliente(self,nome):#essa funçao pega cliente selecionado
        banco=db.select(f'''select id from clientes where nome='{nome}' ''')
        codigo=[i[0] for i in banco]
        self.ui.line_cod_cliente.setText(str(codigo[0]))

    def finalizartb_nota(self):
        data_e_hora_atuais = datetime.now()
        cod_cli=self.ui.line_cod_cliente.text()
        nome_cli=self.ui.line_nome_cliente.text()
        banco=db.select('SELECT notas FROM notas ORDER BY notas DESC LIMIT 1 ')#VERIRICA ULTIMO CODIGO
        try:#CAMUFLA ERRO LIST
            valores=banco[0][0]
        except:
            valores=0
        
        if not valores:
            valores=0
        if cod_cli=="":
            cod_cli='1'
        if nome_cli =="":
            nome_cli='CONSUMIDOR FINAL'
        
        
        somatab=0
        for i in range(self.ui.tb_formPAgmento.rowCount()):
            valor=str(self.ui.tb_formPAgmento.item(i, 2).text()).replace('R', '').replace('$', '')    
            somatab+=float(valor)
       
        if somatab<=0:
            QMessageBox.information(self,'Tabela Pagamento','Valores Pagamento zerado R$ 0,00')
        else:
            insertnotas=F""" INSERT INTO NOTAS (
                NOTAS,COD_CLIENT,NOME_CLI,DT_EMISSAO,VALOR)VALUES
                {f'{valores+1}',f'{cod_cli}',f'{nome_cli}',
                f'{data_e_hora_atuais.strftime("%d/%m/%Y")}',f'{("{:.2f}".format(somatab))}'}; """
            db.insert(insertnotas)
            self.tabela_itens(valores,data_e_hora_atuais.strftime("%d/%m/%Y"))
    def limpartabelasapozfinalizar(self):
        self.objeto[0].setValue(0)
        self.objeto[1].setRowCount(0)
        self.objeto[2].setValue(0)
        self.objeto[3].setValue(0)
    def tabela_itens(self,valores=None,data=None):
        soma=0
        
        for i in range(self.objeto[1].rowCount()):#essa opçapega quantidade iten linha
            codbarra=self.objeto[1].item(i, 0).text()#codbarra
            descricao=self.objeto[1].item(i, 1).text()#descricao
            quant=self.objeto[1].item(i, 2).text()#quantidade
            unid=self.objeto[1].item(i, 3).text()#unidade
            preco=self.objeto[1].item(i, 4).text()#preco unitario
            total=self.objeto[1].item(i, 5).text()#total
            soma=valores+1
             
            
            insert=f""" INSERT INTO nota_itens(nota,codigo_barra,dt_emissao)
            values {f'{soma}',f'{codbarra}',f'{data}'};"""

            db.insert(insert)
        self.limpartabelasapozfinalizar()
        self.close()