# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE_NEW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1142, 733)
        MainWindow.setMinimumSize(QSize(1050, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush11 = QBrush(QColor(51, 153, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(210, 210, 210);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(24, 112, 180);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(112, 130, 173);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: "
                        "20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: "
                        "rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	bor"
                        "der-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	c"
                        "olor: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::ha"
                        "ndle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(110, 137, 165)")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(56, 108, 141)\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 133, 194);\n"
"\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgb(56, 108, 141)\n"
"")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(0, 133, 194);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 133, 194);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 133, 194);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(110, 137, 165)")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(187, 207, 227);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color:  rgb(225, 225, 225);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(110, 137, 165)")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color:  rgb(225, 225, 225);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.frame_15 = QFrame(self.page_5)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(10, 0, 1011, 578))
        self.frame_15.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(450, 170, 441, 131))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_16)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.frame_17)
        self.label_15.setObjectName(u"label_15")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_15.setFont(font4)
        self.label_15.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.comboBox_choiceD = QComboBox(self.frame_17)
        self.comboBox_choiceD.addItem(u"\u041d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u043e\u0435 ")
        self.comboBox_choiceD.addItem(u"\u042d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0435")
        self.comboBox_choiceD.setObjectName(u"comboBox_choiceD")
        self.comboBox_choiceD.setStyleSheet(u"QComboBox{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: rgb(0, 0, 0);	\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(210, 210, 210);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_13.addWidget(self.comboBox_choiceD)


        self.verticalLayout_15.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.lineEdit_5 = QLineEdit(self.frame_18)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(210, 10, 51, 31))
        self.lineEdit_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_16 = QLabel(self.frame_18)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(12, 12, 159, 17))
        self.label_16.setFont(font4)
        self.label_16.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_15.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(20, 10, 411, 161))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_19)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_20)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 0, 160, 31))
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit_15 = QLineEdit(self.frame_20)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(180, 0, 51, 31))
        self.lineEdit_15.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_16.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.frame_21.setPalette(palette1)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_21)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_18 = QLabel(self.frame_21)
        self.label_18.setObjectName(u"label_18")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(8)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(75)
        self.label_18.setFont(font5)
        self.label_18.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_17.addWidget(self.label_18)

        self.comboBox_choiceModel = QComboBox(self.frame_21)
        self.comboBox_choiceModel.addItem("")
        self.comboBox_choiceModel.addItem("")
        self.comboBox_choiceModel.setObjectName(u"comboBox_choiceModel")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush7)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush12 = QBrush(QColor(243, 243, 243, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush12)
        self.comboBox_choiceModel.setPalette(palette2)
        self.comboBox_choiceModel.setContextMenuPolicy(Qt.NoContextMenu)
        self.comboBox_choiceModel.setStyleSheet(u"QComboBox{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: rgb(0, 0, 0);	\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(210, 210, 210);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"background: transparent;\n"
"color: rgb(0, 0, 0);\n"
"selection-color: rgb(243, 243, 243);")
        self.comboBox_choiceModel.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.verticalLayout_17.addWidget(self.comboBox_choiceModel)


        self.verticalLayout_16.addWidget(self.frame_21)

        self.pushButton_3 = QPushButton(self.frame_15)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(230, 190, 171, 51))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        brush13 = QBrush(QColor(240, 255, 248, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush7)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        self.pushButton_3.setPalette(palette3)
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(240, 255, 248);\n"
"color: rgb(0, 0, 0);")
        self.frame_9 = QFrame(self.frame_15)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(440, 50, 441, 80))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.lineEdit_path_2 = QLineEdit(self.frame_9)
        self.lineEdit_path_2.setObjectName(u"lineEdit_path_2")
        self.lineEdit_path_2.setGeometry(QRect(10, 0, 301, 31))
        self.lineEdit_path_2.setStyleSheet(u"\n"
"background: transparent;")
        self.filebutton_2 = QPushButton(self.frame_9)
        self.filebutton_2.setObjectName(u"filebutton_2")
        self.filebutton_2.setGeometry(QRect(320, 0, 121, 31))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush7)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush7)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        self.filebutton_2.setPalette(palette4)
        self.filebutton_2.setFont(font3)
        self.filebutton_2.setStyleSheet(u"background-color: rgb(240, 255, 248);\n"
"color: rgb(0, 0, 0);")
        self.checkBox_3 = QCheckBox(self.frame_15)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(450, 10, 431, 31))
        font6 = QFont()
        font6.setBold(True)
        font6.setWeight(75)
        self.checkBox_3.setFont(font6)
        self.checkBox_3.setStyleSheet(u"background-color: rgb(110, 137, 165);\n"
"color: rgb(230, 230, 230);")
        self.checkBox_8 = QCheckBox(self.frame_15)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(450, 140, 431, 31))
        self.checkBox_8.setFont(font6)
        self.checkBox_8.setStyleSheet(u"background-color: rgb(110, 137, 165);\n"
"color: rgb(230, 230, 230);")
        self.stackedWidget.addWidget(self.page_5)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame_22 = QFrame(self.page)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(0, 0, 1001, 561))
        self.frame_22.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.buttonStart = QPushButton(self.frame_22)
        self.buttonStart.setObjectName(u"buttonStart")
        self.buttonStart.setGeometry(QRect(190, 360, 221, 41))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush7)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush7)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        self.buttonStart.setPalette(palette5)
        self.buttonStart.setFont(font3)
        self.buttonStart.setStyleSheet(u"background-color: rgb(240, 255, 248);\n"
"color: rgb(0, 0, 0);")
        self.frame_10 = QFrame(self.frame_22)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 10, 471, 311))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_20 = QLabel(self.frame_11)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(120, 0, 208, 31))
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit_morle = QLineEdit(self.frame_11)
        self.lineEdit_morle.setObjectName(u"lineEdit_morle")
        self.lineEdit_morle.setGeometry(QRect(350, 0, 51, 31))
        self.lineEdit_morle.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.checkBox_2 = QCheckBox(self.frame_11)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(80, 0, 31, 31))

        self.verticalLayout_11.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_23 = QFrame(self.frame_12)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(10, 30, 120, 80))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.label_22 = QLabel(self.frame_12)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(40, 6, 311, 21))
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit_MH = QLineEdit(self.frame_12)
        self.lineEdit_MH.setObjectName(u"lineEdit_MH")
        self.lineEdit_MH.setGeometry(QRect(350, 0, 51, 31))
        self.lineEdit_MH.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.checkBox_4 = QCheckBox(self.frame_12)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(10, 0, 31, 31))

        self.verticalLayout_11.addWidget(self.frame_12)

        self.frame_24 = QFrame(self.frame_10)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.label_21 = QLabel(self.frame_24)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(140, 0, 201, 31))
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit_Dog = QLineEdit(self.frame_24)
        self.lineEdit_Dog.setObjectName(u"lineEdit_Dog")
        self.lineEdit_Dog.setGeometry(QRect(350, 0, 51, 31))
        self.lineEdit_Dog.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.checkBox_9 = QCheckBox(self.frame_24)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setGeometry(QRect(110, 0, 31, 31))

        self.verticalLayout_11.addWidget(self.frame_24)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.label_23 = QLabel(self.frame_14)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(60, 0, 271, 21))
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit_LP = QLineEdit(self.frame_14)
        self.lineEdit_LP.setObjectName(u"lineEdit_LP")
        self.lineEdit_LP.setGeometry(QRect(350, 0, 51, 31))
        self.lineEdit_LP.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.checkBox_10 = QCheckBox(self.frame_14)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setGeometry(QRect(20, 0, 31, 31))

        self.verticalLayout_11.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.label_19 = QLabel(self.frame_13)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(120, 6, 211, 21))
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit_f = QLineEdit(self.frame_13)
        self.lineEdit_f.setObjectName(u"lineEdit_f")
        self.lineEdit_f.setGeometry(QRect(350, 0, 51, 31))
        self.lineEdit_f.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.checkBox_11 = QCheckBox(self.frame_13)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setGeometry(QRect(80, 0, 31, 31))

        self.verticalLayout_11.addWidget(self.frame_13)

        self.frame_33 = QFrame(self.frame_22)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(470, 10, 511, 91))
        self.frame_33.setStyleSheet(u"")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.lineEdit_path_3 = QLineEdit(self.frame_33)
        self.lineEdit_path_3.setObjectName(u"lineEdit_path_3")
        self.lineEdit_path_3.setGeometry(QRect(20, 50, 301, 31))
        self.lineEdit_path_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.filebutton_3 = QPushButton(self.frame_33)
        self.filebutton_3.setObjectName(u"filebutton_3")
        self.filebutton_3.setGeometry(QRect(340, 50, 121, 31))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush7)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush7)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        self.filebutton_3.setPalette(palette6)
        self.filebutton_3.setFont(font3)
        self.filebutton_3.setStyleSheet(u"background-color: rgb(240, 255, 248);\n"
"color: rgb(0, 0, 0);")
        self.checkBox_5 = QCheckBox(self.frame_33)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(20, 10, 501, 31))
        self.checkBox_5.setFont(font6)
        self.checkBox_5.setStyleSheet(u"background-color: rgb(110, 137, 165);\n"
"color: rgb(230, 230, 230);")
        self.frame_25 = QFrame(self.frame_22)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(490, 200, 511, 341))
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_25)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.checkBox_witDrops = QCheckBox(self.frame_26)
        self.checkBox_witDrops.setObjectName(u"checkBox_witDrops")
        self.checkBox_witDrops.setGeometry(QRect(70, -1, 171, 31))
        self.checkBox_witDrops.setFont(font6)
        self.checkBox_witDrops.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_12.addWidget(self.frame_26)

        self.frame_28 = QFrame(self.frame_25)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.label_24 = QLabel(self.frame_28)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(80, 0, 131, 31))
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit_v = QLineEdit(self.frame_28)
        self.lineEdit_v.setObjectName(u"lineEdit_v")
        self.lineEdit_v.setGeometry(QRect(230, 0, 51, 31))
        self.lineEdit_v.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_12.addWidget(self.frame_28)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_27)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(180, 30, 193, 32))
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_10 = QLabel(self.frame_27)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 0, 171, 32))
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.comboBox_choiceD_2 = QComboBox(self.frame_27)
        self.comboBox_choiceD_2.addItem(u"\u041d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u043e\u0435 ")
        self.comboBox_choiceD_2.addItem(u"\u042d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0435")
        self.comboBox_choiceD_2.setObjectName(u"comboBox_choiceD_2")
        self.comboBox_choiceD_2.setGeometry(QRect(230, 0, 193, 32))
        self.comboBox_choiceD_2.setStyleSheet(u"QComboBox{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: rgb(0, 0, 0);	\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(210, 210, 210);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_12.addWidget(self.frame_27)

        self.frame_29 = QFrame(self.frame_25)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.label_26 = QLabel(self.frame_29)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(90, 0, 121, 31))
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit_step = QLineEdit(self.frame_29)
        self.lineEdit_step.setObjectName(u"lineEdit_step")
        self.lineEdit_step.setGeometry(QRect(230, 0, 51, 31))
        self.lineEdit_step.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_12.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_25)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.label_27 = QLabel(self.frame_30)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(20, 0, 211, 31))
        self.label_27.setFont(font3)
        self.label_27.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit_vv = QLineEdit(self.frame_30)
        self.lineEdit_vv.setObjectName(u"lineEdit_vv")
        self.lineEdit_vv.setGeometry(QRect(230, 0, 51, 31))
        self.lineEdit_vv.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_12.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_25)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.label_28 = QLabel(self.frame_31)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(60, 10, 151, 17))
        self.label_28.setFont(font3)
        self.label_28.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit_kilvo = QLineEdit(self.frame_31)
        self.lineEdit_kilvo.setObjectName(u"lineEdit_kilvo")
        self.lineEdit_kilvo.setGeometry(QRect(230, 0, 51, 31))
        self.lineEdit_kilvo.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_12.addWidget(self.frame_31)

        self.frame_34 = QFrame(self.frame_25)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.filebutton_parametrs = QPushButton(self.frame_34)
        self.filebutton_parametrs.setObjectName(u"filebutton_parametrs")
        self.filebutton_parametrs.setGeometry(QRect(330, 0, 111, 31))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush7)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush7)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        self.filebutton_parametrs.setPalette(palette7)
        self.filebutton_parametrs.setFont(font3)
        self.filebutton_parametrs.setStyleSheet(u"background-color: rgb(240, 255, 248);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_pathpar = QLineEdit(self.frame_34)
        self.lineEdit_pathpar.setObjectName(u"lineEdit_pathpar")
        self.lineEdit_pathpar.setGeometry(QRect(150, 0, 171, 31))
        self.lineEdit_pathpar.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_29 = QLabel(self.frame_34)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(0, 0, 151, 31))
        self.label_29.setFont(font3)
        self.label_29.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_12.addWidget(self.frame_34)

        self.checkBox_6 = QCheckBox(self.frame_22)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(490, 160, 501, 31))
        self.checkBox_6.setFont(font6)
        self.checkBox_6.setStyleSheet(u"background-color: rgb(110, 137, 165);\n"
"color: rgb(230, 230, 230);")
        self.stackedWidget.addWidget(self.page)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(40)
        self.label_6.setFont(font7)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(14)
        self.label.setFont(font8)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.label_7 = QLabel(self.page_home)
        self.label_7.setObjectName(u"label_7")
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(15)
        self.label_7.setFont(font9)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.page_home)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(500, 210, 441, 131))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"QComboBox{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: rgb(0, 0, 0);	\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(210, 210, 210);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_9.addWidget(self.comboBox_2)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(12, 12, 159, 17))
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit_4 = QLineEdit(self.frame_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(210, 10, 101, 31))
        self.lineEdit_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(50, 30, 335, 133))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_2 = QFrame(self.frame_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(12, 12, 160, 17))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(180, 10, 51, 31))
        self.lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.frame_2)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.label_8)

        self.comboBox = QComboBox(self.frame_7)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setContextMenuPolicy(Qt.CustomContextMenu)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: rgb(0, 0, 0);	\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(210, 210, 210);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 180, 171, 41))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush7)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush7)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        self.pushButton.setPalette(palette8)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"background-color: rgb(240, 255, 248);\n"
