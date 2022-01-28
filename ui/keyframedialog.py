# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\minorua\QGIS\plugins\Qgis2threejs\ui\keyframedialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KeyframeDialog(object):
    def setupUi(self, KeyframeDialog):
        KeyframeDialog.setObjectName("KeyframeDialog")
        KeyframeDialog.resize(500, 440)
        KeyframeDialog.setMinimumSize(QtCore.QSize(500, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(KeyframeDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButtonPrev = QtWidgets.QToolButton(KeyframeDialog)
        self.toolButtonPrev.setObjectName("toolButtonPrev")
        self.horizontalLayout.addWidget(self.toolButtonPrev)
        self.horizontalSlider = QtWidgets.QSlider(KeyframeDialog)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(0, 30))
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.toolButtonNext = QtWidgets.QToolButton(KeyframeDialog)
        self.toolButtonNext.setObjectName("toolButtonNext")
        self.horizontalLayout.addWidget(self.toolButtonNext)
        self.lineEditCurrentTrans = QtWidgets.QLineEdit(KeyframeDialog)
        self.lineEditCurrentTrans.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEditCurrentTrans.setReadOnly(True)
        self.lineEditCurrentTrans.setObjectName("lineEditCurrentTrans")
        self.horizontalLayout.addWidget(self.lineEditCurrentTrans)
        self.labelTransCount = QtWidgets.QLabel(KeyframeDialog)
        self.labelTransCount.setObjectName("labelTransCount")
        self.horizontalLayout.addWidget(self.labelTransCount)
        self.pushButtonPlay = QtWidgets.QPushButton(KeyframeDialog)
        self.pushButtonPlay.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButtonPlay.setObjectName("pushButtonPlay")
        self.horizontalLayout.addWidget(self.pushButtonPlay)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line2 = QtWidgets.QFrame(KeyframeDialog)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.verticalLayout.addWidget(self.line2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutLeft = QtWidgets.QGridLayout()
        self.gridLayoutLeft.setVerticalSpacing(7)
        self.gridLayoutLeft.setObjectName("gridLayoutLeft")
        self.labelName = QtWidgets.QLabel(KeyframeDialog)
        self.labelName.setMinimumSize(QtCore.QSize(60, 0))
        self.labelName.setObjectName("labelName")
        self.gridLayoutLeft.addWidget(self.labelName, 0, 0, 1, 1)
        self.doubleSpinBoxOpacity = QtWidgets.QDoubleSpinBox(KeyframeDialog)
        self.doubleSpinBoxOpacity.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.doubleSpinBoxOpacity.setDecimals(1)
        self.doubleSpinBoxOpacity.setMaximum(1.0)
        self.doubleSpinBoxOpacity.setSingleStep(0.1)
        self.doubleSpinBoxOpacity.setProperty("value", 1.0)
        self.doubleSpinBoxOpacity.setObjectName("doubleSpinBoxOpacity")
        self.gridLayoutLeft.addWidget(self.doubleSpinBoxOpacity, 1, 1, 1, 1)
        self.comboBoxMaterial = QtWidgets.QComboBox(KeyframeDialog)
        self.comboBoxMaterial.setObjectName("comboBoxMaterial")
        self.gridLayoutLeft.addWidget(self.comboBoxMaterial, 2, 1, 1, 1)
        self.labelEffect = QtWidgets.QLabel(KeyframeDialog)
        self.labelEffect.setMinimumSize(QtCore.QSize(60, 0))
        self.labelEffect.setObjectName("labelEffect")
        self.gridLayoutLeft.addWidget(self.labelEffect, 3, 0, 1, 1)
        self.lineEditName = QtWidgets.QLineEdit(KeyframeDialog)
        self.lineEditName.setObjectName("lineEditName")
        self.gridLayoutLeft.addWidget(self.lineEditName, 0, 1, 1, 1)
        self.labelMaterial = QtWidgets.QLabel(KeyframeDialog)
        self.labelMaterial.setMinimumSize(QtCore.QSize(60, 0))
        self.labelMaterial.setObjectName("labelMaterial")
        self.gridLayoutLeft.addWidget(self.labelMaterial, 2, 0, 1, 1)
        self.comboBoxEffect = QtWidgets.QComboBox(KeyframeDialog)
        self.comboBoxEffect.setObjectName("comboBoxEffect")
        self.gridLayoutLeft.addWidget(self.comboBoxEffect, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayoutLeft.addItem(spacerItem, 6, 0, 1, 2)
        self.labelOpacity = QtWidgets.QLabel(KeyframeDialog)
        self.labelOpacity.setMinimumSize(QtCore.QSize(60, 0))
        self.labelOpacity.setObjectName("labelOpacity")
        self.gridLayoutLeft.addWidget(self.labelOpacity, 1, 0, 1, 1)
        self.labelNarration = QtWidgets.QLabel(KeyframeDialog)
        self.labelNarration.setObjectName("labelNarration")
        self.gridLayoutLeft.addWidget(self.labelNarration, 4, 0, 1, 2)
        self.textEdit = QtWidgets.QTextEdit(KeyframeDialog)
        self.textEdit.setObjectName("textEdit")
        self.gridLayoutLeft.addWidget(self.textEdit, 5, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayoutLeft, 0, 0, 1, 2)
        self.gridLayoutRight = QtWidgets.QGridLayout()
        self.gridLayoutRight.setVerticalSpacing(7)
        self.gridLayoutRight.setObjectName("gridLayoutRight")
        self.lineEditName2 = QtWidgets.QLineEdit(KeyframeDialog)
        self.lineEditName2.setMinimumSize(QtCore.QSize(140, 0))
        self.lineEditName2.setObjectName("lineEditName2")
        self.gridLayoutRight.addWidget(self.lineEditName2, 0, 1, 1, 1)
        self.doubleSpinBoxOpacity2 = QtWidgets.QDoubleSpinBox(KeyframeDialog)
        self.doubleSpinBoxOpacity2.setMinimumSize(QtCore.QSize(140, 0))
        self.doubleSpinBoxOpacity2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.doubleSpinBoxOpacity2.setDecimals(1)
        self.doubleSpinBoxOpacity2.setMaximum(1.0)
        self.doubleSpinBoxOpacity2.setSingleStep(0.1)
        self.doubleSpinBoxOpacity2.setProperty("value", 1.0)
        self.doubleSpinBoxOpacity2.setObjectName("doubleSpinBoxOpacity2")
        self.gridLayoutRight.addWidget(self.doubleSpinBoxOpacity2, 1, 1, 1, 1)
        self.labelMaterial2 = QtWidgets.QLabel(KeyframeDialog)
        self.labelMaterial2.setMinimumSize(QtCore.QSize(60, 0))
        self.labelMaterial2.setObjectName("labelMaterial2")
        self.gridLayoutRight.addWidget(self.labelMaterial2, 2, 0, 1, 1)
        self.labelOpacity2 = QtWidgets.QLabel(KeyframeDialog)
        self.labelOpacity2.setMinimumSize(QtCore.QSize(60, 0))
        self.labelOpacity2.setObjectName("labelOpacity2")
        self.gridLayoutRight.addWidget(self.labelOpacity2, 1, 0, 1, 1)
        self.comboBoxMaterial2 = QtWidgets.QComboBox(KeyframeDialog)
        self.comboBoxMaterial2.setMinimumSize(QtCore.QSize(140, 0))
        self.comboBoxMaterial2.setObjectName("comboBoxMaterial2")
        self.gridLayoutRight.addWidget(self.comboBoxMaterial2, 2, 1, 1, 1)
        self.labelName2 = QtWidgets.QLabel(KeyframeDialog)
        self.labelName2.setMinimumSize(QtCore.QSize(60, 0))
        self.labelName2.setObjectName("labelName2")
        self.gridLayoutRight.addWidget(self.labelName2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayoutRight.addItem(spacerItem1, 5, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayoutRight, 0, 3, 1, 2)
        self.labelArrow = QtWidgets.QLabel(KeyframeDialog)
        self.labelArrow.setMaximumSize(QtCore.QSize(30, 16777215))
        self.labelArrow.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelArrow.setObjectName("labelArrow")
        self.gridLayout.addWidget(self.labelArrow, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout2 = QtWidgets.QGridLayout()
        self.gridLayout2.setObjectName("gridLayout2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout2.addItem(spacerItem2, 0, 4, 1, 1)
        self.verticalLayout2 = QtWidgets.QVBoxLayout()
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.labelDelay = QtWidgets.QLabel(KeyframeDialog)
        self.labelDelay.setObjectName("labelDelay")
        self.verticalLayout2.addWidget(self.labelDelay)
        self.lineEditDelay = QtWidgets.QLineEdit(KeyframeDialog)
        self.lineEditDelay.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditDelay.setObjectName("lineEditDelay")
        self.verticalLayout2.addWidget(self.lineEditDelay)
        self.gridLayout2.addLayout(self.verticalLayout2, 0, 0, 1, 1)
        self.verticalLayout3 = QtWidgets.QVBoxLayout()
        self.verticalLayout3.setContentsMargins(-1, -1, 100, -1)
        self.verticalLayout3.setObjectName("verticalLayout3")
        self.labelDuration = QtWidgets.QLabel(KeyframeDialog)
        self.labelDuration.setObjectName("labelDuration")
        self.verticalLayout3.addWidget(self.labelDuration)
        self.lineEditDuration = QtWidgets.QLineEdit(KeyframeDialog)
        self.lineEditDuration.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditDuration.setObjectName("lineEditDuration")
        self.verticalLayout3.addWidget(self.lineEditDuration)
        self.gridLayout2.addLayout(self.verticalLayout3, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout2.addItem(spacerItem3, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelBegin = QtWidgets.QLabel(KeyframeDialog)
        self.labelBegin.setMinimumSize(QtCore.QSize(50, 0))
        self.labelBegin.setObjectName("labelBegin")
        self.horizontalLayout_2.addWidget(self.labelBegin)
        self.labelTimeBegin = QtWidgets.QLabel(KeyframeDialog)
        self.labelTimeBegin.setMinimumSize(QtCore.QSize(80, 0))
        self.labelTimeBegin.setObjectName("labelTimeBegin")
        self.horizontalLayout_2.addWidget(self.labelTimeBegin)
        self.labelEnd = QtWidgets.QLabel(KeyframeDialog)
        self.labelEnd.setMinimumSize(QtCore.QSize(50, 0))
        self.labelEnd.setObjectName("labelEnd")
        self.horizontalLayout_2.addWidget(self.labelEnd)
        self.labelTimeEnd = QtWidgets.QLabel(KeyframeDialog)
        self.labelTimeEnd.setMinimumSize(QtCore.QSize(80, 0))
        self.labelTimeEnd.setObjectName("labelTimeEnd")
        self.horizontalLayout_2.addWidget(self.labelTimeEnd)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(KeyframeDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout3.setObjectName("horizontalLayout3")
        self.pushButtonPlayAll = QtWidgets.QPushButton(KeyframeDialog)
        self.pushButtonPlayAll.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButtonPlayAll.setObjectName("pushButtonPlayAll")
        self.horizontalLayout3.addWidget(self.pushButtonPlayAll)
        self.label = QtWidgets.QLabel(KeyframeDialog)
        self.label.setObjectName("label")
        self.horizontalLayout3.addWidget(self.label)
        self.labelTotal = QtWidgets.QLabel(KeyframeDialog)
        self.labelTotal.setObjectName("labelTotal")
        self.horizontalLayout3.addWidget(self.labelTotal)
        self.buttonBox = QtWidgets.QDialogButtonBox(KeyframeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout3.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout3)

        self.retranslateUi(KeyframeDialog)
        self.buttonBox.accepted.connect(KeyframeDialog.accept)
        self.buttonBox.rejected.connect(KeyframeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(KeyframeDialog)

    def retranslateUi(self, KeyframeDialog):
        _translate = QtCore.QCoreApplication.translate
        KeyframeDialog.setWindowTitle(_translate("KeyframeDialog", "Keyframe"))
        self.toolButtonPrev.setText(_translate("KeyframeDialog", "<"))
        self.toolButtonNext.setText(_translate("KeyframeDialog", ">"))
        self.lineEditCurrentTrans.setText(_translate("KeyframeDialog", "1"))
        self.labelTransCount.setText(_translate("KeyframeDialog", "/ N"))
        self.pushButtonPlay.setText(_translate("KeyframeDialog", "Play"))
        self.labelName.setText(_translate("KeyframeDialog", "Name"))
        self.labelEffect.setText(_translate("KeyframeDialog", "Effect"))
        self.labelMaterial.setText(_translate("KeyframeDialog", "Material"))
        self.labelOpacity.setText(_translate("KeyframeDialog", "Opacity"))
        self.labelNarration.setText(_translate("KeyframeDialog", "Narrative content"))
        self.labelMaterial2.setText(_translate("KeyframeDialog", "Material"))
        self.labelOpacity2.setText(_translate("KeyframeDialog", "Opacity"))
        self.labelName2.setText(_translate("KeyframeDialog", "Name"))
        self.labelArrow.setText(_translate("KeyframeDialog", "\n"
"->"))
        self.labelDelay.setText(_translate("KeyframeDialog", "Delay (msec)"))
        self.lineEditDelay.setText(_translate("KeyframeDialog", "0"))
        self.labelDuration.setText(_translate("KeyframeDialog", "Duration (msec)"))
        self.lineEditDuration.setText(_translate("KeyframeDialog", "1000"))
        self.labelBegin.setText(_translate("KeyframeDialog", "Begin: "))
        self.labelTimeBegin.setText(_translate("KeyframeDialog", "00:00.000"))
        self.labelEnd.setText(_translate("KeyframeDialog", "End:"))
        self.labelTimeEnd.setText(_translate("KeyframeDialog", "00:01.000"))
        self.pushButtonPlayAll.setText(_translate("KeyframeDialog", "Play all"))
        self.label.setText(_translate("KeyframeDialog", "Total time:"))
        self.labelTotal.setText(_translate("KeyframeDialog", "00:15.000"))
