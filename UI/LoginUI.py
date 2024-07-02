# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(669, 465)
        LoginWindow.setMinimumSize(QtCore.QSize(669, 465))
        LoginWindow.setMaximumSize(QtCore.QSize(669, 465))
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -11, 331, 481))
        self.frame.setStyleSheet("#frame{\n"
"background-color: qlineargradient(spread:pad, x1:0.508148, y1:1, x2:0.487685, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(134, 88, 183, 255));\n"
"border-radius: 20px;\n"
"}")
        self.frame.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 80, 291, 91))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 36pt \"AaDingXiangShouShu\";\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 211, 151))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(110, 290, 91, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(320, 0, 351, 471))
        self.frame_2.setMinimumSize(QtCore.QSize(351, 471))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(-1, 12, 12, 12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setToolTipDuration(0)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_5)
        self.stackedWidget_2.setStyleSheet("QLineEdit{\n"
"    bakground-color: rgb(255,255,255,0);\n"
"    border: none;\n"
"    border-bottom: 1px solid black;\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(0,0,0);\n"
"    color: rgb(255,255,255);\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top: 5px;\n"
"    padding-left:5px;\n"
"}")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_S_login = QtWidgets.QWidget()
        self.page_S_login.setObjectName("page_S_login")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_S_login)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_S_account = QtWidgets.QLineEdit(self.page_S_login)
        self.lineEdit_S_account.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_S_account.setStyleSheet("QLineEdit{\n"
"    bakground-color: rgb(255,255,255,0);\n"
"    border: none;\n"
"    border-bottom: 1px solid black;\n"
"}")
        self.lineEdit_S_account.setObjectName("lineEdit_S_account")
        self.verticalLayout_5.addWidget(self.lineEdit_S_account)
        self.lineEdit_S_password = QtWidgets.QLineEdit(self.page_S_login)
        self.lineEdit_S_password.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_S_password.setObjectName("lineEdit_S_password")
        self.verticalLayout_5.addWidget(self.lineEdit_S_password)
        self.pushButton_S_sure = QtWidgets.QPushButton(self.page_S_login)
        self.pushButton_S_sure.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_S_sure.setObjectName("pushButton_S_sure")
        self.verticalLayout_5.addWidget(self.pushButton_S_sure)
        self.stackedWidget_2.addWidget(self.page_S_login)
        self.page_A_login = QtWidgets.QWidget()
        self.page_A_login.setObjectName("page_A_login")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_A_login)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_A_account = QtWidgets.QLineEdit(self.page_A_login)
        self.lineEdit_A_account.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_A_account.setObjectName("lineEdit_A_account")
        self.verticalLayout_6.addWidget(self.lineEdit_A_account)
        self.lineEdit_A_password = QtWidgets.QLineEdit(self.page_A_login)
        self.lineEdit_A_password.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_A_password.setObjectName("lineEdit_A_password")
        self.verticalLayout_6.addWidget(self.lineEdit_A_password)
        self.pushButton_A_sure = QtWidgets.QPushButton(self.page_A_login)
        self.pushButton_A_sure.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_A_sure.setObjectName("pushButton_A_sure")
        self.verticalLayout_6.addWidget(self.pushButton_A_sure)
        self.stackedWidget_2.addWidget(self.page_A_login)
        self.verticalLayout_4.addWidget(self.stackedWidget_2)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0,0,0);\n"
"    color: rgb(255,255,255);\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top: 5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_S_login = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_S_login.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_S_login.setStyleSheet("QpushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"    background-color: rgb(211, 121, 255);\n"
"}")
        self.pushButton_S_login.setObjectName("pushButton_S_login")
        self.horizontalLayout.addWidget(self.pushButton_S_login)
        self.pushButton_A_login = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_A_login.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_A_login.setObjectName("pushButton_A_login")
        self.horizontalLayout.addWidget(self.pushButton_A_login)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_2.addWidget(self.stackedWidget, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_2.raise_()
        self.frame.raise_()
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label.setText(_translate("LoginWindow", "大学教材征订系统"))
        self.label_2.setText(_translate("LoginWindow", "现代、直观的用户界面设计，\n"
"提供便捷的教材征订服务体验。"))
        self.label_3.setText(_translate("LoginWindow", "224010217 \n"
"2024-6-29"))
        self.lineEdit_S_account.setPlaceholderText(_translate("LoginWindow", "学生账号："))
        self.lineEdit_S_password.setPlaceholderText(_translate("LoginWindow", "密码："))
        self.lineEdit_S_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_S_sure.setText(_translate("LoginWindow", "确认"))
        self.lineEdit_A_account.setPlaceholderText(_translate("LoginWindow", "管理员账号："))
        self.lineEdit_A_password.setPlaceholderText(_translate("LoginWindow", "密码："))
        self.lineEdit_A_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_A_sure.setText(_translate("LoginWindow", "管理员确认"))
        self.pushButton_S_login.setText(_translate("LoginWindow", "学生登录"))
        self.pushButton_A_login.setText(_translate("LoginWindow", "管理员登录"))
        self.label_4.setText(_translate("LoginWindow", "账号密码不能为空"))
        self.label_5.setText(_translate("LoginWindow", "账号或密码错误！"))