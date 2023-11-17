# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout/ui/Estoque.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_estoque(object):
    def setupUi(self, form_estoque):
        form_estoque.setObjectName("form_estoque")
        form_estoque.setWindowModality(QtCore.Qt.NonModal)
        form_estoque.setEnabled(True)
        form_estoque.resize(1153, 850)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/telainicial/telainicial/estoque.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        form_estoque.setWindowIcon(icon)
        form_estoque.setStyleSheet("text-transform: uppercase;")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(form_estoque)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_2 = QtWidgets.QWidget(form_estoque)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
"\n"
"    background-color: rgb(0, 0, 0,200);}")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.frame_6 = QtWidgets.QFrame(self.widget_2)
        self.frame_6.setMinimumSize(QtCore.QSize(1100, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 900))
        self.frame_6.setStyleSheet("QFrame#frame_6{\n"
"border-radius:15px;\n"
"background-color: rgb(59, 117, 176);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(5, 3, 5, 5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_botoesmenu = QtWidgets.QFrame(self.frame_6)
        self.frame_botoesmenu.setStyleSheet("QFrame#frame_botoesmenu{\n"
"        background-color: #2b3157;\n"
"border-radius:8px;\n"
"padding:4px;\n"
"}\n"
"QToolButton{\n"
"padding:2px 25px;\n"
"font: 8pt \"Arial\";\n"
"text-transform: uppercase;\n"
"}")
        self.frame_botoesmenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_botoesmenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_botoesmenu.setObjectName("frame_botoesmenu")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_botoesmenu)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.bt_closeSistema = QtWidgets.QPushButton(self.frame_botoesmenu)
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(False)
        font.setItalic(False)
        self.bt_closeSistema.setFont(font)
        self.bt_closeSistema.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_closeSistema.setStyleSheet("QPushButton{\n"
"padding:15px;\n"
"    font: 5pt \"Arial\";\n"
"\n"
"}")
        self.bt_closeSistema.setObjectName("bt_closeSistema")
        self.horizontalLayout_5.addWidget(self.bt_closeSistema)
        self.verticalLayout_4.addWidget(self.frame_botoesmenu)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_6)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Incluirestoque = QtWidgets.QWidget()
        self.Incluirestoque.setStyleSheet("QWidget#Incluirestoque{\n"
"background-color: rgb(59, 117, 176);\n"
"}")
        self.Incluirestoque.setObjectName("Incluirestoque")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Incluirestoque)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.Incluirestoque)
        self.frame.setStyleSheet("QFrame{\n"
"border-radius:10px;\n"
"background-color: rgb(59, 117, 176);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setStyleSheet("font: 20pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("QDoubleSpinBox{\n"
"    border: 2px solid gray;\n"
"    border-radius: 4px;\n"
"\n"
"    \n"
"    font: 900 10pt \"Arial Black\";\n"
"    \n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 9pt \"Arial\";\n"
"}\n"
"QLineEdit {\n"
"    font: 12pt \"Segoe UI\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 0px 8px;\n"
"    \n"
"    selection-background-color: darkgray;\n"
"}\n"
"QLineEdit:focus{\n"
"    background-color: rgb(199, 199, 199);\n"
"}\n"
"\n"
"QPushButton{\n"
"padding:5px;\n"
"    font: 11pt \"Arial\";\n"
"}\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QListView{\n"
"text-align: center;\n"
"    border:                 none;\n"
"    color:                      rgb(87, 96, 134);\n"
"    background-color:   rgb(255, 255, 255);\n"
"    font-weight:            bold;\n"
"    selection-background-color: rgb(47, 175, 178);\n"
"    show-decoration-selected: 1;\n"
"    margin-left:                -10px;\n"
"    padding-left    :           15px;\n"
"}\n"
"\n"
"QListView::item:hover{\n"
"\n"
"    background-color:   rgb(47, 175, 178);\n"
"    border:                 none;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(50, 10, 121, 31))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        self.line_codigo = QtWidgets.QLineEdit(self.frame_3)
        self.line_codigo.setGeometry(QtCore.QRect(170, 10, 101, 31))
        self.line_codigo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.line_codigo.setAlignment(QtCore.Qt.AlignCenter)
        self.line_codigo.setReadOnly(True)
        self.line_codigo.setObjectName("line_codigo")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(50, 50, 121, 31))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.line_descricao = QtWidgets.QLineEdit(self.frame_3)
        self.line_descricao.setGeometry(QtCore.QRect(170, 50, 691, 31))
        self.line_descricao.setObjectName("line_descricao")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(40, 90, 131, 31))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setObjectName("label_5")
        self.line_cod_barra = QtWidgets.QLineEdit(self.frame_3)
        self.line_cod_barra.setGeometry(QtCore.QRect(170, 90, 141, 31))
        self.line_cod_barra.setObjectName("line_cod_barra")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(360, 90, 121, 31))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setOpenExternalLinks(False)
        self.label_6.setObjectName("label_6")
        self.cb_tipo = QtWidgets.QComboBox(self.frame_3)
        self.cb_tipo.setGeometry(QtCore.QRect(480, 90, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_tipo.setFont(font)
        self.cb_tipo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.cb_tipo.setObjectName("cb_tipo")
        self.cb_tipo.addItem("")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(40, 140, 131, 31))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setOpenExternalLinks(False)
        self.label_7.setObjectName("label_7")
        self.cb_marca = QtWidgets.QComboBox(self.frame_3)
        self.cb_marca.setGeometry(QtCore.QRect(170, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_marca.setFont(font)
        self.cb_marca.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.cb_marca.setObjectName("cb_marca")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(370, 140, 101, 31))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setOpenExternalLinks(False)
        self.label_8.setObjectName("label_8")
        self.cb_grupo = QtWidgets.QComboBox(self.frame_3)
        self.cb_grupo.setGeometry(QtCore.QRect(480, 140, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_grupo.setFont(font)
        self.cb_grupo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.cb_grupo.setObjectName("cb_grupo")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(50, 190, 111, 31))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(False)
        self.label_9.setOpenExternalLinks(False)
        self.label_9.setObjectName("label_9")
        self.cb_unidade = QtWidgets.QComboBox(self.frame_3)
        self.cb_unidade.setGeometry(QtCore.QRect(170, 190, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cb_unidade.setFont(font)
        self.cb_unidade.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.cb_unidade.setObjectName("cb_unidade")
        self.bt_unid = QtWidgets.QPushButton(self.frame_3)
        self.bt_unid.setGeometry(QtCore.QRect(320, 190, 31, 31))
        self.bt_unid.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_unid.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/venda/lupacliente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_unid.setIcon(icon1)
        self.bt_unid.setObjectName("bt_unid")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(360, 190, 111, 31))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setOpenExternalLinks(False)
        self.label_10.setObjectName("label_10")
        self.linencm = QtWidgets.QLineEdit(self.frame_3)
        self.linencm.setGeometry(QtCore.QRect(480, 190, 171, 31))
        self.linencm.setObjectName("linencm")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(50, 300, 111, 31))
        self.label_11.setScaledContents(True)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(False)
        self.label_11.setOpenExternalLinks(False)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(40, 340, 131, 31))
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(False)
        self.label_12.setOpenExternalLinks(False)
        self.label_12.setObjectName("label_12")
        self.dbcompra = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dbcompra.setGeometry(QtCore.QRect(170, 300, 121, 31))
        self.dbcompra.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dbcompra.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dbcompra.setProperty("showGroupSeparator", True)
        self.dbcompra.setMaximum(9999999999.0)
        self.dbcompra.setObjectName("dbcompra")
        self.dbcusto = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dbcusto.setGeometry(QtCore.QRect(170, 340, 121, 31))
        self.dbcusto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dbcusto.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dbcusto.setProperty("showGroupSeparator", True)
        self.dbcusto.setMaximum(9999999999.0)
        self.dbcusto.setObjectName("dbcusto")
        self.dbvenda = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.dbvenda.setGeometry(QtCore.QRect(170, 380, 121, 31))
        self.dbvenda.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dbvenda.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dbvenda.setProperty("showGroupSeparator", True)
        self.dbvenda.setMaximum(9999999999.0)
        self.dbvenda.setObjectName("dbvenda")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(50, 380, 121, 31))
        self.label_13.setScaledContents(True)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(False)
        self.label_13.setOpenExternalLinks(False)
        self.label_13.setObjectName("label_13")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_3)
        self.tabWidget.setGeometry(QtCore.QRect(320, 230, 541, 421))
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"   border:none\n"
"}\n"
"\n"
"QTabWidget{\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"        \n"
"    font: 10pt \"Segoe UI\";\n"
"              background-color: #2b3157;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    min-width: 15ex;\n"
"     min-height: 6ex;\n"
"  \n"
"color:white;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    color:white;\n"
"    background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QWidget{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox{\n"
"    background-color: rgb(236, 236, 236);\n"
"border:1px solid\n"
"}\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QListView{\n"
"text-align: center;\n"
"    border:                 none;\n"
"    color:                      rgb(87, 96, 134);\n"
"    background-color:   rgb(255, 255, 255);\n"
"    font-weight:            bold;\n"
"    selection-background-color: rgb(47, 175, 178);\n"
"    show-decoration-selected: 1;\n"
"    margin-left:                -10px;\n"
"    padding-left    :           15px;\n"
"}\n"
"QLabel{\n"
"border-radius:none;\n"
"    background-color: transparent;\n"
"color:black\n"
"\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tributos = QtWidgets.QWidget()
        self.tributos.setStyleSheet("")
        self.tributos.setObjectName("tributos")
        self.cb_situcao = QtWidgets.QComboBox(self.tributos)
        self.cb_situcao.setGeometry(QtCore.QRect(50, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_situcao.setFont(font)
        self.cb_situcao.setStyleSheet("QComboBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QListView{\n"
"text-align: center;\n"
"    border:                 none;\n"
"    color:                      rgb(87, 96, 134);\n"
"    background-color:   rgb(255, 255, 255);\n"
"    font-weight:            bold;\n"
"    selection-background-color: rgb(47, 175, 178);\n"
"    show-decoration-selected: 1;\n"
"    margin-left:                -10px;\n"
"    padding-left    :           15px;\n"
"}\n"
"")
        self.cb_situcao.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.cb_situcao.setObjectName("cb_situcao")
        self.label_15 = QtWidgets.QLabel(self.tributos)
        self.label_15.setGeometry(QtCore.QRect(50, 30, 221, 21))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.linecfopsaida = QtWidgets.QLineEdit(self.tributos)
        self.linecfopsaida.setGeometry(QtCore.QRect(50, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.linecfopsaida.setFont(font)
        self.linecfopsaida.setMaxLength(4)
        self.linecfopsaida.setObjectName("linecfopsaida")
        self.linecstsaida = QtWidgets.QLineEdit(self.tributos)
        self.linecstsaida.setGeometry(QtCore.QRect(170, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.linecstsaida.setFont(font)
        self.linecstsaida.setMaxLength(4)
        self.linecstsaida.setObjectName("linecstsaida")
        self.label_16 = QtWidgets.QLabel(self.tributos)
        self.label_16.setGeometry(QtCore.QRect(50, 110, 91, 21))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tributos)
        self.label_17.setGeometry(QtCore.QRect(170, 110, 101, 21))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.tabWidget.addTab(self.tributos, "")
        self.fotos = QtWidgets.QWidget()
        self.fotos.setObjectName("fotos")
        self.lb_fotos = QtWidgets.QLabel(self.fotos)
        self.lb_fotos.setGeometry(QtCore.QRect(10, 20, 500, 350))
        self.lb_fotos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid ;\n"
"border-radius:0px")
        self.lb_fotos.setText("")
        self.lb_fotos.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_fotos.setObjectName("lb_fotos")
        self.tabWidget.addTab(self.fotos, "")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(60, 260, 101, 31))
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setWordWrap(False)
        self.label_14.setOpenExternalLinks(False)
        self.label_14.setObjectName("label_14")
        self.db_quantidade = QtWidgets.QDoubleSpinBox(self.frame_3)
        self.db_quantidade.setGeometry(QtCore.QRect(170, 260, 121, 31))
        self.db_quantidade.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_quantidade.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.db_quantidade.setProperty("showGroupSeparator", False)
        self.db_quantidade.setDecimals(3)
        self.db_quantidade.setMaximum(9999999999.0)
        self.db_quantidade.setObjectName("db_quantidade")
        self.groupBox = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox.setGeometry(QtCore.QRect(60, 430, 181, 91))
        self.groupBox.setStyleSheet("color:white;\n"
"font: 10pt \"Arial\";")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ch_ativo = QtWidgets.QCheckBox(self.groupBox)
        self.ch_ativo.setObjectName("ch_ativo")
        self.verticalLayout_5.addWidget(self.ch_ativo)
        self.ch_pr_desconto = QtWidgets.QCheckBox(self.groupBox)
        self.ch_pr_desconto.setObjectName("ch_pr_desconto")
        self.verticalLayout_5.addWidget(self.ch_pr_desconto)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.bt_grupo = QtWidgets.QPushButton(self.frame_3)
        self.bt_grupo.setGeometry(QtCore.QRect(660, 140, 31, 31))
        self.bt_grupo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_grupo.setText("")
        self.bt_grupo.setIcon(icon1)
        self.bt_grupo.setObjectName("bt_grupo")
        self.bt_marca = QtWidgets.QPushButton(self.frame_3)
        self.bt_marca.setGeometry(QtCore.QRect(320, 140, 31, 31))
        self.bt_marca.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_marca.setText("")
        self.bt_marca.setIcon(icon1)
        self.bt_marca.setObjectName("bt_marca")
        self.verticalLayout_6.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
"        background-color: #2b3157;\n"
"border-radius:8px;\n"
"padding:4px;\n"
"}\n"
"QPushButton{\n"
"padding:15px;\n"
"    font: 11pt \"Arial\";\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_grava = QtWidgets.QPushButton(self.frame_2)
        self.bt_grava.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_grava.setObjectName("bt_grava")
        self.horizontalLayout.addWidget(self.bt_grava)
        self.bt_cancelar = QtWidgets.QPushButton(self.frame_2)
        self.bt_cancelar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_cancelar.setShortcut("")
        self.bt_cancelar.setObjectName("bt_cancelar")
        self.horizontalLayout.addWidget(self.bt_cancelar)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.bt_estoque = QtWidgets.QPushButton(self.frame_2)
        self.bt_estoque.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_estoque.setObjectName("bt_estoque")
        self.horizontalLayout.addWidget(self.bt_estoque)
        self.verticalLayout_6.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.frame)
        self.stackedWidget.addWidget(self.Incluirestoque)
        self.ControleioEstoque = QtWidgets.QWidget()
        self.ControleioEstoque.setStyleSheet("QWidget#ControleioEstoque{\n"
"background-color: rgb(59, 117, 176);\n"
"}")
        self.ControleioEstoque.setObjectName("ControleioEstoque")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ControleioEstoque)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.ControleioEstoque)
        self.frame_4.setStyleSheet("QFrame#frame_4{\n"
"border-radius:10px;\n"
"background-color: rgb(59, 117, 176);\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"    border: 2px solid gray;\n"
"    border-radius: 4px;\n"
"\n"
"    \n"
"    font: 900 10pt \"Arial Black\";\n"
"    \n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 9pt \"Arial\";\n"
"}\n"
"QLineEdit {\n"
"    font: 12pt \"Segoe UI\";\n"
"    border: 2px solid gray;\n"
"    border-radius: 4px;\n"
"    padding: 0px 8px;\n"
"    \n"
"    selection-background-color: darkgray;\n"
"}\n"
"QLineEdit:focus{\n"
"    background-color: rgb(199, 199, 199);\n"
"}\n"
"\n"
"QPushButton{\n"
"padding:5px;\n"
"    font: 11pt \"Arial\";\n"
"}\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QListView{\n"
"text-align: center;\n"
"    border:                 none;\n"
"    color:                      rgb(87, 96, 134);\n"
"    background-color:   rgb(255, 255, 255);\n"
"    font-weight:            bold;\n"
"    selection-background-color: rgb(47, 175, 178);\n"
"    show-decoration-selected: 1;\n"
"    margin-left:                -10px;\n"
"    padding-left    :           15px;\n"
"}\n"
"\n"
"QListView::item:hover{\n"
"\n"
"    background-color:   rgb(47, 175, 178);\n"
"    border:                 none;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setStyleSheet("font: 20pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.line_buscaPRodutoestoque = QtWidgets.QLineEdit(self.frame_4)
        self.line_buscaPRodutoestoque.setMinimumSize(QtCore.QSize(0, 50))
        self.line_buscaPRodutoestoque.setStyleSheet("\n"
"")
        self.line_buscaPRodutoestoque.setObjectName("line_buscaPRodutoestoque")
        self.verticalLayout_3.addWidget(self.line_buscaPRodutoestoque)
        self.tab_estoque = QtWidgets.QTableWidget(self.frame_4)
        self.tab_estoque.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tab_estoque.setStyleSheet("QHeaderView, QHeaderView::section {\n"
"   color:white;\n"
"    background-color: #d3d7e4;\n"
"    font: 10pt \"Segoe UI\";\n"
"color:black;\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"QTableWidget{\n"
"    \n"
"    font: 11pt \"Segoe UI\";\n"
"    selection-background-color: rgb(234, 110, 60);\n"
"}\n"
"")
        self.tab_estoque.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab_estoque.setTabKeyNavigation(False)
        self.tab_estoque.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tab_estoque.setShowGrid(False)
        self.tab_estoque.setGridStyle(QtCore.Qt.SolidLine)
        self.tab_estoque.setObjectName("tab_estoque")
        self.tab_estoque.setColumnCount(8)
        self.tab_estoque.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tab_estoque.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_estoque.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_estoque.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_estoque.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_estoque.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_estoque.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_estoque.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_estoque.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_estoque.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_estoque.setHorizontalHeaderItem(7, item)
        self.tab_estoque.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tab_estoque)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_5.setStyleSheet("QFrame#frame_5{\n"
"        background-color: #2b3157;\n"
"border-radius:8px;\n"
"padding:4px;\n"
"}\n"
"QPushButton{\n"
"padding:15px;\n"
"    font: 11pt \"Arial\";\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_incluir = QtWidgets.QPushButton(self.frame_5)
        self.bt_incluir.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_incluir.setObjectName("bt_incluir")
        self.horizontalLayout_2.addWidget(self.bt_incluir)
        self.bt_alterar = QtWidgets.QPushButton(self.frame_5)
        self.bt_alterar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_alterar.setObjectName("bt_alterar")
        self.horizontalLayout_2.addWidget(self.bt_alterar)
        self.bt_imprimir = QtWidgets.QPushButton(self.frame_5)
        self.bt_imprimir.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_imprimir.setObjectName("bt_imprimir")
        self.horizontalLayout_2.addWidget(self.bt_imprimir)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_4)
        self.stackedWidget.addWidget(self.ControleioEstoque)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.frame_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_3.addWidget(self.widget_2)

        self.retranslateUi(form_estoque)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(form_estoque)
        form_estoque.setTabOrder(self.line_descricao, self.line_cod_barra)
        form_estoque.setTabOrder(self.line_cod_barra, self.cb_tipo)
        form_estoque.setTabOrder(self.cb_tipo, self.cb_marca)
        form_estoque.setTabOrder(self.cb_marca, self.cb_grupo)
        form_estoque.setTabOrder(self.cb_grupo, self.cb_unidade)
        form_estoque.setTabOrder(self.cb_unidade, self.linencm)
        form_estoque.setTabOrder(self.linencm, self.db_quantidade)
        form_estoque.setTabOrder(self.db_quantidade, self.dbcompra)
        form_estoque.setTabOrder(self.dbcompra, self.dbcusto)
        form_estoque.setTabOrder(self.dbcusto, self.dbvenda)
        form_estoque.setTabOrder(self.dbvenda, self.ch_ativo)
        form_estoque.setTabOrder(self.ch_ativo, self.ch_pr_desconto)
        form_estoque.setTabOrder(self.ch_pr_desconto, self.tabWidget)
        form_estoque.setTabOrder(self.tabWidget, self.cb_situcao)
        form_estoque.setTabOrder(self.cb_situcao, self.linecfopsaida)
        form_estoque.setTabOrder(self.linecfopsaida, self.linecstsaida)
        form_estoque.setTabOrder(self.linecstsaida, self.line_buscaPRodutoestoque)
        form_estoque.setTabOrder(self.line_buscaPRodutoestoque, self.tab_estoque)

    def retranslateUi(self, form_estoque):
        _translate = QtCore.QCoreApplication.translate
        form_estoque.setWindowTitle(_translate("form_estoque", "Cadastro Estoque"))
        self.bt_closeSistema.setText(_translate("form_estoque", "x"))
        self.bt_closeSistema.setShortcut(_translate("form_estoque", "Esc"))
        self.label.setText(_translate("form_estoque", "Cadastro estoque"))
        self.label_3.setText(_translate("form_estoque", "codigo"))
        self.label_4.setText(_translate("form_estoque", "descricao"))
        self.label_5.setText(_translate("form_estoque", "codigo Barra"))
        self.label_6.setText(_translate("form_estoque", "tipo produto"))
        self.cb_tipo.setItemText(0, _translate("form_estoque", "00-mercadoria para revenda"))
        self.label_7.setText(_translate("form_estoque", "marca"))
        self.label_8.setText(_translate("form_estoque", "grupo"))
        self.label_9.setText(_translate("form_estoque", "unidade"))
        self.label_10.setText(_translate("form_estoque", "ncm"))
        self.label_11.setText(_translate("form_estoque", "compra"))
        self.label_12.setText(_translate("form_estoque", "custo"))
        self.label_13.setText(_translate("form_estoque", "preço venda"))
        self.label_15.setText(_translate("form_estoque", "situaçao tributaria"))
        self.label_16.setText(_translate("form_estoque", "cfop"))
        self.label_17.setText(_translate("form_estoque", "cst"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tributos), _translate("form_estoque", "tributos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fotos), _translate("form_estoque", "fotos"))
        self.label_14.setText(_translate("form_estoque", "Quantidade"))
        self.groupBox.setTitle(_translate("form_estoque", "paramentros"))
        self.ch_ativo.setText(_translate("form_estoque", "ativo"))
        self.ch_pr_desconto.setText(_translate("form_estoque", "desconto produto"))
        self.bt_grava.setText(_translate("form_estoque", "gravar"))
        self.bt_grava.setShortcut(_translate("form_estoque", "F2"))
        self.bt_cancelar.setText(_translate("form_estoque", "cancelar"))
        self.bt_estoque.setText(_translate("form_estoque", "estoque"))
        self.label_2.setText(_translate("form_estoque", "controleio estoque"))
        self.line_buscaPRodutoestoque.setPlaceholderText(_translate("form_estoque", "busca produto"))
        item = self.tab_estoque.verticalHeaderItem(0)
        item.setText(_translate("form_estoque", "New Row"))
        item = self.tab_estoque.verticalHeaderItem(1)
        item.setText(_translate("form_estoque", "New Row"))
        item = self.tab_estoque.horizontalHeaderItem(0)
        item.setText(_translate("form_estoque", "id"))
        item = self.tab_estoque.horizontalHeaderItem(1)
        item.setText(_translate("form_estoque", "codigo"))
        item = self.tab_estoque.horizontalHeaderItem(2)
        item.setText(_translate("form_estoque", "descricao"))
        item = self.tab_estoque.horizontalHeaderItem(3)
        item.setText(_translate("form_estoque", "Quant"))
        item = self.tab_estoque.horizontalHeaderItem(4)
        item.setText(_translate("form_estoque", "Vl Custo"))
        item = self.tab_estoque.horizontalHeaderItem(5)
        item.setText(_translate("form_estoque", "Vl Venda"))
        item = self.tab_estoque.horizontalHeaderItem(6)
        item.setText(_translate("form_estoque", "Desconto"))
        item = self.tab_estoque.horizontalHeaderItem(7)
        item.setText(_translate("form_estoque", "ativo"))
        self.bt_incluir.setText(_translate("form_estoque", "incluir"))
        self.bt_alterar.setText(_translate("form_estoque", "alterar"))
        self.bt_imprimir.setText(_translate("form_estoque", "imprimir"))