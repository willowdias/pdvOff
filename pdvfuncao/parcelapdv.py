from datetime import datetime,timedelta
from PyQt5.QtWidgets import QApplication, QDialog,QCompleter, QPushButton,QLineEdit,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QShortcut
from PyQt5.QtGui import QKeySequence
from layout.parcelapdv import*
from PyQt5.QtGui import QDoubleValidator
from database.sqlitequery import*
from datetime import datetime,timedelta
import sys
from relatoriopdv.duplicata import*
from relatoriopdv.openpdf import*
from database.sqlitequery import*
class pdv_parcela(QDialog):
    def __init__(self,*args):
        super().__init__()
        self.ui = Ui_parcelapdv()
        self.ui.setupUi(self)
 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Drawer| Qt.FramelessWindowHint)
        self.showFullScreen()
        self.ui.cb_parcela.setFocus()
        self.objetoclass=args
        #pega data atual
        #self.ui.cb_parcela.currentTextChanged.connect(lambda:self.geraparcela(self.ui.cb_parcela.currentText()))
        self.ui.bt_geraparcela.clicked.connect(self.geraparcela)
        self.ui.bt_imprimir.clicked.connect(self.imprimirduplicadata)
    def geraparcela(self):#gera parcela
        parcelas=0
        if str(self.ui.cb_parcela.currentText()).replace('X',''):
            parcelas=str(self.ui.cb_parcela.currentText()).replace('X','')
        banco=db.select(f""" select * from clientes where  id='{self.objetoclass[1].text()}' """)
        codigo=[i for i in banco]
        objetos = {
                "Nome": f"{codigo[0][1]}",
                "CIDADE": "São Paulo",
                "CPF":f"{codigo[0][3]}",
                "TELEFONE":"(69)9-99270-8569",
                "Endereco":f"{codigo[0][13]}",
                "IE":"1408502"
            }   
        self.ui.tb_parcela.setRowCount(0)
        pdf = PDF(format=('A4'))
        pdf.add_page()

        data_e_hora_atuais = datetime.now()
        for x in range(int(parcelas)):  
            data_e_hora_atuais+=timedelta(days=30)
            datavencimento=data_e_hora_atuais.strftime("%d/%m/%Y")
            self.ui.tb_parcela.insertRow(x)
            self.ui.tb_parcela.setItem(x, 0, QTableWidgetItem(str(datavencimento)))   
            self.ui.tb_parcela.setItem(x, 1, QTableWidgetItem(str(float("{:.2f}".format(float(self.objetoclass[0])/int(parcelas))))))   
           
  
            
            pdf.add_item(x,objetos,float(self.objetoclass[0]),
                        datavencimento,parcelas)
            
        # Save the pdf with name .pdf
        pdf.output("relatoriopdv/pdvpdf/duplicata.pdf")

        
    def imprimirduplicadata(self):
        
        relatoriopdv('duplicata').exec()

        