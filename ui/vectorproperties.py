# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\minorua\QGIS\plugins\Qgis2threejs\ui\vectorproperties.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VectorPropertiesWidget(object):
    def setupUi(self, VectorPropertiesWidget):
        VectorPropertiesWidget.setObjectName("VectorPropertiesWidget")
        VectorPropertiesWidget.resize(451, 705)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(VectorPropertiesWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(VectorPropertiesWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_Type = QtWidgets.QFormLayout()
        self.formLayout_Type.setContentsMargins(13, -1, 13, -1)
        self.formLayout_Type.setObjectName("formLayout_Type")
        self.label_ObjectType = QtWidgets.QLabel(self.tab)
        self.label_ObjectType.setMinimumSize(QtCore.QSize(60, 0))
        self.label_ObjectType.setObjectName("label_ObjectType")
        self.formLayout_Type.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_ObjectType)
        self.comboBox_ObjectType = QtWidgets.QComboBox(self.tab)
        self.comboBox_ObjectType.setObjectName("comboBox_ObjectType")
        self.formLayout_Type.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_ObjectType)
        self.verticalLayout.addLayout(self.formLayout_Type)
        self.groupBox_zCoordinate = QtWidgets.QGroupBox(self.tab)
        self.groupBox_zCoordinate.setObjectName("groupBox_zCoordinate")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_zCoordinate)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_Mode = QtWidgets.QLabel(self.groupBox_zCoordinate)
        self.label_Mode.setMinimumSize(QtCore.QSize(60, 0))
        self.label_Mode.setObjectName("label_Mode")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_Mode)
        self.comboBox_altitudeMode = QtWidgets.QComboBox(self.groupBox_zCoordinate)
        self.comboBox_altitudeMode.setObjectName("comboBox_altitudeMode")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_altitudeMode)
        self.label_Altitude = QtWidgets.QLabel(self.groupBox_zCoordinate)
        self.label_Altitude.setMinimumSize(QtCore.QSize(60, 0))
        self.label_Altitude.setObjectName("label_Altitude")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_Altitude)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_Expression = QtWidgets.QRadioButton(self.groupBox_zCoordinate)
        self.radioButton_Expression.setChecked(True)
        self.radioButton_Expression.setObjectName("radioButton_Expression")
        self.buttonGroup_altitude = QtWidgets.QButtonGroup(VectorPropertiesWidget)
        self.buttonGroup_altitude.setObjectName("buttonGroup_altitude")
        self.buttonGroup_altitude.addButton(self.radioButton_Expression)
        self.horizontalLayout_2.addWidget(self.radioButton_Expression)
        self.radioButton_zValue = QtWidgets.QRadioButton(self.groupBox_zCoordinate)
        self.radioButton_zValue.setObjectName("radioButton_zValue")
        self.buttonGroup_altitude.addButton(self.radioButton_zValue)
        self.horizontalLayout_2.addWidget(self.radioButton_zValue)
        self.radioButton_mValue = QtWidgets.QRadioButton(self.groupBox_zCoordinate)
        self.radioButton_mValue.setObjectName("radioButton_mValue")
        self.buttonGroup_altitude.addButton(self.radioButton_mValue)
        self.horizontalLayout_2.addWidget(self.radioButton_mValue)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.fieldExpressionWidget_altitude = QgsFieldExpressionWidget(self.groupBox_zCoordinate)
        self.fieldExpressionWidget_altitude.setMinimumSize(QtCore.QSize(0, 20))
        self.fieldExpressionWidget_altitude.setObjectName("fieldExpressionWidget_altitude")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fieldExpressionWidget_altitude)
        self.label_zExpression = QtWidgets.QLabel(self.groupBox_zCoordinate)
        self.label_zExpression.setMinimumSize(QtCore.QSize(60, 0))
        self.label_zExpression.setObjectName("label_zExpression")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_zExpression)
        self.verticalLayout_8.addLayout(self.formLayout)
        self.comboEdit_altitude2 = PropertyWidget(self.groupBox_zCoordinate)
        self.comboEdit_altitude2.setObjectName("comboEdit_altitude2")
        self.verticalLayout_8.addWidget(self.comboEdit_altitude2)
        self.verticalLayout.addWidget(self.groupBox_zCoordinate)
        self.groupBox_FilePath = QtWidgets.QGroupBox(self.tab)
        self.groupBox_FilePath.setObjectName("groupBox_FilePath")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_FilePath)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.comboEdit_FilePath = PropertyWidget(self.groupBox_FilePath)
        self.comboEdit_FilePath.setObjectName("comboEdit_FilePath")
        self.verticalLayout_6.addWidget(self.comboEdit_FilePath)
        self.verticalLayout.addWidget(self.groupBox_FilePath)
        self.groupBox_Geometry = QtWidgets.QGroupBox(self.tab)
        self.groupBox_Geometry.setObjectName("groupBox_Geometry")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_Geometry)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_Geometry = QtWidgets.QVBoxLayout()
        self.verticalLayout_Geometry.setObjectName("verticalLayout_Geometry")
        self.verticalLayout_7.addLayout(self.verticalLayout_Geometry)
        self.verticalLayout.addWidget(self.groupBox_Geometry)
        self.groupBox_Material = QtWidgets.QGroupBox(self.tab)
        self.groupBox_Material.setObjectName("groupBox_Material")
        self.verticalLayout_Material = QtWidgets.QVBoxLayout(self.groupBox_Material)
        self.verticalLayout_Material.setObjectName("verticalLayout_Material")
        self.comboEdit_Color = PropertyWidget(self.groupBox_Material)
        self.comboEdit_Color.setObjectName("comboEdit_Color")
        self.verticalLayout_Material.addWidget(self.comboEdit_Color)
        self.comboEdit_Color2 = PropertyWidget(self.groupBox_Material)
        self.comboEdit_Color2.setObjectName("comboEdit_Color2")
        self.verticalLayout_Material.addWidget(self.comboEdit_Color2)
        self.comboEdit_Opacity = PropertyWidget(self.groupBox_Material)
        self.comboEdit_Opacity.setObjectName("comboEdit_Opacity")
        self.verticalLayout_Material.addWidget(self.comboEdit_Opacity)
        self.verticalLayout.addWidget(self.groupBox_Material)
        self.groupBox_Features = QtWidgets.QGroupBox(self.tab)
        self.groupBox_Features.setObjectName("groupBox_Features")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_Features)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_AllFeatures = QtWidgets.QRadioButton(self.groupBox_Features)
        self.radioButton_AllFeatures.setObjectName("radioButton_AllFeatures")
        self.verticalLayout_3.addWidget(self.radioButton_AllFeatures)
        self.radioButton_IntersectingFeatures = QtWidgets.QRadioButton(self.groupBox_Features)
        self.radioButton_IntersectingFeatures.setChecked(True)
        self.radioButton_IntersectingFeatures.setObjectName("radioButton_IntersectingFeatures")
        self.verticalLayout_3.addWidget(self.radioButton_IntersectingFeatures)
        self.verticalLayout_Feature = QtWidgets.QVBoxLayout()
        self.verticalLayout_Feature.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_Feature.setObjectName("verticalLayout_Feature")
        self.checkBox_Clip = QtWidgets.QCheckBox(self.groupBox_Features)
        self.checkBox_Clip.setChecked(True)
        self.checkBox_Clip.setObjectName("checkBox_Clip")
        self.verticalLayout_Feature.addWidget(self.checkBox_Clip)
        self.verticalLayout_3.addLayout(self.verticalLayout_Feature)
        self.line = QtWidgets.QFrame(self.groupBox_Features)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.checkBox_ExportAttrs = QtWidgets.QCheckBox(self.groupBox_Features)
        self.checkBox_ExportAttrs.setChecked(False)
        self.checkBox_ExportAttrs.setObjectName("checkBox_ExportAttrs")
        self.verticalLayout_3.addWidget(self.checkBox_ExportAttrs)
        self.verticalLayout.addWidget(self.groupBox_Features)
        self.groupBox_Others = QtWidgets.QGroupBox(self.tab)
        self.groupBox_Others.setObjectName("groupBox_Others")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_Others)
        self.gridLayout.setObjectName("gridLayout")
        self.label_Name = QtWidgets.QLabel(self.groupBox_Others)
        self.label_Name.setMinimumSize(QtCore.QSize(60, 0))
        self.label_Name.setObjectName("label_Name")
        self.gridLayout.addWidget(self.label_Name, 0, 0, 1, 1)
        self.checkBox_Visible = QtWidgets.QCheckBox(self.groupBox_Others)
        self.checkBox_Visible.setChecked(True)
        self.checkBox_Visible.setObjectName("checkBox_Visible")
        self.gridLayout.addWidget(self.checkBox_Visible, 2, 0, 1, 2)
        self.lineEdit_Name = QtWidgets.QLineEdit(self.groupBox_Others)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.gridLayout.addWidget(self.lineEdit_Name, 0, 1, 1, 1)
        self.checkBox_Clickable = QtWidgets.QCheckBox(self.groupBox_Others)
        self.checkBox_Clickable.setChecked(True)
        self.checkBox_Clickable.setObjectName("checkBox_Clickable")
        self.gridLayout.addWidget(self.checkBox_Clickable, 3, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_Others)
        self.tabWidget.addTab(self.tab, "")
        self.tab_Label = QtWidgets.QWidget()
        self.tab_Label.setObjectName("tab_Label")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_Label)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_Label = QtWidgets.QCheckBox(self.tab_Label)
        self.checkBox_Label.setObjectName("checkBox_Label")
        self.verticalLayout_2.addWidget(self.checkBox_Label)
        self.groupBox_Position = QtWidgets.QGroupBox(self.tab_Label)
        self.groupBox_Position.setObjectName("groupBox_Position")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_Position)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelHeightWidget = PropertyWidget(self.groupBox_Position)
        self.labelHeightWidget.setMinimumSize(QtCore.QSize(0, 10))
        self.labelHeightWidget.setObjectName("labelHeightWidget")
        self.verticalLayout_4.addWidget(self.labelHeightWidget)
        self.verticalLayout_2.addWidget(self.groupBox_Position)
        self.groupBox_LabelText = QtWidgets.QGroupBox(self.tab_Label)
        self.groupBox_LabelText.setObjectName("groupBox_LabelText")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_LabelText)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_FontFamily = QtWidgets.QLabel(self.groupBox_LabelText)
        self.label_FontFamily.setObjectName("label_FontFamily")
        self.gridLayout_5.addWidget(self.label_FontFamily, 1, 0, 1, 1)
        self.checkBox_Outline = QtWidgets.QCheckBox(self.groupBox_LabelText)
        self.checkBox_Outline.setChecked(True)
        self.checkBox_Outline.setObjectName("checkBox_Outline")
        self.gridLayout_5.addWidget(self.checkBox_Outline, 5, 1, 1, 4)
        self.label_Outline = QtWidgets.QLabel(self.groupBox_LabelText)
        self.label_Outline.setObjectName("label_Outline")
        self.gridLayout_5.addWidget(self.label_Outline, 5, 0, 1, 1)
        self.label_FontSize = QtWidgets.QLabel(self.groupBox_LabelText)
        self.label_FontSize.setObjectName("label_FontSize")
        self.gridLayout_5.addWidget(self.label_FontSize, 2, 0, 1, 1)
        self.comboBox_FontFamily = QtWidgets.QComboBox(self.groupBox_LabelText)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_FontFamily.sizePolicy().hasHeightForWidth())
        self.comboBox_FontFamily.setSizePolicy(sizePolicy)
        self.comboBox_FontFamily.setObjectName("comboBox_FontFamily")
        self.gridLayout_5.addWidget(self.comboBox_FontFamily, 1, 1, 1, 4)
        self.colorButton_Label = QgsColorButton(self.groupBox_LabelText)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_Label.sizePolicy().hasHeightForWidth())
        self.colorButton_Label.setSizePolicy(sizePolicy)
        self.colorButton_Label.setObjectName("colorButton_Label")
        self.gridLayout_5.addWidget(self.colorButton_Label, 4, 1, 1, 4)
        self.colorButton_OtlColor = QgsColorButton(self.groupBox_LabelText)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_OtlColor.sizePolicy().hasHeightForWidth())
        self.colorButton_OtlColor.setSizePolicy(sizePolicy)
        self.colorButton_OtlColor.setObjectName("colorButton_OtlColor")
        self.gridLayout_5.addWidget(self.colorButton_OtlColor, 6, 1, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.groupBox_LabelText)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 6, 0, 1, 1)
        self.label_LabelColor = QtWidgets.QLabel(self.groupBox_LabelText)
        self.label_LabelColor.setObjectName("label_LabelColor")
        self.gridLayout_5.addWidget(self.label_LabelColor, 4, 0, 1, 1)
        self.label_Text = QtWidgets.QLabel(self.groupBox_LabelText)
        self.label_Text.setMinimumSize(QtCore.QSize(85, 0))
        self.label_Text.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_Text.setObjectName("label_Text")
        self.gridLayout_5.addWidget(self.label_Text, 0, 0, 1, 1)
        self.expression_Label = QgsFieldExpressionWidget(self.groupBox_LabelText)
        self.expression_Label.setMinimumSize(QtCore.QSize(0, 10))
        self.expression_Label.setObjectName("expression_Label")
        self.gridLayout_5.addWidget(self.expression_Label, 0, 1, 1, 4)
        self.slider_FontSize = QtWidgets.QSlider(self.groupBox_LabelText)
        self.slider_FontSize.setMaximum(6)
        self.slider_FontSize.setOrientation(QtCore.Qt.Horizontal)
        self.slider_FontSize.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_FontSize.setObjectName("slider_FontSize")
        self.gridLayout_5.addWidget(self.slider_FontSize, 2, 1, 1, 4)
        self.label = QtWidgets.QLabel(self.groupBox_LabelText)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_LabelText)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 3, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_LabelText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 3, 2, 1, 2)
        self.verticalLayout_2.addWidget(self.groupBox_LabelText)
        self.groupBox_Background = QtWidgets.QGroupBox(self.tab_Label)
        self.groupBox_Background.setCheckable(True)
        self.groupBox_Background.setObjectName("groupBox_Background")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_Background)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_LabelBgColor = QtWidgets.QLabel(self.groupBox_Background)
        self.label_LabelBgColor.setMinimumSize(QtCore.QSize(85, 0))
        self.label_LabelBgColor.setObjectName("label_LabelBgColor")
        self.gridLayout_4.addWidget(self.label_LabelBgColor, 0, 0, 1, 1)
        self.colorButton_BgColor = QgsColorButton(self.groupBox_Background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_BgColor.sizePolicy().hasHeightForWidth())
        self.colorButton_BgColor.setSizePolicy(sizePolicy)
        self.colorButton_BgColor.setObjectName("colorButton_BgColor")
        self.gridLayout_4.addWidget(self.colorButton_BgColor, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_Background)
        self.groupBox_Conn = QtWidgets.QGroupBox(self.tab_Label)
        self.groupBox_Conn.setCheckable(True)
        self.groupBox_Conn.setChecked(True)
        self.groupBox_Conn.setObjectName("groupBox_Conn")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_Conn)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.colorButton_ConnColor = QgsColorButton(self.groupBox_Conn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_ConnColor.sizePolicy().hasHeightForWidth())
        self.colorButton_ConnColor.setSizePolicy(sizePolicy)
        self.colorButton_ConnColor.setObjectName("colorButton_ConnColor")
        self.gridLayout_3.addWidget(self.colorButton_ConnColor, 0, 1, 1, 1)
        self.label_ConnColor = QtWidgets.QLabel(self.groupBox_Conn)
        self.label_ConnColor.setMinimumSize(QtCore.QSize(85, 0))
        self.label_ConnColor.setObjectName("label_ConnColor")
        self.gridLayout_3.addWidget(self.label_ConnColor, 0, 0, 1, 1)
        self.checkBox_Underline = QtWidgets.QCheckBox(self.groupBox_Conn)
        self.checkBox_Underline.setText("")
        self.checkBox_Underline.setObjectName("checkBox_Underline")
        self.gridLayout_3.addWidget(self.checkBox_Underline, 1, 1, 1, 1)
        self.label_Underline = QtWidgets.QLabel(self.groupBox_Conn)
        self.label_Underline.setObjectName("label_Underline")
        self.gridLayout_3.addWidget(self.label_Underline, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_Conn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_Label, "")
        self.verticalLayout_5.addWidget(self.tabWidget)

        self.retranslateUi(VectorPropertiesWidget)
        self.tabWidget.setCurrentIndex(1)
        self.radioButton_IntersectingFeatures.toggled['bool'].connect(self.checkBox_Clip.setEnabled)
        self.checkBox_Outline.toggled['bool'].connect(self.label_Outline.setEnabled)
        self.checkBox_Outline.toggled['bool'].connect(self.colorButton_OtlColor.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(VectorPropertiesWidget)

    def retranslateUi(self, VectorPropertiesWidget):
        _translate = QtCore.QCoreApplication.translate
        VectorPropertiesWidget.setWindowTitle(_translate("VectorPropertiesWidget", "Form"))
        self.label_ObjectType.setText(_translate("VectorPropertiesWidget", "Type"))
        self.groupBox_zCoordinate.setTitle(_translate("VectorPropertiesWidget", "&Z coordinate"))
        self.label_Mode.setText(_translate("VectorPropertiesWidget", "Mode"))
        self.label_Altitude.setText(_translate("VectorPropertiesWidget", "Altitude"))
        self.radioButton_Expression.setText(_translate("VectorPropertiesWidget", "Expression"))
        self.radioButton_zValue.setText(_translate("VectorPropertiesWidget", "Z value"))
        self.radioButton_mValue.setText(_translate("VectorPropertiesWidget", "M value"))
        self.groupBox_FilePath.setTitle(_translate("VectorPropertiesWidget", "File &path"))
        self.groupBox_Geometry.setTitle(_translate("VectorPropertiesWidget", "&Geometry"))
        self.groupBox_Material.setTitle(_translate("VectorPropertiesWidget", "&Material"))
        self.groupBox_Features.setTitle(_translate("VectorPropertiesWidget", "&Features"))
        self.radioButton_AllFeatures.setText(_translate("VectorPropertiesWidget", "All features"))
        self.radioButton_IntersectingFeatures.setText(_translate("VectorPropertiesWidget", "Features that intersect with base extent of the scene"))
        self.checkBox_Clip.setText(_translate("VectorPropertiesWidget", "Clip geometries"))
        self.checkBox_ExportAttrs.setText(_translate("VectorPropertiesWidget", "Export attributes"))
        self.groupBox_Others.setTitle(_translate("VectorPropertiesWidget", "&Other options"))
        self.label_Name.setText(_translate("VectorPropertiesWidget", "Name"))
        self.checkBox_Visible.setText(_translate("VectorPropertiesWidget", "Visible on load"))
        self.checkBox_Clickable.setText(_translate("VectorPropertiesWidget", "Clickable"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("VectorPropertiesWidget", "General"))
        self.checkBox_Label.setText(_translate("VectorPropertiesWidget", "Show labels"))
        self.groupBox_Position.setTitle(_translate("VectorPropertiesWidget", "&Position"))
        self.groupBox_LabelText.setTitle(_translate("VectorPropertiesWidget", "&Text"))
        self.label_FontFamily.setText(_translate("VectorPropertiesWidget", "Font family"))
        self.label_Outline.setText(_translate("VectorPropertiesWidget", "Outline"))
        self.label_FontSize.setText(_translate("VectorPropertiesWidget", "Size"))
        self.label_2.setText(_translate("VectorPropertiesWidget", "Outline color"))
        self.label_LabelColor.setText(_translate("VectorPropertiesWidget", "Color"))
        self.label_Text.setText(_translate("VectorPropertiesWidget", "Text"))
        self.label.setText(_translate("VectorPropertiesWidget", "small"))
        self.label_4.setText(_translate("VectorPropertiesWidget", "large"))
        self.label_3.setText(_translate("VectorPropertiesWidget", "medium"))
        self.groupBox_Background.setTitle(_translate("VectorPropertiesWidget", "Fill &background"))
        self.label_LabelBgColor.setText(_translate("VectorPropertiesWidget", "Fill color"))
        self.groupBox_Conn.setTitle(_translate("VectorPropertiesWidget", "&Connector"))
        self.label_ConnColor.setText(_translate("VectorPropertiesWidget", "Color"))
        self.label_Underline.setText(_translate("VectorPropertiesWidget", "Underline"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Label), _translate("VectorPropertiesWidget", "Labels"))
from Qgis2threejs.propwidget import PropertyWidget
from qgis.gui import QgsColorButton, QgsFieldExpressionWidget
