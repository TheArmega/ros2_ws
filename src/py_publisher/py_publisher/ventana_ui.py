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
        MainWindow.resize(1217, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 1101, 461))
        self.tabWidget.setMinimumSize(QtCore.QSize(1101, 461))
        self.tabWidget.setMaximumSize(QtCore.QSize(1191, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.sendPositionNeck_button = QtWidgets.QPushButton(self.tab_6)
        self.sendPositionNeck_button.setGeometry(QtCore.QRect(540, 210, 89, 25))
        self.sendPositionNeck_button.setObjectName("sendPositionNeck_button")
        self.SagittalRightShoulder_label_3 = QtWidgets.QLabel(self.tab_6)
        self.SagittalRightShoulder_label_3.setGeometry(QtCore.QRect(270, 170, 181, 17))
        self.SagittalRightShoulder_label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SagittalRightShoulder_label_3.setObjectName("SagittalRightShoulder_label_3")
        self.AxialNeckSpeed_textBox = QtWidgets.QLineEdit(self.tab_6)
        self.AxialNeckSpeed_textBox.setGeometry(QtCore.QRect(600, 140, 113, 25))
        self.AxialNeckSpeed_textBox.setObjectName("AxialNeckSpeed_textBox")
        self.label_8 = QtWidgets.QLabel(self.tab_6)
        self.label_8.setGeometry(QtCore.QRect(490, 70, 181, 17))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.FrontalNeckPosition_textBox = QtWidgets.QLineEdit(self.tab_6)
        self.FrontalNeckPosition_textBox.setGeometry(QtCore.QRect(460, 170, 113, 25))
        self.FrontalNeckPosition_textBox.setObjectName("FrontalNeckPosition_textBox")
        self.label_9 = QtWidgets.QLabel(self.tab_6)
        self.label_9.setGeometry(QtCore.QRect(630, 110, 67, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_6)
        self.label_10.setGeometry(QtCore.QRect(480, 110, 67, 17))
        self.label_10.setObjectName("label_10")
        self.AxialNeckPosition_textBox = QtWidgets.QLineEdit(self.tab_6)
        self.AxialNeckPosition_textBox.setGeometry(QtCore.QRect(460, 140, 113, 25))
        self.AxialNeckPosition_textBox.setObjectName("AxialNeckPosition_textBox")
        self.FrontalNeckSpeed_textBox = QtWidgets.QLineEdit(self.tab_6)
        self.FrontalNeckSpeed_textBox.setGeometry(QtCore.QRect(600, 170, 113, 25))
        self.FrontalNeckSpeed_textBox.setObjectName("FrontalNeckSpeed_textBox")
        self.FrontalRightShoulder_label_3 = QtWidgets.QLabel(self.tab_6)
        self.FrontalRightShoulder_label_3.setGeometry(QtCore.QRect(270, 140, 181, 17))
        self.FrontalRightShoulder_label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightShoulder_label_3.setObjectName("FrontalRightShoulder_label_3")
        self.horizontalSlider = QtWidgets.QSlider(self.tab_6)
        self.horizontalSlider.setGeometry(QtCore.QRect(350, 320, 160, 16))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.horizontalSlider.setMaximum(180)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.FrontalRightShoulder_label = QtWidgets.QLabel(self.tab)
        self.FrontalRightShoulder_label.setGeometry(QtCore.QRect(270, 140, 181, 17))
        self.FrontalRightShoulder_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightShoulder_label.setObjectName("FrontalRightShoulder_label")
        self.FrontalRightWristPosition_textBox = QtWidgets.QLineEdit(self.tab)
        self.FrontalRightWristPosition_textBox.setGeometry(QtCore.QRect(460, 290, 113, 25))
        self.FrontalRightWristPosition_textBox.setObjectName("FrontalRightWristPosition_textBox")
        self.FrontalRightElbowPosition_textBox = QtWidgets.QLineEdit(self.tab)
        self.FrontalRightElbowPosition_textBox.setGeometry(QtCore.QRect(460, 230, 113, 25))
        self.FrontalRightElbowPosition_textBox.setObjectName("FrontalRightElbowPosition_textBox")
        self.SagittalRightShoulderPosition_textBox = QtWidgets.QLineEdit(self.tab)
        self.SagittalRightShoulderPosition_textBox.setGeometry(QtCore.QRect(460, 170, 113, 25))
        self.SagittalRightShoulderPosition_textBox.setObjectName("SagittalRightShoulderPosition_textBox")
        self.AxialRightWristPosition_textBox = QtWidgets.QLineEdit(self.tab)
        self.AxialRightWristPosition_textBox.setGeometry(QtCore.QRect(460, 260, 113, 25))
        self.AxialRightWristPosition_textBox.setObjectName("AxialRightWristPosition_textBox")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(490, 70, 181, 17))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.FrontalRightWrist_label = QtWidgets.QLabel(self.tab)
        self.FrontalRightWrist_label.setGeometry(QtCore.QRect(270, 290, 181, 17))
        self.FrontalRightWrist_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightWrist_label.setObjectName("FrontalRightWrist_label")
        self.AxialRightShoulder_label = QtWidgets.QLabel(self.tab)
        self.AxialRightShoulder_label.setGeometry(QtCore.QRect(270, 200, 181, 17))
        self.AxialRightShoulder_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AxialRightShoulder_label.setObjectName("AxialRightShoulder_label")
        self.FrontalRightElbow_label = QtWidgets.QLabel(self.tab)
        self.FrontalRightElbow_label.setGeometry(QtCore.QRect(270, 230, 181, 17))
        self.FrontalRightElbow_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightElbow_label.setObjectName("FrontalRightElbow_label")
        self.AxialRightWrist_label = QtWidgets.QLabel(self.tab)
        self.AxialRightWrist_label.setGeometry(QtCore.QRect(270, 260, 181, 17))
        self.AxialRightWrist_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AxialRightWrist_label.setObjectName("AxialRightWrist_label")
        self.FrontalRightWristSpeed_textBox = QtWidgets.QLineEdit(self.tab)
        self.FrontalRightWristSpeed_textBox.setGeometry(QtCore.QRect(600, 290, 113, 25))
        self.FrontalRightWristSpeed_textBox.setObjectName("FrontalRightWristSpeed_textBox")
        self.AxialRightShoulderSpeed_textBox = QtWidgets.QLineEdit(self.tab)
        self.AxialRightShoulderSpeed_textBox.setGeometry(QtCore.QRect(600, 200, 113, 25))
        self.AxialRightShoulderSpeed_textBox.setObjectName("AxialRightShoulderSpeed_textBox")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(630, 110, 67, 17))
        self.label_4.setObjectName("label_4")
        self.FrontalRightShoulderSpeed_textBox = QtWidgets.QLineEdit(self.tab)
        self.FrontalRightShoulderSpeed_textBox.setGeometry(QtCore.QRect(600, 140, 113, 25))
        self.FrontalRightShoulderSpeed_textBox.setObjectName("FrontalRightShoulderSpeed_textBox")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(480, 110, 67, 17))
        self.label_3.setObjectName("label_3")
        self.sendPositionRightArm_button = QtWidgets.QPushButton(self.tab)
        self.sendPositionRightArm_button.setGeometry(QtCore.QRect(540, 330, 89, 25))
        self.sendPositionRightArm_button.setObjectName("sendPositionRightArm_button")
        self.AxialRightWristSpeed_textBox = QtWidgets.QLineEdit(self.tab)
        self.AxialRightWristSpeed_textBox.setGeometry(QtCore.QRect(600, 260, 113, 25))
        self.AxialRightWristSpeed_textBox.setObjectName("AxialRightWristSpeed_textBox")
        self.FrontalRightElbowSpeed_textBox = QtWidgets.QLineEdit(self.tab)
        self.FrontalRightElbowSpeed_textBox.setGeometry(QtCore.QRect(600, 230, 113, 25))
        self.FrontalRightElbowSpeed_textBox.setObjectName("FrontalRightElbowSpeed_textBox")
        self.AxialRightShoulderPosition_textBox = QtWidgets.QLineEdit(self.tab)
        self.AxialRightShoulderPosition_textBox.setGeometry(QtCore.QRect(460, 200, 113, 25))
        self.AxialRightShoulderPosition_textBox.setObjectName("AxialRightShoulderPosition_textBox")
        self.SagittalRightShoulderSpeed_textBox = QtWidgets.QLineEdit(self.tab)
        self.SagittalRightShoulderSpeed_textBox.setGeometry(QtCore.QRect(600, 170, 113, 25))
        self.SagittalRightShoulderSpeed_textBox.setObjectName("SagittalRightShoulderSpeed_textBox")
        self.SagittalRightShoulder_label = QtWidgets.QLabel(self.tab)
        self.SagittalRightShoulder_label.setGeometry(QtCore.QRect(270, 170, 181, 17))
        self.SagittalRightShoulder_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SagittalRightShoulder_label.setObjectName("SagittalRightShoulder_label")
        self.FrontalRightShoulderPosition_textBox = QtWidgets.QLineEdit(self.tab)
        self.FrontalRightShoulderPosition_textBox.setGeometry(QtCore.QRect(460, 140, 113, 25))
        self.FrontalRightShoulderPosition_textBox.setObjectName("FrontalRightShoulderPosition_textBox")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.FrontalLeftElbowPosition_textBox = QtWidgets.QLineEdit(self.tab_2)
        self.FrontalLeftElbowPosition_textBox.setGeometry(QtCore.QRect(460, 230, 113, 25))
        self.FrontalLeftElbowPosition_textBox.setObjectName("FrontalLeftElbowPosition_textBox")
        self.FrontalRightElbow_label_2 = QtWidgets.QLabel(self.tab_2)
        self.FrontalRightElbow_label_2.setGeometry(QtCore.QRect(270, 230, 181, 17))
        self.FrontalRightElbow_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightElbow_label_2.setObjectName("FrontalRightElbow_label_2")
        self.AxialLeftWristSpeed_textBox = QtWidgets.QLineEdit(self.tab_2)
        self.AxialLeftWristSpeed_textBox.setGeometry(QtCore.QRect(600, 260, 113, 25))
        self.AxialLeftWristSpeed_textBox.setObjectName("AxialLeftWristSpeed_textBox")
        self.FrontalRightWrist_label_2 = QtWidgets.QLabel(self.tab_2)
        self.FrontalRightWrist_label_2.setGeometry(QtCore.QRect(270, 290, 181, 17))
        self.FrontalRightWrist_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightWrist_label_2.setObjectName("FrontalRightWrist_label_2")
        self.SagittalLeftShoulderPosition_textBox = QtWidgets.QLineEdit(self.tab_2)
        self.SagittalLeftShoulderPosition_textBox.setGeometry(QtCore.QRect(460, 170, 113, 25))
        self.SagittalLeftShoulderPosition_textBox.setObjectName("SagittalLeftShoulderPosition_textBox")
        self.AxialRightShoulder_label_2 = QtWidgets.QLabel(self.tab_2)
        self.AxialRightShoulder_label_2.setGeometry(QtCore.QRect(270, 200, 181, 17))
        self.AxialRightShoulder_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AxialRightShoulder_label_2.setObjectName("AxialRightShoulder_label_2")
        self.SagittalLeftShoulderSpeed_textBox = QtWidgets.QLineEdit(self.tab_2)
        self.SagittalLeftShoulderSpeed_textBox.setGeometry(QtCore.QRect(600, 170, 113, 25))
        self.SagittalLeftShoulderSpeed_textBox.setObjectName("SagittalLeftShoulderSpeed_textBox")
        self.AxialLeftShoulderPosition_textBox = QtWidgets.QLineEdit(self.tab_2)
        self.AxialLeftShoulderPosition_textBox.setGeometry(QtCore.QRect(460, 200, 113, 25))
        self.AxialLeftShoulderPosition_textBox.setObjectName("AxialLeftShoulderPosition_textBox")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(480, 110, 67, 17))
        self.label_6.setObjectName("label_6")
        self.FrontalLeftElbowSpeed_textBox = QtWidgets.QLineEdit(self.tab_2)
        self.FrontalLeftElbowSpeed_textBox.setGeometry(QtCore.QRect(600, 230, 113, 25))
        self.FrontalLeftElbowSpeed_textBox.setObjectName("FrontalLeftElbowSpeed_textBox")
        self.FrontalLeftShoulderPosition_textBox = QtWidgets.QLineEdit(self.tab_2)
        self.FrontalLeftShoulderPosition_textBox.setGeometry(QtCore.QRect(460, 140, 113, 25))
        self.FrontalLeftShoulderPosition_textBox.setObjectName("FrontalLeftShoulderPosition_textBox")
        self.sendPositionLeftArm_button = QtWidgets.QPushButton(self.tab_2)
        self.sendPositionLeftArm_button.setGeometry(QtCore.QRect(540, 330, 89, 25))
        self.sendPositionLeftArm_button.setObjectName("sendPositionLeftArm_button")
        self.AxialLeftWristPosition_textBox = QtWidgets.QLineEdit(self.tab_2)
        self.AxialLeftWristPosition_textBox.setGeometry(QtCore.QRect(460, 260, 113, 25))
        self.AxialLeftWristPosition_textBox.setObjectName("AxialLeftWristPosition_textBox")
        self.FrontalRightShoulder_label_2 = QtWidgets.QLabel(self.tab_2)
        self.FrontalRightShoulder_label_2.setGeometry(QtCore.QRect(270, 140, 181, 17))
        self.FrontalRightShoulder_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightShoulder_label_2.setObjectName("FrontalRightShoulder_label_2")
        self.SagittalRightShoulder_label_2 = QtWidgets.QLabel(self.tab_2)
        self.SagittalRightShoulder_label_2.setGeometry(QtCore.QRect(270, 170, 181, 17))
        self.SagittalRightShoulder_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SagittalRightShoulder_label_2.setObjectName("SagittalRightShoulder_label_2")
        self.FrontalLeftWristSpeed_textBox = QtWidgets.QLineEdit(self.tab_2)
        self.FrontalLeftWristSpeed_textBox.setGeometry(QtCore.QRect(600, 290, 113, 25))
        self.FrontalLeftWristSpeed_textBox.setObjectName("FrontalLeftWristSpeed_textBox")
        self.AxialLeftShoulderSpeed_textBox = QtWidgets.QLineEdit(self.tab_2)
        self.AxialLeftShoulderSpeed_textBox.setGeometry(QtCore.QRect(600, 200, 113, 25))
        self.AxialLeftShoulderSpeed_textBox.setObjectName("AxialLeftShoulderSpeed_textBox")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(490, 70, 181, 17))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.FrontalLeftWristPosition_textBox = QtWidgets.QLineEdit(self.tab_2)
        self.FrontalLeftWristPosition_textBox.setGeometry(QtCore.QRect(460, 290, 113, 25))
        self.FrontalLeftWristPosition_textBox.setObjectName("FrontalLeftWristPosition_textBox")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(630, 110, 67, 17))
        self.label_7.setObjectName("label_7")
        self.AxialRightWrist_label_2 = QtWidgets.QLabel(self.tab_2)
        self.AxialRightWrist_label_2.setGeometry(QtCore.QRect(270, 260, 181, 17))
        self.AxialRightWrist_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AxialRightWrist_label_2.setObjectName("AxialRightWrist_label_2")
        self.FrontalLeftShoulderSpeed_textBox = QtWidgets.QLineEdit(self.tab_2)
        self.FrontalLeftShoulderSpeed_textBox.setGeometry(QtCore.QRect(600, 140, 113, 25))
        self.FrontalLeftShoulderSpeed_textBox.setObjectName("FrontalLeftShoulderSpeed_textBox")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.sendPositionTrunk_button = QtWidgets.QPushButton(self.tab_3)
        self.sendPositionTrunk_button.setGeometry(QtCore.QRect(540, 210, 89, 25))
        self.sendPositionTrunk_button.setObjectName("sendPositionTrunk_button")
        self.SagittalRightShoulder_label_4 = QtWidgets.QLabel(self.tab_3)
        self.SagittalRightShoulder_label_4.setGeometry(QtCore.QRect(270, 170, 181, 17))
        self.SagittalRightShoulder_label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SagittalRightShoulder_label_4.setObjectName("SagittalRightShoulder_label_4")
        self.AxialTrunkSpeed_textBox = QtWidgets.QLineEdit(self.tab_3)
        self.AxialTrunkSpeed_textBox.setGeometry(QtCore.QRect(600, 140, 113, 25))
        self.AxialTrunkSpeed_textBox.setObjectName("AxialTrunkSpeed_textBox")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(490, 70, 181, 17))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.FrontalTrunkPosition_textBox = QtWidgets.QLineEdit(self.tab_3)
        self.FrontalTrunkPosition_textBox.setGeometry(QtCore.QRect(460, 170, 113, 25))
        self.FrontalTrunkPosition_textBox.setObjectName("FrontalTrunkPosition_textBox")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(630, 110, 67, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(480, 110, 67, 17))
        self.label_13.setObjectName("label_13")
        self.AxialTrunkPosition_textBox = QtWidgets.QLineEdit(self.tab_3)
        self.AxialTrunkPosition_textBox.setGeometry(QtCore.QRect(460, 140, 113, 25))
        self.AxialTrunkPosition_textBox.setObjectName("AxialTrunkPosition_textBox")
        self.FrontalTrunkSpeed_textBox = QtWidgets.QLineEdit(self.tab_3)
        self.FrontalTrunkSpeed_textBox.setGeometry(QtCore.QRect(600, 170, 113, 25))
        self.FrontalTrunkSpeed_textBox.setObjectName("FrontalTrunkSpeed_textBox")
        self.FrontalRightShoulder_label_4 = QtWidgets.QLabel(self.tab_3)
        self.FrontalRightShoulder_label_4.setGeometry(QtCore.QRect(270, 140, 181, 17))
        self.FrontalRightShoulder_label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightShoulder_label_4.setObjectName("FrontalRightShoulder_label_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.sendPositionRightLeg_button = QtWidgets.QPushButton(self.tab_4)
        self.sendPositionRightLeg_button.setGeometry(QtCore.QRect(540, 330, 89, 25))
        self.sendPositionRightLeg_button.setObjectName("sendPositionRightLeg_button")
        self.SagittalRightShoulder_label_5 = QtWidgets.QLabel(self.tab_4)
        self.SagittalRightShoulder_label_5.setGeometry(QtCore.QRect(270, 170, 181, 17))
        self.SagittalRightShoulder_label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SagittalRightShoulder_label_5.setObjectName("SagittalRightShoulder_label_5")
        self.FrontalHipRightLegPosition_textBox = QtWidgets.QLineEdit(self.tab_4)
        self.FrontalHipRightLegPosition_textBox.setGeometry(QtCore.QRect(460, 200, 113, 25))
        self.FrontalHipRightLegPosition_textBox.setObjectName("FrontalHipRightLegPosition_textBox")
        self.FrontalAnkleRightLegSpeed_textBox = QtWidgets.QLineEdit(self.tab_4)
        self.FrontalAnkleRightLegSpeed_textBox.setGeometry(QtCore.QRect(600, 260, 113, 25))
        self.FrontalAnkleRightLegSpeed_textBox.setObjectName("FrontalAnkleRightLegSpeed_textBox")
        self.FrontalHipRightLegSpeed_textBox = QtWidgets.QLineEdit(self.tab_4)
        self.FrontalHipRightLegSpeed_textBox.setGeometry(QtCore.QRect(600, 200, 113, 25))
        self.FrontalHipRightLegSpeed_textBox.setObjectName("FrontalHipRightLegSpeed_textBox")
        self.SagittalAnkleRightLegSpeed_textBox = QtWidgets.QLineEdit(self.tab_4)
        self.SagittalAnkleRightLegSpeed_textBox.setGeometry(QtCore.QRect(600, 290, 113, 25))
        self.SagittalAnkleRightLegSpeed_textBox.setObjectName("SagittalAnkleRightLegSpeed_textBox")
        self.AxialHipRightLegSpeed_textBox = QtWidgets.QLineEdit(self.tab_4)
        self.AxialHipRightLegSpeed_textBox.setGeometry(QtCore.QRect(600, 140, 113, 25))
        self.AxialHipRightLegSpeed_textBox.setObjectName("AxialHipRightLegSpeed_textBox")
        self.FrontalKneeRightLegPosition_textBox = QtWidgets.QLineEdit(self.tab_4)
        self.FrontalKneeRightLegPosition_textBox.setGeometry(QtCore.QRect(460, 230, 113, 25))
        self.FrontalKneeRightLegPosition_textBox.setObjectName("FrontalKneeRightLegPosition_textBox")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(490, 70, 181, 17))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.SagittalHipRightLegPosition_textBox = QtWidgets.QLineEdit(self.tab_4)
        self.SagittalHipRightLegPosition_textBox.setGeometry(QtCore.QRect(460, 170, 113, 25))
        self.SagittalHipRightLegPosition_textBox.setObjectName("SagittalHipRightLegPosition_textBox")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(630, 110, 67, 17))
        self.label_15.setObjectName("label_15")
        self.FrontalRightWrist_label_5 = QtWidgets.QLabel(self.tab_4)
        self.FrontalRightWrist_label_5.setGeometry(QtCore.QRect(270, 290, 181, 17))
        self.FrontalRightWrist_label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightWrist_label_5.setObjectName("FrontalRightWrist_label_5")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(480, 110, 67, 17))
        self.label_16.setObjectName("label_16")
        self.SagittalAnkleRightLegPosition_textBox = QtWidgets.QLineEdit(self.tab_4)
        self.SagittalAnkleRightLegPosition_textBox.setGeometry(QtCore.QRect(460, 290, 113, 25))
        self.SagittalAnkleRightLegPosition_textBox.setObjectName("SagittalAnkleRightLegPosition_textBox")
        self.AxialHipRightLegPosition_textBox = QtWidgets.QLineEdit(self.tab_4)
        self.AxialHipRightLegPosition_textBox.setGeometry(QtCore.QRect(460, 140, 113, 25))
        self.AxialHipRightLegPosition_textBox.setObjectName("AxialHipRightLegPosition_textBox")
        self.FrontalRightElbow_label_5 = QtWidgets.QLabel(self.tab_4)
        self.FrontalRightElbow_label_5.setGeometry(QtCore.QRect(270, 230, 181, 17))
        self.FrontalRightElbow_label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightElbow_label_5.setObjectName("FrontalRightElbow_label_5")
        self.AxialRightShoulder_label_5 = QtWidgets.QLabel(self.tab_4)
        self.AxialRightShoulder_label_5.setGeometry(QtCore.QRect(270, 200, 181, 17))
        self.AxialRightShoulder_label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AxialRightShoulder_label_5.setObjectName("AxialRightShoulder_label_5")
        self.FrontalAnkleRightLegPosition_textBox = QtWidgets.QLineEdit(self.tab_4)
        self.FrontalAnkleRightLegPosition_textBox.setGeometry(QtCore.QRect(460, 260, 113, 25))
        self.FrontalAnkleRightLegPosition_textBox.setObjectName("FrontalAnkleRightLegPosition_textBox")
        self.FrontalKneeRightLegSpeed_textBox = QtWidgets.QLineEdit(self.tab_4)
        self.FrontalKneeRightLegSpeed_textBox.setGeometry(QtCore.QRect(600, 230, 113, 25))
        self.FrontalKneeRightLegSpeed_textBox.setObjectName("FrontalKneeRightLegSpeed_textBox")
        self.SagittalHipRightLegSpeed_textBox = QtWidgets.QLineEdit(self.tab_4)
        self.SagittalHipRightLegSpeed_textBox.setGeometry(QtCore.QRect(600, 170, 113, 25))
        self.SagittalHipRightLegSpeed_textBox.setObjectName("SagittalHipRightLegSpeed_textBox")
        self.AxialRightWrist_label_5 = QtWidgets.QLabel(self.tab_4)
        self.AxialRightWrist_label_5.setGeometry(QtCore.QRect(270, 260, 181, 17))
        self.AxialRightWrist_label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AxialRightWrist_label_5.setObjectName("AxialRightWrist_label_5")
        self.FrontalRightShoulder_label_5 = QtWidgets.QLabel(self.tab_4)
        self.FrontalRightShoulder_label_5.setGeometry(QtCore.QRect(270, 140, 181, 17))
        self.FrontalRightShoulder_label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightShoulder_label_5.setObjectName("FrontalRightShoulder_label_5")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.sendPositionLeftLeg_button = QtWidgets.QPushButton(self.tab_5)
        self.sendPositionLeftLeg_button.setGeometry(QtCore.QRect(540, 330, 89, 25))
        self.sendPositionLeftLeg_button.setObjectName("sendPositionLeftLeg_button")
        self.FrontalHipLeftLegPosition_textBox = QtWidgets.QLineEdit(self.tab_5)
        self.FrontalHipLeftLegPosition_textBox.setGeometry(QtCore.QRect(460, 200, 113, 25))
        self.FrontalHipLeftLegPosition_textBox.setObjectName("FrontalHipLeftLegPosition_textBox")
        self.FrontalAnkleLeftLegSpeed_textBox = QtWidgets.QLineEdit(self.tab_5)
        self.FrontalAnkleLeftLegSpeed_textBox.setGeometry(QtCore.QRect(600, 260, 113, 25))
        self.FrontalAnkleLeftLegSpeed_textBox.setObjectName("FrontalAnkleLeftLegSpeed_textBox")
        self.FrontalHipLeftLegSpeed_textBox = QtWidgets.QLineEdit(self.tab_5)
        self.FrontalHipLeftLegSpeed_textBox.setGeometry(QtCore.QRect(600, 200, 113, 25))
        self.FrontalHipLeftLegSpeed_textBox.setObjectName("FrontalHipLeftLegSpeed_textBox")
        self.SagittalAnkleLeftLegSpeed_textBox = QtWidgets.QLineEdit(self.tab_5)
        self.SagittalAnkleLeftLegSpeed_textBox.setGeometry(QtCore.QRect(600, 290, 113, 25))
        self.SagittalAnkleLeftLegSpeed_textBox.setObjectName("SagittalAnkleLeftLegSpeed_textBox")
        self.AxialHipLeftLegSpeed_textBox = QtWidgets.QLineEdit(self.tab_5)
        self.AxialHipLeftLegSpeed_textBox.setGeometry(QtCore.QRect(600, 140, 113, 25))
        self.AxialHipLeftLegSpeed_textBox.setObjectName("AxialHipLeftLegSpeed_textBox")
        self.FrontalKneeLeftLegPosition_textBox = QtWidgets.QLineEdit(self.tab_5)
        self.FrontalKneeLeftLegPosition_textBox.setGeometry(QtCore.QRect(460, 230, 113, 25))
        self.FrontalKneeLeftLegPosition_textBox.setObjectName("FrontalKneeLeftLegPosition_textBox")
        self.label_17 = QtWidgets.QLabel(self.tab_5)
        self.label_17.setGeometry(QtCore.QRect(490, 70, 181, 17))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.SagittalHipLeftLegPosition_textBox = QtWidgets.QLineEdit(self.tab_5)
        self.SagittalHipLeftLegPosition_textBox.setGeometry(QtCore.QRect(460, 170, 113, 25))
        self.SagittalHipLeftLegPosition_textBox.setObjectName("SagittalHipLeftLegPosition_textBox")
        self.label_18 = QtWidgets.QLabel(self.tab_5)
        self.label_18.setGeometry(QtCore.QRect(630, 110, 67, 17))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_5)
        self.label_19.setGeometry(QtCore.QRect(480, 110, 67, 17))
        self.label_19.setObjectName("label_19")
        self.SagittalAnkleLeftLegPosition_textBox = QtWidgets.QLineEdit(self.tab_5)
        self.SagittalAnkleLeftLegPosition_textBox.setGeometry(QtCore.QRect(460, 290, 113, 25))
        self.SagittalAnkleLeftLegPosition_textBox.setObjectName("SagittalAnkleLeftLegPosition_textBox")
        self.AxialHipLeftLegPosition_textBox = QtWidgets.QLineEdit(self.tab_5)
        self.AxialHipLeftLegPosition_textBox.setGeometry(QtCore.QRect(460, 140, 113, 25))
        self.AxialHipLeftLegPosition_textBox.setObjectName("AxialHipLeftLegPosition_textBox")
        self.FrontalAnkleLeftLegPosition_textBox = QtWidgets.QLineEdit(self.tab_5)
        self.FrontalAnkleLeftLegPosition_textBox.setGeometry(QtCore.QRect(460, 260, 113, 25))
        self.FrontalAnkleLeftLegPosition_textBox.setObjectName("FrontalAnkleLeftLegPosition_textBox")
        self.FrontalKneeLeftLegSpeed_textBox = QtWidgets.QLineEdit(self.tab_5)
        self.FrontalKneeLeftLegSpeed_textBox.setGeometry(QtCore.QRect(600, 230, 113, 25))
        self.FrontalKneeLeftLegSpeed_textBox.setObjectName("FrontalKneeLeftLegSpeed_textBox")
        self.SagittalHipLeftLegSpeed_textBox = QtWidgets.QLineEdit(self.tab_5)
        self.SagittalHipLeftLegSpeed_textBox.setGeometry(QtCore.QRect(600, 170, 113, 25))
        self.SagittalHipLeftLegSpeed_textBox.setObjectName("SagittalHipLeftLegSpeed_textBox")
        self.AxialRightShoulder_label_6 = QtWidgets.QLabel(self.tab_5)
        self.AxialRightShoulder_label_6.setGeometry(QtCore.QRect(270, 200, 181, 17))
        self.AxialRightShoulder_label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AxialRightShoulder_label_6.setObjectName("AxialRightShoulder_label_6")
        self.SagittalRightShoulder_label_6 = QtWidgets.QLabel(self.tab_5)
        self.SagittalRightShoulder_label_6.setGeometry(QtCore.QRect(270, 170, 181, 17))
        self.SagittalRightShoulder_label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SagittalRightShoulder_label_6.setObjectName("SagittalRightShoulder_label_6")
        self.FrontalRightShoulder_label_6 = QtWidgets.QLabel(self.tab_5)
        self.FrontalRightShoulder_label_6.setGeometry(QtCore.QRect(270, 140, 181, 17))
        self.FrontalRightShoulder_label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightShoulder_label_6.setObjectName("FrontalRightShoulder_label_6")
        self.FrontalRightWrist_label_6 = QtWidgets.QLabel(self.tab_5)
        self.FrontalRightWrist_label_6.setGeometry(QtCore.QRect(270, 290, 181, 17))
        self.FrontalRightWrist_label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightWrist_label_6.setObjectName("FrontalRightWrist_label_6")
        self.AxialRightWrist_label_6 = QtWidgets.QLabel(self.tab_5)
        self.AxialRightWrist_label_6.setGeometry(QtCore.QRect(270, 260, 181, 17))
        self.AxialRightWrist_label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AxialRightWrist_label_6.setObjectName("AxialRightWrist_label_6")
        self.FrontalRightElbow_label_6 = QtWidgets.QLabel(self.tab_5)
        self.FrontalRightElbow_label_6.setGeometry(QtCore.QRect(270, 230, 181, 17))
        self.FrontalRightElbow_label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.FrontalRightElbow_label_6.setObjectName("FrontalRightElbow_label_6")
        self.tabWidget.addTab(self.tab_5, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 10, 311, 17))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1217, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sendPositionNeck_button.setText(_translate("MainWindow", "Enviar"))
        self.SagittalRightShoulder_label_3.setText(_translate("MainWindow", "Frontal Neck"))
        self.label_8.setText(_translate("MainWindow", "Head"))
        self.label_9.setText(_translate("MainWindow", "Speed"))
        self.label_10.setText(_translate("MainWindow", "Position"))
        self.FrontalRightShoulder_label_3.setText(_translate("MainWindow", "Axial Neck"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Head"))
        self.FrontalRightShoulder_label.setText(_translate("MainWindow", "Frontal Shoulder"))
        self.label_2.setText(_translate("MainWindow", "Right Arm"))
        self.FrontalRightWrist_label.setText(_translate("MainWindow", "Frontal Wrist"))
        self.AxialRightShoulder_label.setText(_translate("MainWindow", "Axial Shoulder"))
        self.FrontalRightElbow_label.setText(_translate("MainWindow", "Frontal Elbow"))
        self.AxialRightWrist_label.setText(_translate("MainWindow", "Axial Wrist"))
        self.label_4.setText(_translate("MainWindow", "Speed"))
        self.label_3.setText(_translate("MainWindow", "Position"))
        self.sendPositionRightArm_button.setText(_translate("MainWindow", "Enviar"))
        self.SagittalRightShoulder_label.setText(_translate("MainWindow", "Sagittal Shoulder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Right Arm"))
        self.FrontalRightElbow_label_2.setText(_translate("MainWindow", "Frontal Elbow"))
        self.FrontalRightWrist_label_2.setText(_translate("MainWindow", "Frontal Wrist"))
        self.AxialRightShoulder_label_2.setText(_translate("MainWindow", "Axial Shoulder"))
        self.label_6.setText(_translate("MainWindow", "Position"))
        self.sendPositionLeftArm_button.setText(_translate("MainWindow", "Enviar"))
        self.FrontalRightShoulder_label_2.setText(_translate("MainWindow", "Frontal Shoulder"))
        self.SagittalRightShoulder_label_2.setText(_translate("MainWindow", "Sagittal Shoulder"))
        self.label_5.setText(_translate("MainWindow", "Left Arm"))
        self.label_7.setText(_translate("MainWindow", "Speed"))
        self.AxialRightWrist_label_2.setText(_translate("MainWindow", "Axial Wrist"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Left Arm"))
        self.sendPositionTrunk_button.setText(_translate("MainWindow", "Enviar"))
        self.SagittalRightShoulder_label_4.setText(_translate("MainWindow", "Frontal Trunk"))
        self.label_11.setText(_translate("MainWindow", "Trunk"))
        self.label_12.setText(_translate("MainWindow", "Speed"))
        self.label_13.setText(_translate("MainWindow", "Position"))
        self.FrontalRightShoulder_label_4.setText(_translate("MainWindow", "Axial Trunk"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Trunk"))
        self.sendPositionRightLeg_button.setText(_translate("MainWindow", "Enviar"))
        self.SagittalRightShoulder_label_5.setText(_translate("MainWindow", "Sagittal Hip"))
        self.label_14.setText(_translate("MainWindow", "Right Leg"))
        self.label_15.setText(_translate("MainWindow", "Speed"))
        self.FrontalRightWrist_label_5.setText(_translate("MainWindow", "Sagittal Ankle"))
        self.label_16.setText(_translate("MainWindow", "Position"))
        self.FrontalRightElbow_label_5.setText(_translate("MainWindow", "Frontal Knee"))
        self.AxialRightShoulder_label_5.setText(_translate("MainWindow", "Frontal Hip"))
        self.AxialRightWrist_label_5.setText(_translate("MainWindow", "Frontal Ankle"))
        self.FrontalRightShoulder_label_5.setText(_translate("MainWindow", "Axial Hip"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Right Lef"))
        self.sendPositionLeftLeg_button.setText(_translate("MainWindow", "Enviar"))
        self.label_17.setText(_translate("MainWindow", "Left Leg"))
        self.label_18.setText(_translate("MainWindow", "Speed"))
        self.label_19.setText(_translate("MainWindow", "Position"))
        self.AxialRightShoulder_label_6.setText(_translate("MainWindow", "Frontal Hip"))
        self.SagittalRightShoulder_label_6.setText(_translate("MainWindow", "Sagittal Hip"))
        self.FrontalRightShoulder_label_6.setText(_translate("MainWindow", "Axial Hip"))
        self.FrontalRightWrist_label_6.setText(_translate("MainWindow", "Sagittal Ankle"))
        self.AxialRightWrist_label_6.setText(_translate("MainWindow", "Frontal Ankle"))
        self.FrontalRightElbow_label_6.setText(_translate("MainWindow", "Frontal Knee"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Left Lef"))
        self.label.setText(_translate("MainWindow", "TEO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
