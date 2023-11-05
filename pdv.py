import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget

from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QLineEdit, QLabel, QWidget,QFrame
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSpacerItem, QLabel
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from icone.icone import*
from layout.pdvoff import*
from funcao import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
class Pdv(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_pdv_sistem()
        self.ui.setupUi(self)
        self.showMaximized()

        self.funcoe=pdb_funcao(
            self.ui.line_produto,#[0]
            self.ui.db_quantidade,#[1]
            self.ui.tab_itens,#[2]
            self.ui.db_quantidade_itens,#[3]
            self.ui.db_total_unitario,#[4]
            self.ui.db_total_venda,#[5]
            self.ui.lb_caixa_livre,#[6]
            self.ui.tab_estoque_itens,#[7]
            self.ui.stackedWidget,#[8]
            self.ui.venda,#[9]
            self.ui.estoque,#[10]
            self.ui.line_estoque#[11]
            
        )    
        self.ui.line_produto.returnPressed.connect(self.funcoe.add_row)
        self.ui.db_quantidade.editingFinished.connect(self.ui.line_produto.setFocus)
        self.ui.bt_delete_produto.clicked.connect(self.funcoe.removesLinhas)
        #busca itens estoque
        self.atalho = QShortcut(QKeySequence(Qt.Key_F12), self)
        self.atalho.activated.connect(lambda:self.funcoe.currenttela(True))
        self.esc = QShortcut(QKeySequence(Qt.Key_Escape), self)
        self.esc.activated.connect(lambda:self.funcoe.currenttela(False))   
        self.ui.line_estoque.returnPressed.connect(self.funcoe.buscaProduto)
        #selecionar item tb estoque
        
        self.ui.tab_estoque_itens.installEventFilter(self)
    def eventFilter(self, obj, event):
        if event.type() == event.KeyPress and obj is self.ui.tab_estoque_itens:
            key = event.key()
            if key == Qt.Key_Return or key == Qt.Key_Enter:
                self.funcoe.selecionaritenestoque()
                return True  
        return super().eventFilter(obj, event)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Pdv()
    #window.setWindowFlags(Qt.FramelessWindowHint)
    window.show()
    sys.exit(app.exec_())
