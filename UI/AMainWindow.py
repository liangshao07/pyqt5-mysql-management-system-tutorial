# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AMainWindow(object):
    def setupUi(self, AMainWindow):
        AMainWindow.setObjectName("AMainWindow")
        AMainWindow.resize(800, 600)
        AMainWindow.setMinimumSize(QtCore.QSize(800, 600))
        AMainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(AMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("#frame_2{\n"
"    background-color: rgb(186, 143, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(0,0,0,0);\n"
"    color: rgb(255,255,255);\n"
"    border: none;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top: 5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_A_college = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_A_college.setObjectName("pushButton_A_college")
        self.verticalLayout_2.addWidget(self.pushButton_A_college)
        self.pushButton_A_major = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_A_major.setObjectName("pushButton_A_major")
        self.verticalLayout_2.addWidget(self.pushButton_A_major)
        self.pushButton_A_book = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_A_book.setObjectName("pushButton_A_book")
        self.verticalLayout_2.addWidget(self.pushButton_A_book)
        self.pushButton_A_backup_recover = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_A_backup_recover.setObjectName("pushButton_A_backup_recover")
        self.verticalLayout_2.addWidget(self.pushButton_A_backup_recover)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButton_A_update = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_A_update.setObjectName("pushButton_A_update")
        self.verticalLayout_2.addWidget(self.pushButton_A_update)
        self.pushButton_A_login_out = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_A_login_out.setObjectName("pushButton_A_login_out")
        self.verticalLayout_2.addWidget(self.pushButton_A_login_out)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(600, 500))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget_A = QtWidgets.QStackedWidget(self.frame_6)
        self.stackedWidget_A.setObjectName("stackedWidget_A")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.page_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_21 = QtWidgets.QFrame(self.frame_5)
        self.frame_21.setMinimumSize(QtCore.QSize(600, 500))
        self.frame_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_22 = QtWidgets.QFrame(self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setStyleSheet("QLineEdit{\n"
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
        self.frame_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.lineEdit_A_M_college = QtWidgets.QLineEdit(self.frame_22)
        self.lineEdit_A_M_college.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_A_M_college.setText("")
        self.lineEdit_A_M_college.setObjectName("lineEdit_A_M_college")
        self.horizontalLayout_18.addWidget(self.lineEdit_A_M_college)
        self.pushButton_A_M_college_sure = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_A_M_college_sure.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_A_M_college_sure.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_A_M_college_sure.setObjectName("pushButton_A_M_college_sure")
        self.horizontalLayout_18.addWidget(self.pushButton_A_M_college_sure)
        self.verticalLayout_10.addWidget(self.frame_22)
        self.frame_23 = QtWidgets.QFrame(self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.tableView_A_M_bookList_college = QtWidgets.QTableView(self.frame_23)
        self.tableView_A_M_bookList_college.setObjectName("tableView_A_M_bookList_college")
        self.horizontalLayout_19.addWidget(self.tableView_A_M_bookList_college)
        self.verticalLayout_10.addWidget(self.frame_23)
        self.horizontalLayout_5.addWidget(self.frame_21)
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.stackedWidget_A.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_3 = QtWidgets.QFrame(self.page_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setMinimumSize(QtCore.QSize(600, 500))
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_19 = QtWidgets.QFrame(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setStyleSheet("QLineEdit{\n"
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
        self.frame_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lineEdit_A_M_major = QtWidgets.QLineEdit(self.frame_19)
        self.lineEdit_A_M_major.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_A_M_major.setText("")
        self.lineEdit_A_M_major.setObjectName("lineEdit_A_M_major")
        self.horizontalLayout_15.addWidget(self.lineEdit_A_M_major)
        self.pushButton_A_M_major_sure = QtWidgets.QPushButton(self.frame_19)
        self.pushButton_A_M_major_sure.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_A_M_major_sure.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_A_M_major_sure.setObjectName("pushButton_A_M_major_sure")
        self.horizontalLayout_15.addWidget(self.pushButton_A_M_major_sure)
        self.verticalLayout_7.addWidget(self.frame_19)
        self.frame_20 = QtWidgets.QFrame(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.tableView_A_M_major = QtWidgets.QTableView(self.frame_20)
        self.tableView_A_M_major.setObjectName("tableView_A_M_major")
        self.horizontalLayout_16.addWidget(self.tableView_A_M_major)
        self.verticalLayout_7.addWidget(self.frame_20)
        self.horizontalLayout_17.addWidget(self.frame_10)
        self.horizontalLayout_6.addWidget(self.frame_3)
        self.stackedWidget_A.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_13 = QtWidgets.QFrame(self.page_5)
        self.frame_13.setMinimumSize(QtCore.QSize(600, 500))
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_14 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setStyleSheet("QLineEdit{\n"
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
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_A_M_out = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_A_M_out.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_A_M_out.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_A_M_out.setObjectName("pushButton_A_M_out")
        self.horizontalLayout_9.addWidget(self.pushButton_A_M_out)
        self.verticalLayout_8.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.tableView_A_M_book_out = QtWidgets.QTableView(self.frame_15)
        self.tableView_A_M_book_out.setObjectName("tableView_A_M_book_out")
        self.horizontalLayout_10.addWidget(self.tableView_A_M_book_out)
        self.verticalLayout_8.addWidget(self.frame_15)
        self.horizontalLayout_3.addWidget(self.frame_13)
        self.stackedWidget_A.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.page_6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_7 = QtWidgets.QFrame(self.page_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.frame_16 = QtWidgets.QFrame(self.frame_7)
        self.frame_16.setGeometry(QtCore.QRect(80, 70, 431, 391))
        self.frame_16.setStyleSheet("QLineEdit{\n"
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
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_A_M_backup = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_A_M_backup.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_A_M_backup.setObjectName("pushButton_A_M_backup")
        self.verticalLayout_9.addWidget(self.pushButton_A_M_backup)
        self.pushButton_A_M_recover = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_A_M_recover.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_A_M_recover.setObjectName("pushButton_A_M_recover")
        self.verticalLayout_9.addWidget(self.pushButton_A_M_recover)
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.frame_16)
        self.stackedWidget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.stackedWidget_3.addWidget(self.page_14)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.label_7 = QtWidgets.QLabel(self.page_15)
        self.label_7.setGeometry(QtCore.QRect(180, 10, 81, 39))
        self.label_7.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.stackedWidget_3.addWidget(self.page_15)
        self.page_16 = QtWidgets.QWidget()
        self.page_16.setObjectName("page_16")
        self.label_8 = QtWidgets.QLabel(self.page_16)
        self.label_8.setGeometry(QtCore.QRect(180, 10, 161, 39))
        self.label_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.stackedWidget_3.addWidget(self.page_16)
        self.page_17 = QtWidgets.QWidget()
        self.page_17.setObjectName("page_17")
        self.stackedWidget_3.addWidget(self.page_17)
        self.verticalLayout_9.addWidget(self.stackedWidget_3)
        self.horizontalLayout_13.addWidget(self.frame_7)
        self.stackedWidget_A.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.frame_9 = QtWidgets.QFrame(self.page_7)
        self.frame_9.setGeometry(QtCore.QRect(80, 80, 431, 391))
        self.frame_9.setStyleSheet("QLineEdit{\n"
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
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_A_M_password = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_A_M_password.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_A_M_password.setText("")
        self.lineEdit_A_M_password.setObjectName("lineEdit_A_M_password")
        self.verticalLayout_5.addWidget(self.lineEdit_A_M_password)
        self.lineEdit_A_M_new_password = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_A_M_new_password.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_A_M_new_password.setText("")
        self.lineEdit_A_M_new_password.setObjectName("lineEdit_A_M_new_password")
        self.verticalLayout_5.addWidget(self.lineEdit_A_M_new_password)
        self.lineEdit_A_M_new_password_sure = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_A_M_new_password_sure.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_A_M_new_password_sure.setText("")
        self.lineEdit_A_M_new_password_sure.setObjectName("lineEdit_A_M_new_password_sure")
        self.verticalLayout_5.addWidget(self.lineEdit_A_M_new_password_sure)
        self.pushButton_A_M_sure = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_A_M_sure.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_A_M_sure.setObjectName("pushButton_A_M_sure")
        self.verticalLayout_5.addWidget(self.pushButton_A_M_sure)
        self.stackedWidget_A_2 = QtWidgets.QStackedWidget(self.frame_9)
        self.stackedWidget_A_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.stackedWidget_A_2.setObjectName("stackedWidget_A_2")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.stackedWidget_A_2.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label_4 = QtWidgets.QLabel(self.page_9)
        self.label_4.setGeometry(QtCore.QRect(160, 0, 81, 39))
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.stackedWidget_A_2.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_5 = QtWidgets.QLabel(self.page_10)
        self.label_5.setGeometry(QtCore.QRect(130, 10, 161, 39))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.stackedWidget_A_2.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.label_6 = QtWidgets.QLabel(self.page_11)
        self.label_6.setGeometry(QtCore.QRect(180, 0, 81, 39))
        self.label_6.setStyleSheet("color: rgb(255, 182, 38);")
        self.label_6.setObjectName("label_6")
        self.stackedWidget_A_2.addWidget(self.page_11)
        self.verticalLayout_5.addWidget(self.stackedWidget_A_2)
        self.stackedWidget_A.addWidget(self.page_7)
        self.verticalLayout_3.addWidget(self.stackedWidget_A)
        self.horizontalLayout_8.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.frame)
        AMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AMainWindow)
        self.stackedWidget_A.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_A_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AMainWindow)

    def retranslateUi(self, AMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AMainWindow.setWindowTitle(_translate("AMainWindow", "MainWindow"))
        self.pushButton_A_college.setText(_translate("AMainWindow", "学院订购情况"))
        self.pushButton_A_major.setText(_translate("AMainWindow", "专业订购情况"))
        self.pushButton_A_book.setText(_translate("AMainWindow", "教材订购情况"))
        self.pushButton_A_backup_recover.setText(_translate("AMainWindow", "备份与恢复数据"))
        self.pushButton_A_update.setText(_translate("AMainWindow", "修改密码"))
        self.pushButton_A_login_out.setText(_translate("AMainWindow", "退出登录"))
        self.lineEdit_A_M_college.setPlaceholderText(_translate("AMainWindow", "学院：请输入学院编号"))
        self.pushButton_A_M_college_sure.setText(_translate("AMainWindow", "确认"))
        self.lineEdit_A_M_major.setPlaceholderText(_translate("AMainWindow", "专业：请输入专业编号"))
        self.pushButton_A_M_major_sure.setText(_translate("AMainWindow", "确认"))
        self.pushButton_A_M_out.setText(_translate("AMainWindow", "导出教材订购"))
        self.pushButton_A_M_backup.setText(_translate("AMainWindow", "备份"))
        self.pushButton_A_M_recover.setText(_translate("AMainWindow", "恢复"))
        self.label_7.setText(_translate("AMainWindow", "备份成功"))
        self.label_8.setText(_translate("AMainWindow", "恢复成功"))
        self.lineEdit_A_M_password.setPlaceholderText(_translate("AMainWindow", "原密码："))
        self.lineEdit_A_M_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_A_M_new_password.setPlaceholderText(_translate("AMainWindow", "新密码："))
        self.lineEdit_A_M_new_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_A_M_new_password_sure.setPlaceholderText(_translate("AMainWindow", "确认新密码："))
        self.lineEdit_A_M_new_password_sure.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_A_M_sure.setText(_translate("AMainWindow", "确认"))
        self.label_4.setText(_translate("AMainWindow", "密码不能为空"))
        self.label_5.setText(_translate("AMainWindow", "原密码错误或新密码不一致"))
        self.label_6.setText(_translate("AMainWindow", "修改成功"))
