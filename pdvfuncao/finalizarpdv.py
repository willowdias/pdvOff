from PyQt5.QtWidgets import QApplication, QDialog,QCompleter, QPushButton,QLineEdit,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QShortcut
from PyQt5.QtGui import QKeySequence
from layout.finalizarpdv import*
from PyQt5.QtGui import QDoubleValidator
from database.sqlitequery import*
from datetime import datetime,timedelta
from pdvfuncao.parcelapdv import*
from relatoriopdv.cupom import*
class Finaliza_pdv(QDialog):
    def __init__(self,*args):
        super().__init__()
        self.ui = Ui_finalizar()
        self.ui.setupUi(self)
        self.unittamanhocoluna()
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
        ###############finalizar Venda NFCE
        self.ui.actioncodCliente.triggered.connect(self.LiberaCliente)
        shortcut = QShortcut(QKeySequence("Ctrl+F2"), self)
        shortcut.activated.connect(lambda:self.verfiicaparcela("True"))
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
        #ocultar combox parcela
       
        #######finalizar venda
        self.ui.bt_finalizar.clicked.connect(self.verfiicaparcela)
    def unittamanhocoluna(self):
        self.ui.tb_formPAgmento.setColumnWidth(0, 25)
        self.ui.tb_formPAgmento.setColumnWidth(1, 200)
        self.ui.tb_formPAgmento.setColumnWidth(3, 15)
    def selecionarformapagmento(self):#essa opçao pega indice da tabela pra pagamento
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
        self.ui.line_nome_cliente.selectAll()
        banco=db.select('''select nome from clientes ''')
        nome=[i[0] for i in banco]#essa funçao coloca lista
        completer = QCompleter(nome, self)
        completer.setCaseSensitivity(False)
        self.ui.line_nome_cliente.setCompleter(completer)
        
    def selecionacodCliente(self,nome):#essa funçao pega cliente selecionado
        banco=db.select(f'''select * from clientes where nome='{nome}' ''')
        codigo=[i for i in banco]
        print(codigo[0][0])
        self.ui.line_cod_cliente.setText(str(codigo[0][0]))
        self.ui.line_cpf.setText(str(codigo[0][3]))
        self.ui.line_endereco.setText(str(codigo[0][13]))
    def verfiicaparcela(self,AtivaNfce=None):
        if float(self.ui.db_total_venda.value())>0:#verficia valo zerado pra finalizar venda
            pass
        else:
            fatura=0
            somatab=0
            formapagamentorsu=[]
            for i in range(self.ui.tb_formPAgmento.rowCount()):
                vl=(str(self.ui.tb_formPAgmento.item(i, 2).text()).replace('R','').replace('$',''))
                vl2=(self.ui.tb_formPAgmento.item(i,3).text())
                valor=str(self.ui.tb_formPAgmento.item(i, 2).text()).replace('R', '').replace('$', '')    
                somatab+=float(valor)
                formapagamento=str(self.ui.tb_formPAgmento.item(i,1).text().upper())
                if float(vl)>0:#verifica valor soma para envia para cupom
                    formapagamentorsu.append(formapagamento)
                if float(vl)>0 and vl2=='S':
                    fatura=float(vl)
            
            if fatura>0:#verficia se campo tem valor gera parcela
                if self.ui.line_cod_cliente.text()=="":
                    QMessageBox.information(self,"Clientes","Cliente vazio Gera parcela")
                    self.LiberaCliente()
                else:
                    if AtivaNfce=="True":
                        if somatab<1:
                            pass
                        else:
                            self.geranfce(formapagamentorsu)
                    self.finalizartb_nota(somatab)
                    pdv_parcela(fatura,self.ui.line_cod_cliente,).exec_()
            else:
                if AtivaNfce=="True":
                    if somatab<1:
                        pass
                    else:
                        self.geranfce(formapagamentorsu)
                self.finalizartb_nota(somatab)
    def geranfce(self,formapagamentorsu):#essa funçao gera cupo eletronico
        
        geranfce(self.objeto[1],
                formapagamentorsu
                 )
        relatoriopdv('nfce').exec()
    def finalizartb_nota(self,somatab):
        data_e_hora_atuais = datetime.now()
        cod_cli=self.ui.line_cod_cliente.text()
        nome_cli=self.ui.line_nome_cliente.text()
        
        banco=db.select('SELECT notas FROM notas ORDER BY notas DESC LIMIT 1 ')#VERIRICA ULTIMO CODIGO
        try:#CAMUFLA ERRO LIST
            ultimocodigonota=banco[0][0]
        except:
            ultimocodigonota=0
        
        if not ultimocodigonota:
            ultimocodigonota=0

        if cod_cli=="":
            cod_cli='1'
        if nome_cli =="":
            nome_cli='CONSUMIDOR FINAL'

        if somatab<=0:
            QMessageBox.information(self,'Tabela Pagamento','Valores Pagamento zerado R$ 0,00')
        else:
            
            insertnotas=F""" INSERT INTO NOTAS (
                NOTAS,COD_CLIENT,NOME_CLI,DT_EMISSAO,VALOR)VALUES
                {f'{ultimocodigonota+1}',f'{cod_cli}',f'{nome_cli}',
                f'{data_e_hora_atuais.strftime("%d/%m/%Y")}',f'{("{:.2f}".format(somatab))}'}; """
            db.insert(insertnotas)
            self.tabela_itens(ultimocodigonota,data_e_hora_atuais.strftime("%d/%m/%Y"))
    
    def tabela_itens(self,ultimocodigonota=None,data=None):#gera itens tabelaitens
        ultimocodigo=0
        
        for i in range(self.objeto[1].rowCount()):#essa opçapega quantidade iten linha
            codbarra=self.objeto[1].item(i, 0).text()#codbarra
            descricao=self.objeto[1].item(i, 1).text()#descricao
            quant=self.objeto[1].item(i, 2).text()#quantidade
            unid=self.objeto[1].item(i, 3).text()#unidade
            preco=self.objeto[1].item(i, 4).text()#preco unitario
            total=self.objeto[1].item(i, 5).text()#total
            ultimocodigo=ultimocodigonota+1
             
            
            insert=f""" INSERT INTO nota_itens(nota,codigo_barra,dt_emissao)
            values {f'{ultimocodigo}',f'{codbarra}',f'{data}'};"""

            db.insert(insert)
        
        QMessageBox.information(self,'Nota',f'Numero nota: {ultimocodigo}')
        
        self.limpartabelasapozfinalizar()
        self.objeto[4]()#verifica caixa
        self.close()

    def limpartabelasapozfinalizar(self):
        self.objeto[0].setValue(0)
        self.objeto[1].setRowCount(0)
        self.objeto[2].setValue(0)
        self.objeto[3].setValue(0)