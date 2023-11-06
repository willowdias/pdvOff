# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout/ui/FormPdf.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_pdf_gerado(object):
    def setupUi(self, form_pdf_gerado):
        form_pdf_gerado.setObjectName("form_pdf_gerado")
        form_pdf_gerado.setWindowModality(QtCore.Qt.WindowModal)
        form_pdf_gerado.resize(682, 642)
        form_pdf_gerado.setStyleSheet("QWidget#form_pdf_gerado{\n"
"text-transform: uppercase;\n"
"    background-color: #2b3157;\n"
"\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(form_pdf_gerado)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(form_pdf_gerado)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background-color: #2b3157;\n"
"border-radius:0px;\n"
"padding:4px;\n"
"text-transform: uppercase;\n"
"}\n"
"QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"border: none;\n"
"}\n"
"QToolButton{\n"
"padding:5px;\n"
"font: 11pt \"Arial\";\n"
"text-transform: uppercase;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tol_menu = QtWidgets.QToolButton(self.frame_2)
        self.tol_menu.setStyleSheet("")
        self.tol_menu.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.tol_menu.setObjectName("tol_menu")
        self.horizontalLayout_2.addWidget(self.tol_menu)
        self.lb_receberNome = QtWidgets.QLabel(self.frame_2)
        self.lb_receberNome.setMinimumSize(QtCore.QSize(80, 0))
        self.lb_receberNome.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_receberNome.setObjectName("lb_receberNome")
        self.horizontalLayout_2.addWidget(self.lb_receberNome)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(form_pdf_gerado)
        self.frame_4.setStyleSheet("text-transform: uppercase;\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frame_4)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.web_browser = QtWebEngineWidgets.QWebEngineView(self.frame)
        self.web_browser.setMinimumSize(QtCore.QSize(0, 0))
        self.web_browser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.web_browser.setStyleSheet("border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid white;")
        self.web_browser.setObjectName("web_browser")
        self.verticalLayout.addWidget(self.web_browser)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.actionimprimir = QtWidgets.QAction(form_pdf_gerado)
        self.actionimprimir.setObjectName("actionimprimir")
        self.actionenvia_email = QtWidgets.QAction(form_pdf_gerado)
        self.actionenvia_email.setObjectName("actionenvia_email")
        self.actionsalvar_pdf = QtWidgets.QAction(form_pdf_gerado)
        self.actionsalvar_pdf.setObjectName("actionsalvar_pdf")

        self.retranslateUi(form_pdf_gerado)
        QtCore.QMetaObject.connectSlotsByName(form_pdf_gerado)

    def retranslateUi(self, form_pdf_gerado):
        _translate = QtCore.QCoreApplication.translate
        form_pdf_gerado.setWindowTitle(_translate("form_pdf_gerado", "Pdf"))
        self.tol_menu.setText(_translate("form_pdf_gerado", "Arquivo"))
        self.lb_receberNome.setText(_translate("form_pdf_gerado", "nome"))
        self.actionimprimir.setText(_translate("form_pdf_gerado", "IMPRIMIR"))
        self.actionenvia_email.setText(_translate("form_pdf_gerado", "ENVIA EMAIL"))
        self.actionsalvar_pdf.setText(_translate("form_pdf_gerado", "SALVAR PDF"))
from PyQt5 import QtWebEngineWidgets