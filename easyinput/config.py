# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_config_panel(object):
    def setupUi(self, config_panel):
        config_panel.setObjectName("config_panel")
        config_panel.resize(538, 421)
        config_panel.setMinimumSize(QtCore.QSize(538, 421))
        config_panel.setMaximumSize(QtCore.QSize(538, 421))
        self.layoutWidget = QtWidgets.QWidget(config_panel)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 370, 201, 44))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.close = QtWidgets.QPushButton(self.layoutWidget)
        self.close.setObjectName("close")
        self.horizontalLayout_7.addWidget(self.close)
        self.save = QtWidgets.QPushButton(self.layoutWidget)
        self.save.setObjectName("save")
        self.horizontalLayout_7.addWidget(self.save)
        self.layoutWidget1 = QtWidgets.QWidget(config_panel)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 12, 521, 341))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.font_size = QtWidgets.QSpinBox(self.layoutWidget1)
        self.font_size.setMinimumSize(QtCore.QSize(200, 40))
        self.font_size.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.font_size.setFont(font)
        self.font_size.setObjectName("font_size")
        self.horizontalLayout.addWidget(self.font_size)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.windowW = QtWidgets.QSpinBox(self.layoutWidget1)
        self.windowW.setMinimumSize(QtCore.QSize(200, 30))
        self.windowW.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.windowW.setFont(font)
        self.windowW.setMinimum(0)
        self.windowW.setMaximum(1000)
        self.windowW.setObjectName("windowW")
        self.horizontalLayout_2.addWidget(self.windowW)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.windowH = QtWidgets.QSpinBox(self.layoutWidget1)
        self.windowH.setMinimumSize(QtCore.QSize(200, 30))
        self.windowH.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.windowH.setFont(font)
        self.windowH.setMaximum(1000)
        self.windowH.setObjectName("windowH")
        self.horizontalLayout_3.addWidget(self.windowH)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.windowOpacity = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.windowOpacity.setMinimumSize(QtCore.QSize(200, 40))
        self.windowOpacity.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.windowOpacity.setFont(font)
        self.windowOpacity.setMaximum(1.0)
        self.windowOpacity.setSingleStep(0.1)
        self.windowOpacity.setObjectName("windowOpacity")
        self.horizontalLayout_4.addWidget(self.windowOpacity)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.background = QtWidgets.QLineEdit(self.layoutWidget1)
        self.background.setMaximumSize(QtCore.QSize(170, 16777215))
        self.background.setObjectName("background")
        self.horizontalLayout_5.addWidget(self.background)
        self.ch_backcolor = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch_backcolor.setMaximumSize(QtCore.QSize(20, 37))
        self.ch_backcolor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch_backcolor.setText("")
        self.ch_backcolor.setObjectName("ch_backcolor")
        self.horizontalLayout_5.addWidget(self.ch_backcolor)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.font_color = QtWidgets.QLineEdit(self.layoutWidget1)
        self.font_color.setMaximumSize(QtCore.QSize(170, 16777215))
        self.font_color.setObjectName("font_color")
        self.horizontalLayout_6.addWidget(self.font_color)
        self.ch_font_color = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch_font_color.setMaximumSize(QtCore.QSize(20, 37))
        self.ch_font_color.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch_font_color.setText("")
        self.ch_font_color.setObjectName("ch_font_color")
        self.horizontalLayout_6.addWidget(self.ch_font_color)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(config_panel)
        QtCore.QMetaObject.connectSlotsByName(config_panel)

    def retranslateUi(self, config_panel):
        _translate = QtCore.QCoreApplication.translate
        config_panel.setWindowTitle(_translate("config_panel", "Dialog"))
        self.close.setText(_translate("config_panel", "关闭"))
        self.save.setText(_translate("config_panel", "保存"))
        self.label.setText(_translate("config_panel", "字体大小"))
        self.label_2.setText(_translate("config_panel", "窗口宽"))
        self.label_3.setText(_translate("config_panel", "窗口高"))
        self.label_4.setText(_translate("config_panel", "窗口透明度"))
        self.label_5.setText(_translate("config_panel", "背景颜色"))
        self.label_6.setText(_translate("config_panel", "字体颜色"))
