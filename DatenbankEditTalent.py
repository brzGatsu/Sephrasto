# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatenbankEditTalent.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_talentDialog(object):
    def setupUi(self, talentDialog):
        talentDialog.setObjectName("talentDialog")
        talentDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        talentDialog.resize(381, 304)
        self.gridLayout_2 = QtWidgets.QGridLayout(talentDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nameEdit = QtWidgets.QLineEdit(talentDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.fertigkeitenEdit = QtWidgets.QLineEdit(talentDialog)
        self.fertigkeitenEdit.setObjectName("fertigkeitenEdit")
        self.gridLayout.addWidget(self.fertigkeitenEdit, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(talentDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(talentDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonRegulaer = QtWidgets.QRadioButton(talentDialog)
        self.buttonRegulaer.setChecked(True)
        self.buttonRegulaer.setObjectName("buttonRegulaer")
        self.verticalLayout.addWidget(self.buttonRegulaer)
        self.buttonVerbilligt = QtWidgets.QRadioButton(talentDialog)
        self.buttonVerbilligt.setObjectName("buttonVerbilligt")
        self.verticalLayout.addWidget(self.buttonVerbilligt)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonSpezial = QtWidgets.QRadioButton(talentDialog)
        self.buttonSpezial.setObjectName("buttonSpezial")
        self.horizontalLayout.addWidget(self.buttonSpezial)
        self.spinKosten = QtWidgets.QSpinBox(talentDialog)
        self.spinKosten.setAlignment(QtCore.Qt.AlignCenter)
        self.spinKosten.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinKosten.setMinimum(0)
        self.spinKosten.setMaximum(200)
        self.spinKosten.setSingleStep(20)
        self.spinKosten.setObjectName("spinKosten")
        self.horizontalLayout.addWidget(self.spinKosten)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(talentDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(talentDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.voraussetzungenEdit = QtWidgets.QLineEdit(talentDialog)
        self.voraussetzungenEdit.setObjectName("voraussetzungenEdit")
        self.gridLayout.addWidget(self.voraussetzungenEdit, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(talentDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.textEdit = QtWidgets.QPlainTextEdit(talentDialog)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(talentDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(talentDialog)
        self.buttonBox.accepted.connect(talentDialog.accept)
        self.buttonBox.rejected.connect(talentDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(talentDialog)
        talentDialog.setTabOrder(self.nameEdit, self.buttonRegulaer)
        talentDialog.setTabOrder(self.buttonRegulaer, self.buttonVerbilligt)
        talentDialog.setTabOrder(self.buttonVerbilligt, self.buttonSpezial)
        talentDialog.setTabOrder(self.buttonSpezial, self.fertigkeitenEdit)
        talentDialog.setTabOrder(self.fertigkeitenEdit, self.voraussetzungenEdit)
        talentDialog.setTabOrder(self.voraussetzungenEdit, self.textEdit)

    def retranslateUi(self, talentDialog):
        _translate = QtCore.QCoreApplication.translate
        talentDialog.setWindowTitle(_translate("talentDialog", "Sephrasto - Talent bearbeiten..."))
        self.label.setText(_translate("talentDialog", "Talentname"))
        self.label_2.setText(_translate("talentDialog", "Lernkosten"))
        self.buttonRegulaer.setText(_translate("talentDialog", "Reguläres Talent (Kosten nach Fertigkeit)"))
        self.buttonVerbilligt.setText(_translate("talentDialog", "Verbilligtes Talent (Kosten nach Fertigkeit)"))
        self.buttonSpezial.setText(_translate("talentDialog", "Spezialtalent (Kosten frei wählbar)"))
        self.spinKosten.setSuffix(_translate("talentDialog", " EP"))
        self.label_3.setText(_translate("talentDialog", "Fertigkeiten"))
        self.label_4.setText(_translate("talentDialog", "Voraussetzungen"))
        self.label_5.setText(_translate("talentDialog", "Text"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    talentDialog = QtWidgets.QDialog()
    ui = Ui_talentDialog()
    ui.setupUi(talentDialog)
    talentDialog.show()
    sys.exit(app.exec_())