"color: rgb(0, 0, 0);")
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(500, 30, 441, 41))
        self.checkBox.setFont(font6)
        self.checkBox.setStyleSheet(u"background-color: rgb(110, 137, 165);\n"
"color: rgb(238, 238, 238);")
        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(500, 70, 441, 80))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.lineEdit_path = QLineEdit(self.frame_8)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        self.lineEdit_path.setGeometry(QRect(10, 10, 301, 31))
        self.filebutton = QPushButton(self.frame_8)
        self.filebutton.setObjectName(u"filebutton")
        self.filebutton.setGeometry(QRect(320, 10, 121, 31))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush7)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush7)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        self.filebutton.setPalette(palette9)
        self.filebutton.setFont(font3)
        self.filebutton.setStyleSheet(u"background-color: rgb(240, 255, 248);\n"
"color: rgb(0, 0, 0);")
        self.checkBox_7 = QCheckBox(self.frame)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(500, 160, 441, 41))
        self.checkBox_7.setFont(font6)
        self.checkBox_7.setStyleSheet(u"background-color: rgb(110, 137, 165);\n"
"color: rgb(230, 230, 230);")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 250, 491, 21))
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.comboBox_3 = QComboBox(self.frame)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(80, 280, 351, 31))
        self.comboBox_3.setContextMenuPolicy(Qt.CustomContextMenu)
        self.comboBox_3.setStyleSheet(u"QComboBox{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: rgb(0, 0, 0);	\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(210, 210, 210);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.verticalLayout_6.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setStyleSheet(u"background-color: rgb(110, 137, 165)")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	background-color: rgb(231, 255, 253) ;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.gridLayout_2.addWidget(self.frame_main, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"WTiRM V1.0", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| \u0413\u041b\u0410\u0412\u041d\u0410\u042f \u0421\u0420\u0410\u041d\u0418\u0426\u0410", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 ", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u0431\u044a\u0435\u043c \u0432\u044b\u0431\u043e\u0440\u043a\u0438", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0447\u043b\u0435\u043d\u043e\u0432 \u0440\u044f\u0434\u0430", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0424\u0443\u0440\u044c\u0435", None))
        self.comboBox_choiceModel.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u043a\u0440\u0435\u0442\u043d\u043e\u0435", None))
        self.comboBox_choiceModel.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0441\u0442\u0440\u043e\u0435", None))

        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435", None))
        self.filebutton_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432\u044b\u0431\u043e\u0440\u043a\u0443 \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"\u041c\u041e\u0414\u0415\u041b\u0418\u0420\u041e\u0412\u0410\u041d\u0418\u0415 \u0412\u042b\u0411\u041e\u0420\u041a\u0418 ", None))
        self.buttonStart.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u041c\u043e\u0440\u043b\u0435", None))
        self.lineEdit_morle.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.checkBox_2.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u041c\u0435\u043a\u0441\u0438\u043a\u0430\u043d\u0441\u043a\u0430\u044f \u0448\u043b\u044f\u043f\u0430", None))
        self.lineEdit_MH.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.checkBox_4.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u044f DOG", None))
        self.lineEdit_Dog.setText(QCoreApplication.translate("MainWindow", u"34", None))
        self.checkBox_9.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u044f Littlewood&Paley", None))
        self.lineEdit_LP.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.checkBox_10.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u0424\u0443\u0440\u044c\u0435", None))
        self.lineEdit_f.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.checkBox_11.setText("")
        self.filebutton_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432\u044b\u0431\u043e\u0440\u043a\u0443 \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.checkBox_witDrops.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u043e\u0441\u044b", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u044f \u0432\u044b\u0431\u0440\u043e\u0441\u043e\u0432", None))
        self.lineEdit_v.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0438\u0440\u0438\u0442\u0435 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0438\u0440\u0438\u0442\u0435 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 ", None))

        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0448\u0443\u043c\u0430", None))
        self.lineEdit_step.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044a\u0435\u043c \u0433\u0435\u043d\u0435\u0440\u0438\u0440\u0443\u0435\u043c\u043e\u0439 \u0432\u044b\u0431\u043e\u0440\u043a\u0438", None))
        self.lineEdit_vv.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u044b\u0431\u043e\u0440\u043e\u043a", None))
        self.lineEdit_kilvo.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.filebutton_parametrs.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.lineEdit_pathpar.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u0441 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c\u0438", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"\u041c\u041e\u0414\u0415\u041b\u0418\u0420\u041e\u0412\u0410\u041d\u0418\u0415 \u0412\u042b\u0411\u041e\u0420\u041a\u0418 ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0413\u0422\u0423", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Page Index 0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 ", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u043e\u0435 ", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u042d\u043a\u043f\u043e\u043d\u0438\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0435", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u0431\u044a\u0435\u043c \u0432\u044b\u0431\u043e\u0440\u043a\u0438", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0447\u043b\u0435\u043d\u043e\u0432 \u0440\u044f\u0434\u0430", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0435\u0439\u0432\u043b\u0435\u0442", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0440\u043b\u0435", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"DOG", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Littlewood&Paley", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043a\u0441\u0438\u043a\u0430\u043d\u0441\u043a\u0430\u044f \u0448\u043b\u044f\u043f\u0430", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0432\u044b\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u0435", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432\u044b\u0431\u043e\u0440\u043a\u0443 \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.filebutton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"\u041c\u041e\u0414\u0415\u041b\u0418\u0420\u041e\u0412\u0410\u041d\u0418\u0415 \u0412\u042b\u0411\u041e\u0420\u041a\u0418 ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0430\u0441\u0447\u0435\u0442 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u0430 \u0434\u043b\u044f \u0432\u0435\u0439\u0432\u043b\u0435\u0442\u043e\u0432 DOG \u0438 \u043c\u0435\u043a\u0441\u0438\u043a\u0430\u043d\u0441\u043a\u043e\u0439 \u0448\u043b\u044f\u043f\u044b", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0437\u043e\u043b\u043e\u0442\u043e\u0433\u043e \u0441\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0442\u0440\u0430\u043f\u0435\u0446\u0438\u0439", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0421\u0438\u043c\u043f\u0441\u043e\u043d\u0430", None))

        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Registered by: NSTU", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

