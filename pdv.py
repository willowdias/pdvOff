import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from icone.icone import*
from layout.pdvoff import*
from pdvfuncao.funcao import*
from PyQt5.QtCore import Qt
from pdvfuncao.finalizarpdv import*
from pdvfuncao.estoque import*
class Pdv(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_pdv_sistem()
        self.ui.setupUi(self)
        

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
            self.ui.line_estoque,#[11]
            self.ui.lb_data_emissao,#[12]
            self.ui.lb_ip,#[13]
            self.ui.lb_nome_user,#[14]
            self.ui.tool_menu,#[15]
            self.ui.actionCadastro_Cliente,#[16]
            self.ui.actionCadastro_Produto,#[17]
            self.ui.db_desconto#[18]
            
        )    
        self.ui.line_produto.returnPressed.connect(self.funcoe.add_row)
        self.ui.db_quantidade.editingFinished.connect(self.ui.line_produto.setFocus)
        self.ui.bt_delete_produto.clicked.connect(self.funcoe.removesLinhas)
        #busca itens estoque
        self.atalho = QShortcut(QKeySequence("F11"),self)#f12 chama tela
        self.atalho.activated.connect(lambda:self.funcoe.currenttela(True))
        self.esc = QShortcut(QKeySequence("Ctrl+F11"),self)#said da tela
        self.esc.activated.connect(lambda:self.funcoe.currenttela(False))   
        self.ui.line_estoque.returnPressed.connect(self.funcoe.buscaProduto)
        #desconto na venda
        self.descontovenda = QShortcut(QKeySequence("F12"),self)#said da tela
        self.descontovenda.activated.connect(self.funcoe.liberaDesconto)
        self.ui.db_desconto.editingFinished.connect(self.funcoe.DescontoNavenda)
        self.ui.db_desconto.editingFinished.connect(lambda:self.ui.line_produto.setFocus())
        #cadastro estoque ou busca estoque
        self.ui.actionCadastro_Produto.triggered.connect(lambda:Estoque_cadastro().exec_())
        #finalizar venda 

        self.ui.tb_finalizar.clicked.connect(lambda:Finaliza_pdv(
            self.ui.db_total_venda,#[0]
            self.ui.tab_itens,#[1]
            self.ui.db_quantidade_itens,#[2]
            self.ui.db_total_unitario,#[3]
            self.funcoe.verificacaixaOcupado,#[4]
            self.ui.db_desconto#[5]


        ).exec())
        self.ui.tab_estoque_itens.installEventFilter(self)#chama tela estoque
    def eventFilter(self, obj, event):#essa funçao enter para tabela-
        if event.type() == event.KeyPress and obj is self.ui.tab_estoque_itens:
            key = event.key()
            if key == Qt.Key_Return or key == Qt.Key_Enter:
                self.funcoe.selecionaritenestoque()
                return True  
        return super().eventFilter(obj, event)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Pdv()
    
    window.show()
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.showMaximized()
    sys.exit(app.exec_())
