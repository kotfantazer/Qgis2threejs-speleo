# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\minorua\QGIS\plugins\Qgis2threejs\ui\keyframegroupdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KeyframeGroupDialog(object):
    def setupUi(self, KeyframeGroupDialog):
        KeyframeGroupDialog.setObjectName("KeyframeGroupDialog")
        KeyframeGroupDialog.resize(399, 108)
        self.verticalLayout = QtWidgets.QVBoxLayout(KeyframeGroupDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(KeyframeGroupDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditName = QtWidgets.QLineEdit(KeyframeGroupDialog)
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditName)
        self.label_2 = QtWidgets.QLabel(KeyframeGroupDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBoxEasing = QtWidgets.QComboBox(KeyframeGroupDialog)
        self.comboBoxEasing.setObjectName("comboBoxEasing")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxEasing)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(KeyframeGroupDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(KeyframeGroupDialog)
        self.buttonBox.accepted.connect(KeyframeGroupDialog.accept)
        self.buttonBox.rejected.connect(KeyframeGroupDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(KeyframeGroupDialog)

    def retranslateUi(self, KeyframeGroupDialog):
        _translate = QtCore.QCoreApplication.translate
        KeyframeGroupDialog.setWindowTitle(_translate("KeyframeGroupDialog", "Keyframe Group"))
        self.label.setText(_translate("KeyframeGroupDialog", "Name"))
        self.label_2.setText(_translate("KeyframeGroupDialog", "Easing function"))
