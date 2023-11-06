
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
#from relatorio.formPdf import *
from layout.FormPdf import*
import os
import sys
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog, QPrintDialog
class relatoriopdv(QDialog):#essa tela puxa sistema sintegra
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_pdf_gerado()
        self.ui.setupUi(self)
        #self.showMaximized()
        
        #add botoes menu
        self.ui.tol_menu.addAction(self.ui.actionenvia_email) 
        self.ui.tol_menu.addAction(self.ui.actionimprimir) 
        self.ui.tol_menu.addAction(self.ui.actionsalvar_pdf) 
        settings =self.ui.web_browser.settings()
        settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        settings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.JavascriptEnabled, True)
       
        url = QtCore.QUrl.fromLocalFile(f'{os.getcwd()}/itens.pdf')
        self.ui.web_browser.load(url)
        self.printer = QPrinter()#chama impressora
        #funçao imprimir 
        self.ui.actionimprimir.triggered.connect(self.printPDF)
    def printPDF(self):
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            printer = QPdfWriter("itens.pdf")
            painter = QPainter(printer)
            self.ui.web_browser.render(painter)
            painter.end()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = relatoriopdv()
    #window.setWindowFlags(Qt.FramelessWindowHint)
    window.setWindowFlags(Qt.Drawer|Qt.WindowStaysOnTopHint)
    window.show()
    sys.exit(app.exec_())