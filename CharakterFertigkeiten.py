# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharakterFertigkeiten.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(872, 460)
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setMinimumSize(QtCore.QSize(250, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(225, 16777215))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 246, 436))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 3, 1, 1)
        self.labelAttribute = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setItalic(True)
        self.labelAttribute.setFont(font)
        self.labelAttribute.setObjectName("labelAttribute")
        self.gridLayout_2.addWidget(self.labelAttribute, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.plainText = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainText.setFrameShape(QtWidgets.QFrame.Box)
        self.plainText.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.plainText.setLineWidth(1)
        self.plainText.setReadOnly(True)
        self.plainText.setBackgroundVisible(False)
        self.plainText.setObjectName("plainText")
        self.gridLayout_2.addWidget(self.plainText, 7, 0, 1, 5)
        self.spinFW = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinFW.setAlignment(QtCore.Qt.AlignCenter)
        self.spinFW.setReadOnly(False)
        self.spinFW.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinFW.setObjectName("spinFW")
        self.gridLayout_2.addWidget(self.spinFW, 3, 4, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listTalente = QtWidgets.QListView(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listTalente.sizePolicy().hasHeightForWidth())
        self.listTalente.setSizePolicy(sizePolicy)
        self.listTalente.setMaximumSize(QtCore.QSize(16777215, 80))
        self.listTalente.setObjectName("listTalente")
        self.horizontalLayout.addWidget(self.listTalente)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 5)
        self.spinBasis = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBasis.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBasis.setReadOnly(True)
        self.spinBasis.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBasis.setObjectName("spinBasis")
        self.gridLayout_2.addWidget(self.spinBasis, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.spinPWT = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinPWT.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinPWT.setReadOnly(True)
        self.spinPWT.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinPWT.setObjectName("spinPWT")
        self.gridLayout_2.addWidget(self.spinPWT, 4, 4, 1, 1)
        self.spinSF = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinSF.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinSF.setReadOnly(True)
        self.spinSF.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinSF.setObjectName("spinSF")
        self.gridLayout_2.addWidget(self.spinSF, 2, 4, 1, 1)
        self.spinPW = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinPW.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinPW.setReadOnly(True)
        self.spinPW.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinPW.setObjectName("spinPW")
        self.gridLayout_2.addWidget(self.spinPW, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 3, 1, 1)
        self.labelFertigkeit = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelFertigkeit.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelFertigkeit.setFont(font)
        self.labelFertigkeit.setObjectName("labelFertigkeit")
        self.gridLayout_2.addWidget(self.labelFertigkeit, 0, 0, 1, 5)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 2, 3, 1)
        self.buttonAdd = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.buttonAdd.setMaximumSize(QtCore.QSize(25, 20))
        self.buttonAdd.setObjectName("buttonAdd")
        self.gridLayout_2.addWidget(self.buttonAdd, 5, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 5, 0, 1, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 6, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(80)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setMinimumSectionSize(40)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 5, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.tableWidget, self.scrollArea)
        Form.setTabOrder(self.scrollArea, self.spinSF)
        Form.setTabOrder(self.spinSF, self.spinBasis)
        Form.setTabOrder(self.spinBasis, self.spinFW)
        Form.setTabOrder(self.spinFW, self.spinPW)
        Form.setTabOrder(self.spinPW, self.spinPWT)
        Form.setTabOrder(self.spinPWT, self.buttonAdd)
        Form.setTabOrder(self.buttonAdd, self.listTalente)
        Form.setTabOrder(self.listTalente, self.plainText)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "FW:"))
        self.labelAttribute.setText(_translate("Form", "Attribute"))
        self.label_8.setText(_translate("Form", "PW:"))
        self.label_5.setText(_translate("Form", "SF:"))
        self.label_6.setText(_translate("Form", "Basis:"))
        self.label.setText(_translate("Form", "PW(T):"))
        self.labelFertigkeit.setText(_translate("Form", "Fertigkeit"))
        self.buttonAdd.setText(_translate("Form", "+"))
        self.label_9.setText(_translate("Form", "Erworbene Talente:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Fertigkeitsname"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "FW"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Talente"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
