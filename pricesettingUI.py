# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\program\autopaipai\pricesetting.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(240, 320)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtBidTime = QtWidgets.QLineEdit(Dialog)
        self.txtBidTime.setObjectName("txtBidTime")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtBidTime)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtAttrackLastTime = QtWidgets.QLineEdit(Dialog)
        self.txtAttrackLastTime.setObjectName("txtAttrackLastTime")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtAttrackLastTime)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.txtRaisePrice = QtWidgets.QLineEdit(Dialog)
        self.txtRaisePrice.setObjectName("txtRaisePrice")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtRaisePrice)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "加价设置"))
        self.label.setText(_translate("Dialog", "加价幅度"))
        self.label_2.setText(_translate("Dialog", "加价时间"))
        self.label_3.setText(_translate("Dialog", "最后出价"))
        self.label_4.setText(_translate("Dialog", "元"))
        self.label_5.setText(_translate("Dialog", "秒"))
        self.label_6.setText(_translate("Dialog", "秒"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

