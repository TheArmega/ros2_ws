# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1177, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 10, 311, 17))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.sendPositionRighArm_button = QtWidgets.QPushButton(self.centralwidget)
        self.sendPositionRighArm_button.setGeometry(QtCore.QRect(290, 300, 89, 25))
        self.sendPositionRighArm_button.setObjectName("sendPositionRighArm_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 40, 181, 17))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.FrontalRightShoulderPosition_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.FrontalRightShoulderPosition_textBox.setGeometry(QtCore.QRect(210, 110, 113, 25))
        self.FrontalRightShoulderPosition_textBox.setObjectName("FrontalRightShoulderPosition_textBox")
        self.SagittalRightShoulderPosition_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.SagittalRightShoulderPosition_textBox.setGeometry(QtCore.QRect(210, 140, 113, 25))
        self.SagittalRightShoulderPosition_textBox.setObjectName("SagittalRightShoulderPosition_textBox")
        self.AxialRightShoulderPosition_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.AxialRightShoulderPosition_textBox.setGeometry(QtCore.QRect(210, 170, 113, 25))
        self.AxialRightShoulderPosition_textBox.setObjectName("AxialRightShoulderPosition_textBox")
        self.FrontalRightElbowPosition_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.FrontalRightElbowPosition_textBox.setGeometry(QtCore.QRect(210, 200, 113, 25))
        self.FrontalRightElbowPosition_textBox.setObjectName("FrontalRightElbowPosition_textBox")
        self.AxialRightWristPosition_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.AxialRightWristPosition_textBox.setGeometry(QtCore.QRect(210, 230, 113, 25))
        self.AxialRightWristPosition_textBox.setObjectName("AxialRightWristPosition_textBox")
        self.FrontalRightWristPosition_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.FrontalRightWristPosition_textBox.setGeometry(QtCore.QRect(210, 260, 113, 25))
        self.FrontalRightWristPosition_textBox.setObjectName("FrontalRightWristPosition_textBox")
        self.FrontalRightShoulder_label = QtWidgets.QLabel(self.centralwidget)
        self.FrontalRightShoulder_label.setGeometry(QtCore.QRect(20, 110, 181, 17))
        self.FrontalRightShoulder_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightShoulder_label.setObjectName("FrontalRightShoulder_label")
        self.SagittalRightShoulder_label = QtWidgets.QLabel(self.centralwidget)
        self.SagittalRightShoulder_label.setGeometry(QtCore.QRect(20, 140, 181, 17))
        self.SagittalRightShoulder_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SagittalRightShoulder_label.setObjectName("SagittalRightShoulder_label")
        self.FrontalRightElbow_label = QtWidgets.QLabel(self.centralwidget)
        self.FrontalRightElbow_label.setGeometry(QtCore.QRect(20, 200, 181, 17))
        self.FrontalRightElbow_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightElbow_label.setObjectName("FrontalRightElbow_label")
        self.AxialRightShoulder_label = QtWidgets.QLabel(self.centralwidget)
        self.AxialRightShoulder_label.setGeometry(QtCore.QRect(20, 170, 181, 17))
        self.AxialRightShoulder_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AxialRightShoulder_label.setObjectName("AxialRightShoulder_label")
        self.FrontalRightWrist_label = QtWidgets.QLabel(self.centralwidget)
        self.FrontalRightWrist_label.setGeometry(QtCore.QRect(20, 260, 181, 17))
        self.FrontalRightWrist_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightWrist_label.setObjectName("FrontalRightWrist_label")
        self.AxialRightWrist_label = QtWidgets.QLabel(self.centralwidget)
        self.AxialRightWrist_label.setGeometry(QtCore.QRect(20, 230, 181, 17))
        self.AxialRightWrist_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AxialRightWrist_label.setObjectName("AxialRightWrist_label")
        self.FrontalRightElbowSpeed_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.FrontalRightElbowSpeed_textBox.setGeometry(QtCore.QRect(350, 200, 113, 25))
        self.FrontalRightElbowSpeed_textBox.setObjectName("FrontalRightElbowSpeed_textBox")
        self.SagittalRightShoulderSpeed_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.SagittalRightShoulderSpeed_textBox.setGeometry(QtCore.QRect(350, 140, 113, 25))
        self.SagittalRightShoulderSpeed_textBox.setObjectName("SagittalRightShoulderSpeed_textBox")
        self.FrontalRightShoulderSpeed_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.FrontalRightShoulderSpeed_textBox.setGeometry(QtCore.QRect(350, 110, 113, 25))
        self.FrontalRightShoulderSpeed_textBox.setObjectName("FrontalRightShoulderSpeed_textBox")
        self.FrontalRightWristSpeed_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.FrontalRightWristSpeed_textBox.setGeometry(QtCore.QRect(350, 260, 113, 25))
        self.FrontalRightWristSpeed_textBox.setObjectName("FrontalRightWristSpeed_textBox")
        self.AxialRightShoulderSpeed_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.AxialRightShoulderSpeed_textBox.setGeometry(QtCore.QRect(350, 170, 113, 25))
        self.AxialRightShoulderSpeed_textBox.setObjectName("AxialRightShoulderSpeed_textBox")
        self.AxialRightWristSpeed_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.AxialRightWristSpeed_textBox.setGeometry(QtCore.QRect(350, 230, 113, 25))
        self.AxialRightWristSpeed_textBox.setObjectName("AxialRightWristSpeed_textBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 80, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 80, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(760, 40, 181, 17))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(750, 80, 67, 17))
        self.label_6.setObjectName("label_6")
        self.FrontalLeftShoulderSpeed_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.FrontalLeftShoulderSpeed_textBox.setGeometry(QtCore.QRect(870, 110, 113, 25))
        self.FrontalLeftShoulderSpeed_textBox.setObjectName("FrontalLeftShoulderSpeed_textBox")
        self.FrontalLeftWristSpeed_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.FrontalLeftWristSpeed_textBox.setGeometry(QtCore.QRect(870, 260, 113, 25))
        self.FrontalLeftWristSpeed_textBox.setObjectName("FrontalLeftWristSpeed_textBox")
        self.SagittalRightShoulder_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.SagittalRightShoulder_label_2.setGeometry(QtCore.QRect(540, 140, 181, 17))
        self.SagittalRightShoulder_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SagittalRightShoulder_label_2.setObjectName("SagittalRightShoulder_label_2")
        self.AxialLeftWristPosition_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.AxialLeftWristPosition_textBox.setGeometry(QtCore.QRect(730, 230, 113, 25))
        self.AxialLeftWristPosition_textBox.setObjectName("AxialLeftWristPosition_textBox")
        self.FrontalLeftWristPosition_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.FrontalLeftWristPosition_textBox.setGeometry(QtCore.QRect(730, 260, 113, 25))
        self.FrontalLeftWristPosition_textBox.setObjectName("FrontalLeftWristPosition_textBox")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(900, 80, 67, 17))
        self.label_7.setObjectName("label_7")
        self.FrontalLeftElbowSpeed_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.FrontalLeftElbowSpeed_textBox.setGeometry(QtCore.QRect(870, 200, 113, 25))
        self.FrontalLeftElbowSpeed_textBox.setObjectName("FrontalLeftElbowSpeed_textBox")
        self.FrontalRightShoulder_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.FrontalRightShoulder_label_2.setGeometry(QtCore.QRect(540, 110, 181, 17))
        self.FrontalRightShoulder_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightShoulder_label_2.setObjectName("FrontalRightShoulder_label_2")
        self.FrontalRightWrist_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.FrontalRightWrist_label_2.setGeometry(QtCore.QRect(540, 260, 181, 17))
        self.FrontalRightWrist_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightWrist_label_2.setObjectName("FrontalRightWrist_label_2")
        self.AxialLeftWristSpeed_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.AxialLeftWristSpeed_textBox.setGeometry(QtCore.QRect(870, 230, 113, 25))
        self.AxialLeftWristSpeed_textBox.setObjectName("AxialLeftWristSpeed_textBox")
        self.AxialLeftShoulderPosition_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.AxialLeftShoulderPosition_textBox.setGeometry(QtCore.QRect(730, 170, 113, 25))
        self.AxialLeftShoulderPosition_textBox.setObjectName("AxialLeftShoulderPosition_textBox")
        self.FrontalLeftElbowPosition_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.FrontalLeftElbowPosition_textBox.setGeometry(QtCore.QRect(730, 200, 113, 25))
        self.FrontalLeftElbowPosition_textBox.setObjectName("FrontalLeftElbowPosition_textBox")
        self.FrontalLeftShoulderPosition_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.FrontalLeftShoulderPosition_textBox.setGeometry(QtCore.QRect(730, 110, 113, 25))
        self.FrontalLeftShoulderPosition_textBox.setObjectName("FrontalLeftShoulderPosition_textBox")
        self.sendPositionLeftArm_button = QtWidgets.QPushButton(self.centralwidget)
        self.sendPositionLeftArm_button.setGeometry(QtCore.QRect(810, 300, 89, 25))
        self.sendPositionLeftArm_button.setObjectName("sendPositionLeftArm_button")
        self.SagittalLeftShoulderSpeed_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.SagittalLeftShoulderSpeed_textBox.setGeometry(QtCore.QRect(870, 140, 113, 25))
        self.SagittalLeftShoulderSpeed_textBox.setObjectName("SagittalLeftShoulderSpeed_textBox")
        self.AxialLeftShoulderSpeed_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.AxialLeftShoulderSpeed_textBox.setGeometry(QtCore.QRect(870, 170, 113, 25))
        self.AxialLeftShoulderSpeed_textBox.setObjectName("AxialLeftShoulderSpeed_textBox")
        self.AxialRightWrist_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.AxialRightWrist_label_2.setGeometry(QtCore.QRect(540, 230, 181, 17))
        self.AxialRightWrist_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AxialRightWrist_label_2.setObjectName("AxialRightWrist_label_2")
        self.FrontalRightElbow_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.FrontalRightElbow_label_2.setGeometry(QtCore.QRect(540, 200, 181, 17))
        self.FrontalRightElbow_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightElbow_label_2.setObjectName("FrontalRightElbow_label_2")
        self.SagittalLeftShoulderPosition_textBox = QtWidgets.QLineEdit(self.centralwidget)
        self.SagittalLeftShoulderPosition_textBox.setGeometry(QtCore.QRect(730, 140, 113, 25))
        self.SagittalLeftShoulderPosition_textBox.setObjectName("SagittalLeftShoulderPosition_textBox")
        self.AxialRightShoulder_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.AxialRightShoulder_label_2.setGeometry(QtCore.QRect(540, 170, 181, 17))
        self.AxialRightShoulder_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AxialRightShoulder_label_2.setObjectName("AxialRightShoulder_label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1177, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TEO"))
        self.sendPositionRighArm_button.setText(_translate("MainWindow", "Enviar"))
        self.label_2.setText(_translate("MainWindow", "Right Arm"))
        self.FrontalRightShoulder_label.setText(_translate("MainWindow", "FrontalRightShoulder"))
        self.SagittalRightShoulder_label.setText(_translate("MainWindow", "SagittalRightShoulder"))
        self.FrontalRightElbow_label.setText(_translate("MainWindow", "FrontalRightElbow"))
        self.AxialRightShoulder_label.setText(_translate("MainWindow", "AxialRightShoulder"))
        self.FrontalRightWrist_label.setText(_translate("MainWindow", "FrontalRightWrist"))
        self.AxialRightWrist_label.setText(_translate("MainWindow", "AxialRightWrist"))
        self.label_3.setText(_translate("MainWindow", "Position"))
        self.label_4.setText(_translate("MainWindow", "Speed"))
        self.label_5.setText(_translate("MainWindow", "Left Arm"))
        self.label_6.setText(_translate("MainWindow", "Position"))
        self.SagittalRightShoulder_label_2.setText(_translate("MainWindow", "SagittalLeftShoulder"))
        self.label_7.setText(_translate("MainWindow", "Speed"))
        self.FrontalRightShoulder_label_2.setText(_translate("MainWindow", "FrontalLeftShoulder"))
        self.FrontalRightWrist_label_2.setText(_translate("MainWindow", "FrontalLeftWrist"))
        self.sendPositionLeftArm_button.setText(_translate("MainWindow", "Enviar"))
        self.AxialRightWrist_label_2.setText(_translate("MainWindow", "AxialLeftWrist"))
        self.FrontalRightElbow_label_2.setText(_translate("MainWindow", "FrontalLeftElbow"))
        self.AxialRightShoulder_label_2.setText(_translate("MainWindow", "AxialLeftShoulder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
