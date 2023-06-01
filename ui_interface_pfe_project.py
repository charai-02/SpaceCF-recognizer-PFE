# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_pfe_projecteRwXNX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1354, 824)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: rgb(211, 211, 211);\n"
"	background-image:url('backgrounds/wallpaperflare.com_wallpaper(22).jpg');\n"
"}\n"
"\n"
"#leftMenuSubContainer{\n"
"	background-color: rgb(130, 28, 255);\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"#centerMenuSubContainer{\n"
"	background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"#frame_4, #popupNotificationSubContainer, #frame_11, #screenshotBtn, #changeScreenshotBtn{\n"
"	background-color: rgb(0, 115, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#headerContainer, #footerContainer{\n"
"	background-color: rgb(175, 175, 175);\n"
"}\n"
"\n"
"#label_11{\n"
"	background-color: rgb(175, 175, 175);\n"
"	border-radius: 15px;\n"
"	border-width: 10"
                        "px;\n"
"	border-color:  rgb(0, 175, 175);\n"
"}\n"
"#label_12{\n"
"\n"
"}\n"
"\n"
"#recognizeBtn , #screenShotBtn , #addBtn, #clearDataBtn,  #cancelBtn{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(126, 140, 130);\n"
"	border-radius:20px;\n"
"}\n"
"\n"
"#addPersonTitle{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(45, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuBtn.setStyleSheet(u"font-size: 18px;")
        icon = QIcon()
        icon.addFile(u"icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 30, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        sizePolicy.setHeightForWidth(self.homeBtn.sizePolicy().hasHeightForWidth())
        self.homeBtn.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"URW Gothic [urw]")
        self.homeBtn.setFont(font)
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeBtn.setStyleSheet(u"font-size: 18px;\n"
"background-color: rgb(211, 211, 211);")
        icon1 = QIcon()
        icon1.addFile(u"icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.addpersonBtn = QPushButton(self.frame_2)
        self.addpersonBtn.setObjectName(u"addpersonBtn")
        self.addpersonBtn.setFont(font)
        self.addpersonBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addpersonBtn.setStyleSheet(u"font-size: 18px;")
        icon2 = QIcon()
        icon2.addFile(u"icons/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addpersonBtn.setIcon(icon2)
        self.addpersonBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.addpersonBtn)

        self.databaseBtn = QPushButton(self.frame_2)
        self.databaseBtn.setObjectName(u"databaseBtn")
        self.databaseBtn.setFont(font)
        self.databaseBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.databaseBtn.setStyleSheet(u"font-size: 18px;")
        icon3 = QIcon()
        icon3.addFile(u"icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.databaseBtn.setIcon(icon3)
        self.databaseBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.databaseBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setFont(font)
        self.infoBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.infoBtn.setStyleSheet(u"font-size: 18px;")
        icon4 = QIcon()
        icon4.addFile(u"icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon4)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font)
        self.helpBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.helpBtn.setStyleSheet(u"font-size: 18px;")
        icon5 = QIcon()
        icon5.addFile(u"icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon5)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setMinimumSize(QSize(617, 554))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.mainBodyContainer.setFont(font1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamily(u"FontAwesome")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        self.label_4.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_4)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.notificationBtn = QPushButton(self.frame_6)
        self.notificationBtn.setObjectName(u"notificationBtn")
        self.notificationBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon6)
        self.notificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificationBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        icon7 = QIcon()
        icon7.addFile(u"icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon7)
        self.minimizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon8 = QIcon()
        icon8.addFile(u"icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon8)
        self.restoreBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_4.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon9 = QIcon()
        icon9.addFile(u"icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon9)
        self.closeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_11 = QVBoxLayout(self.page_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.homeContainer = QWidget(self.page_3)
        self.homeContainer.setObjectName(u"homeContainer")
        self.verticalLayout_5 = QVBoxLayout(self.homeContainer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.homeTitleContainer = QWidget(self.homeContainer)
        self.homeTitleContainer.setObjectName(u"homeTitleContainer")
        self.homeTitleContainer.setMinimumSize(QSize(0, 150))
        self.horizontalLayout_3 = QHBoxLayout(self.homeTitleContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.homeTitle = QLabel(self.homeTitleContainer)
        self.homeTitle.setObjectName(u"homeTitle")
        font3 = QFont()
        font3.setFamily(u"Fira Code SemiBold")
        font3.setPointSize(28)
        font3.setBold(True)
        font3.setWeight(75)
        self.homeTitle.setFont(font3)
        self.homeTitle.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.homeTitle, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.homeTitleContainer, 0, Qt.AlignTop)

        self.homeMainContainer = QWidget(self.homeContainer)
        self.homeMainContainer.setObjectName(u"homeMainContainer")
        sizePolicy2.setHeightForWidth(self.homeMainContainer.sizePolicy().hasHeightForWidth())
        self.homeMainContainer.setSizePolicy(sizePolicy2)
        self.horizontalLayout_13 = QHBoxLayout(self.homeMainContainer)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.videoContainer = QWidget(self.homeMainContainer)
        self.videoContainer.setObjectName(u"videoContainer")
        sizePolicy.setHeightForWidth(self.videoContainer.sizePolicy().hasHeightForWidth())
        self.videoContainer.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.videoContainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frameVideo = QFrame(self.videoContainer)
        self.frameVideo.setObjectName(u"frameVideo")
        sizePolicy2.setHeightForWidth(self.frameVideo.sizePolicy().hasHeightForWidth())
        self.frameVideo.setSizePolicy(sizePolicy2)
        self.frameVideo.setMinimumSize(QSize(520, 370))
        self.frameVideo.setMaximumSize(QSize(520, 370))
        font4 = QFont()
        font4.setFamily(u"Noto Sans Adlam Unjoined")
        font4.setPointSize(10)
        self.frameVideo.setFont(font4)
        self.frameVideo.setStyleSheet(u"background-color: rgb(126, 140, 130);")
        self.frameVideo.setFrameShape(QFrame.StyledPanel)
        self.frameVideo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frameVideo)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.videoLive = QLabel(self.frameVideo)
        self.videoLive.setObjectName(u"videoLive")
        self.videoLive.setMinimumSize(QSize(500, 350))
        self.videoLive.setMaximumSize(QSize(500, 350))
        self.videoLive.setPixmap(QPixmap(u"backgrounds/face_reco.jpg"))
        self.videoLive.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.videoLive, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frameVideo)

        self.activeDesactiveBtn = QFrame(self.videoContainer)
        self.activeDesactiveBtn.setObjectName(u"activeDesactiveBtn")
        self.activeDesactiveBtn.setMinimumSize(QSize(0, 55))
        self.activeDesactiveBtn.setMaximumSize(QSize(16777215, 55))
        self.activeDesactiveBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.activeDesactiveBtn.setStyleSheet(u"background-color: rgb(128, 55, 255);")
        self.activeDesactiveBtn.setFrameShape(QFrame.StyledPanel)
        self.activeDesactiveBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.activeDesactiveBtn)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.cameraActiveBtn = QPushButton(self.activeDesactiveBtn)
        self.cameraActiveBtn.setObjectName(u"cameraActiveBtn")
        icon10 = QIcon()
        icon10.addFile(u"icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cameraActiveBtn.setIcon(icon10)
        self.cameraActiveBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.cameraActiveBtn)

        self.label = QLabel(self.activeDesactiveBtn)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(15, 16777215))
        font5 = QFont()
        font5.setPointSize(20)
        self.label.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label, 0, Qt.AlignTop)

        self.cameraDesactiveBtn = QPushButton(self.activeDesactiveBtn)
        self.cameraDesactiveBtn.setObjectName(u"cameraDesactiveBtn")
        icon11 = QIcon()
        icon11.addFile(u"icons/camera-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cameraDesactiveBtn.setIcon(icon11)
        self.cameraDesactiveBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_18.addWidget(self.cameraDesactiveBtn)


        self.verticalLayout_6.addWidget(self.activeDesactiveBtn)


        self.horizontalLayout_13.addWidget(self.videoContainer, 0, Qt.AlignTop)

        self.labDataBtnContainer = QWidget(self.homeMainContainer)
        self.labDataBtnContainer.setObjectName(u"labDataBtnContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labDataBtnContainer.sizePolicy().hasHeightForWidth())
        self.labDataBtnContainer.setSizePolicy(sizePolicy3)
        self.verticalLayout_31 = QVBoxLayout(self.labDataBtnContainer)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(-1, -1, -1, 37)
        self.back = QWidget(self.labDataBtnContainer)
        self.back.setObjectName(u"back")
        sizePolicy3.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy3)
        self.back.setMinimumSize(QSize(0, 0))
        self.back.setMaximumSize(QSize(16777215, 16777215))
        self.back.setStyleSheet(u"background-color: rgb(126, 140, 130);\n"
"\n"
"\n"
"")
        self.horizontalLayout_27 = QHBoxLayout(self.back)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, -1, -1, 6)
        self.labDataContainer = QWidget(self.back)
        self.labDataContainer.setObjectName(u"labDataContainer")
        self.labDataContainer.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);\n"
"margin: 4px;")
        self.horizontalLayout_12 = QHBoxLayout(self.labDataContainer)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.labSubContainer = QWidget(self.labDataContainer)
        self.labSubContainer.setObjectName(u"labSubContainer")
        self.verticalLayout_25 = QVBoxLayout(self.labSubContainer)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.fnameLab = QLabel(self.labSubContainer)
        self.fnameLab.setObjectName(u"fnameLab")
        self.fnameLab.setMaximumSize(QSize(16777215, 50))
        font6 = QFont()
        font6.setFamily(u"Fira Code Retina")
        font6.setPointSize(18)
        font6.setBold(True)
        font6.setWeight(75)
        self.fnameLab.setFont(font6)

        self.verticalLayout_25.addWidget(self.fnameLab)

        self.lnameLab = QLabel(self.labSubContainer)
        self.lnameLab.setObjectName(u"lnameLab")
        self.lnameLab.setMaximumSize(QSize(16777215, 50))
        self.lnameLab.setFont(font6)

        self.verticalLayout_25.addWidget(self.lnameLab)

        self.ageLab = QLabel(self.labSubContainer)
        self.ageLab.setObjectName(u"ageLab")
        self.ageLab.setMaximumSize(QSize(16777215, 50))
        self.ageLab.setFont(font6)

        self.verticalLayout_25.addWidget(self.ageLab)

        self.phonenumLab = QLabel(self.labSubContainer)
        self.phonenumLab.setObjectName(u"phonenumLab")
        self.phonenumLab.setMaximumSize(QSize(16777215, 50))
        self.phonenumLab.setFont(font6)

        self.verticalLayout_25.addWidget(self.phonenumLab)

        self.emailLab = QLabel(self.labSubContainer)
        self.emailLab.setObjectName(u"emailLab")
        self.emailLab.setMaximumSize(QSize(16777215, 50))
        self.emailLab.setFont(font6)

        self.verticalLayout_25.addWidget(self.emailLab)


        self.horizontalLayout_12.addWidget(self.labSubContainer)

        self.dataSubContainer = QWidget(self.labDataContainer)
        self.dataSubContainer.setObjectName(u"dataSubContainer")
        sizePolicy1.setHeightForWidth(self.dataSubContainer.sizePolicy().hasHeightForWidth())
        self.dataSubContainer.setSizePolicy(sizePolicy1)
        font7 = QFont()
        font7.setFamily(u"Fira Code SemiBold")
        self.dataSubContainer.setFont(font7)
        self.verticalLayout_30 = QVBoxLayout(self.dataSubContainer)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.fnameData = QLabel(self.dataSubContainer)
        self.fnameData.setObjectName(u"fnameData")
        self.fnameData.setMaximumSize(QSize(16777215, 50))
        self.fnameData.setFont(font6)

        self.verticalLayout_30.addWidget(self.fnameData)

        self.lnameData = QLabel(self.dataSubContainer)
        self.lnameData.setObjectName(u"lnameData")
        self.lnameData.setMaximumSize(QSize(16777215, 50))
        self.lnameData.setFont(font6)

        self.verticalLayout_30.addWidget(self.lnameData)

        self.ageData = QLabel(self.dataSubContainer)
        self.ageData.setObjectName(u"ageData")
        self.ageData.setMaximumSize(QSize(16777215, 50))
        self.ageData.setFont(font6)

        self.verticalLayout_30.addWidget(self.ageData)

        self.phonenumData = QLabel(self.dataSubContainer)
        self.phonenumData.setObjectName(u"phonenumData")
        self.phonenumData.setMaximumSize(QSize(16777215, 50))
        self.phonenumData.setFont(font6)

        self.verticalLayout_30.addWidget(self.phonenumData)

        self.emailData = QLabel(self.dataSubContainer)
        self.emailData.setObjectName(u"emailData")
        self.emailData.setMaximumSize(QSize(16777215, 50))
        self.emailData.setFont(font6)

        self.verticalLayout_30.addWidget(self.emailData)


        self.horizontalLayout_12.addWidget(self.dataSubContainer)


        self.horizontalLayout_27.addWidget(self.labDataContainer)


        self.verticalLayout_31.addWidget(self.back)

        self.widget_3 = QWidget(self.labDataBtnContainer)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_28.setSpacing(8)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.recognizeBtn = QPushButton(self.widget_3)
        self.recognizeBtn.setObjectName(u"recognizeBtn")
        self.recognizeBtn.setMinimumSize(QSize(0, 50))
        font8 = QFont()
        font8.setFamily(u"URW Gothic [urw]")
        font8.setPointSize(18)
        font8.setBold(True)
        font8.setWeight(75)
        self.recognizeBtn.setFont(font8)
        self.recognizeBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_28.addWidget(self.recognizeBtn)

        self.clearDataBtn = QPushButton(self.widget_3)
        self.clearDataBtn.setObjectName(u"clearDataBtn")
        self.clearDataBtn.setMinimumSize(QSize(0, 50))
        self.clearDataBtn.setFont(font8)
        self.clearDataBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_28.addWidget(self.clearDataBtn)


        self.verticalLayout_31.addWidget(self.widget_3, 0, Qt.AlignBottom)


        self.horizontalLayout_13.addWidget(self.labDataBtnContainer)


        self.verticalLayout_5.addWidget(self.homeMainContainer)


        self.verticalLayout_11.addWidget(self.homeContainer)

        self.mainPages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_15 = QHBoxLayout(self.page_4)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.databaseContainer = QWidget(self.page_4)
        self.databaseContainer.setObjectName(u"databaseContainer")
        self.verticalLayout_22 = QVBoxLayout(self.databaseContainer)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.databaseTitleContainer = QWidget(self.databaseContainer)
        self.databaseTitleContainer.setObjectName(u"databaseTitleContainer")
        self.databaseTitleContainer.setMinimumSize(QSize(0, 150))
        self.horizontalLayout_17 = QHBoxLayout(self.databaseTitleContainer)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.databaseTitle = QLabel(self.databaseTitleContainer)
        self.databaseTitle.setObjectName(u"databaseTitle")
        self.databaseTitle.setFont(font3)
        self.databaseTitle.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.databaseTitle, 0, Qt.AlignHCenter)


        self.verticalLayout_22.addWidget(self.databaseTitleContainer)

        self.DatabaseSubContainer = QWidget(self.databaseContainer)
        self.DatabaseSubContainer.setObjectName(u"DatabaseSubContainer")
        self.DatabaseSubContainer.setStyleSheet(u"background-color: rgb(126, 140, 130);")
        self.horizontalLayout_16 = QHBoxLayout(self.DatabaseSubContainer)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, 10, 10, 10)
        self.database = QTableWidget(self.DatabaseSubContainer)
        if (self.database.columnCount() < 6):
            self.database.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.database.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.database.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.database.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.database.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.database.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.database.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.database.setObjectName(u"database")
        sizePolicy3.setHeightForWidth(self.database.sizePolicy().hasHeightForWidth())
        self.database.setSizePolicy(sizePolicy3)
        font9 = QFont()
        font9.setFamily(u"Fira Code Retina")
        font9.setBold(False)
        font9.setWeight(50)
        self.database.setFont(font9)
        self.database.setStyleSheet(u"background-color: rgb(217, 237, 255);\n"
"font-size: 18px;\n"
"")
        self.database.setLineWidth(2)
        self.database.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.database.setTextElideMode(Qt.ElideLeft)

        self.horizontalLayout_16.addWidget(self.database)


        self.verticalLayout_22.addWidget(self.DatabaseSubContainer)


        self.horizontalLayout_15.addWidget(self.databaseContainer)

        self.mainPages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        font10 = QFont()
        font10.setPointSize(10)
        self.page_5.setFont(font10)
        self.horizontalLayout_11 = QHBoxLayout(self.page_5)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.addPersonContainer = QWidget(self.page_5)
        self.addPersonContainer.setObjectName(u"addPersonContainer")
        self.verticalLayout_28 = QVBoxLayout(self.addPersonContainer)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.homeTitleContainer_3 = QWidget(self.addPersonContainer)
        self.homeTitleContainer_3.setObjectName(u"homeTitleContainer_3")
        self.homeTitleContainer_3.setMinimumSize(QSize(0, 150))
        self.horizontalLayout_25 = QHBoxLayout(self.homeTitleContainer_3)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.homeTitle_3 = QLabel(self.homeTitleContainer_3)
        self.homeTitle_3.setObjectName(u"homeTitle_3")
        self.homeTitle_3.setFont(font3)
        self.homeTitle_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_25.addWidget(self.homeTitle_3, 0, Qt.AlignHCenter)


        self.verticalLayout_28.addWidget(self.homeTitleContainer_3)

        self.addMainContainer = QWidget(self.addPersonContainer)
        self.addMainContainer.setObjectName(u"addMainContainer")
        sizePolicy2.setHeightForWidth(self.addMainContainer.sizePolicy().hasHeightForWidth())
        self.addMainContainer.setSizePolicy(sizePolicy2)
        self.horizontalLayout_22 = QHBoxLayout(self.addMainContainer)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, -1, -1, 28)
        self.videoContainer_3 = QWidget(self.addMainContainer)
        self.videoContainer_3.setObjectName(u"videoContainer_3")
        sizePolicy.setHeightForWidth(self.videoContainer_3.sizePolicy().hasHeightForWidth())
        self.videoContainer_3.setSizePolicy(sizePolicy)
        self.videoContainer_3.setMaximumSize(QSize(700, 16777215))
        self.verticalLayout_20 = QVBoxLayout(self.videoContainer_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 6, -1, 0)
        self.frameVideo_3 = QFrame(self.videoContainer_3)
        self.frameVideo_3.setObjectName(u"frameVideo_3")
        sizePolicy2.setHeightForWidth(self.frameVideo_3.sizePolicy().hasHeightForWidth())
        self.frameVideo_3.setSizePolicy(sizePolicy2)
        self.frameVideo_3.setMinimumSize(QSize(520, 370))
        self.frameVideo_3.setMaximumSize(QSize(520, 370))
        self.frameVideo_3.setFont(font4)
        self.frameVideo_3.setStyleSheet(u"background-color: rgb(126, 140, 130);")
        self.frameVideo_3.setFrameShape(QFrame.StyledPanel)
        self.frameVideo_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frameVideo_3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.videoLive_3 = QLabel(self.frameVideo_3)
        self.videoLive_3.setObjectName(u"videoLive_3")
        self.videoLive_3.setMinimumSize(QSize(500, 350))
        self.videoLive_3.setMaximumSize(QSize(500, 350))
        self.videoLive_3.setPixmap(QPixmap(u"backgrounds/face_reco.jpg"))
        self.videoLive_3.setScaledContents(True)

        self.verticalLayout_24.addWidget(self.videoLive_3, 0, Qt.AlignHCenter)


        self.verticalLayout_20.addWidget(self.frameVideo_3)

        self.frame_11 = QFrame(self.videoContainer_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 55))
        self.frame_11.setMaximumSize(QSize(16777215, 55))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.cameraActiveBtn_3 = QPushButton(self.frame_11)
        self.cameraActiveBtn_3.setObjectName(u"cameraActiveBtn_3")
        self.cameraActiveBtn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.cameraActiveBtn_3.setIcon(icon10)
        self.cameraActiveBtn_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_23.addWidget(self.cameraActiveBtn_3, 0, Qt.AlignVCenter)

        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(15, 16777215))
        self.label_3.setFont(font5)

        self.horizontalLayout_23.addWidget(self.label_3, 0, Qt.AlignVCenter)

        self.cameraDesactiveBtn_3 = QPushButton(self.frame_11)
        self.cameraDesactiveBtn_3.setObjectName(u"cameraDesactiveBtn_3")
        self.cameraDesactiveBtn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.cameraDesactiveBtn_3.setIcon(icon11)
        self.cameraDesactiveBtn_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_23.addWidget(self.cameraDesactiveBtn_3, 0, Qt.AlignVCenter)


        self.verticalLayout_20.addWidget(self.frame_11)

        self.widget = QWidget(self.videoContainer_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_14 = QHBoxLayout(self.widget)
        self.horizontalLayout_14.setSpacing(11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.screenshotBtn = QPushButton(self.widget)
        self.screenshotBtn.setObjectName(u"screenshotBtn")
        self.screenshotBtn.setMinimumSize(QSize(0, 55))
        font11 = QFont()
        font11.setFamily(u"URW Gothic [urw]")
        font11.setPointSize(19)
        font11.setBold(True)
        font11.setWeight(75)
        self.screenshotBtn.setFont(font11)
        self.screenshotBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.screenshotBtn)

        self.changeScreenshotBtn = QPushButton(self.widget)
        self.changeScreenshotBtn.setObjectName(u"changeScreenshotBtn")
        self.changeScreenshotBtn.setMinimumSize(QSize(0, 55))
        self.changeScreenshotBtn.setFont(font11)
        self.changeScreenshotBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.changeScreenshotBtn)


        self.verticalLayout_20.addWidget(self.widget)


        self.horizontalLayout_22.addWidget(self.videoContainer_3, 0, Qt.AlignTop)

        self.widget_2 = QWidget(self.addMainContainer)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_29 = QVBoxLayout(self.widget_2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, -1, -1, 24)
        self.labDataInsert = QWidget(self.widget_2)
        self.labDataInsert.setObjectName(u"labDataInsert")
        sizePolicy3.setHeightForWidth(self.labDataInsert.sizePolicy().hasHeightForWidth())
        self.labDataInsert.setSizePolicy(sizePolicy3)
        self.labDataInsert.setMinimumSize(QSize(0, 0))
        self.labDataInsert.setMaximumSize(QSize(16777215, 16777215))
        self.labDataInsert.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 50, 50);\n"
"\n"
"")
        self.horizontalLayout_24 = QHBoxLayout(self.labDataInsert)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.labSubInsertContainer = QWidget(self.labDataInsert)
        self.labSubInsertContainer.setObjectName(u"labSubInsertContainer")
        self.verticalLayout_26 = QVBoxLayout(self.labSubInsertContainer)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(6, 7, 0, 0)
        self.fnameInsertLab = QLabel(self.labSubInsertContainer)
        self.fnameInsertLab.setObjectName(u"fnameInsertLab")
        self.fnameInsertLab.setMaximumSize(QSize(16777215, 50))
        self.fnameInsertLab.setFont(font6)

        self.verticalLayout_26.addWidget(self.fnameInsertLab)

        self.lnameInsertLab = QLabel(self.labSubInsertContainer)
        self.lnameInsertLab.setObjectName(u"lnameInsertLab")
        self.lnameInsertLab.setMaximumSize(QSize(16777215, 50))
        self.lnameInsertLab.setFont(font6)

        self.verticalLayout_26.addWidget(self.lnameInsertLab)

        self.ageInsertLab = QLabel(self.labSubInsertContainer)
        self.ageInsertLab.setObjectName(u"ageInsertLab")
        self.ageInsertLab.setMaximumSize(QSize(16777215, 50))
        self.ageInsertLab.setFont(font6)

        self.verticalLayout_26.addWidget(self.ageInsertLab)

        self.phonenumInsertLab = QLabel(self.labSubInsertContainer)
        self.phonenumInsertLab.setObjectName(u"phonenumInsertLab")
        self.phonenumInsertLab.setMaximumSize(QSize(16777215, 50))
        self.phonenumInsertLab.setFont(font6)

        self.verticalLayout_26.addWidget(self.phonenumInsertLab)

        self.emailInsertLab = QLabel(self.labSubInsertContainer)
        self.emailInsertLab.setObjectName(u"emailInsertLab")
        self.emailInsertLab.setMinimumSize(QSize(0, 0))
        self.emailInsertLab.setMaximumSize(QSize(16777215, 50))
        self.emailInsertLab.setFont(font6)

        self.verticalLayout_26.addWidget(self.emailInsertLab)


        self.horizontalLayout_24.addWidget(self.labSubInsertContainer)

        self.dataSubInsertContainer = QWidget(self.labDataInsert)
        self.dataSubInsertContainer.setObjectName(u"dataSubInsertContainer")
        sizePolicy1.setHeightForWidth(self.dataSubInsertContainer.sizePolicy().hasHeightForWidth())
        self.dataSubInsertContainer.setSizePolicy(sizePolicy1)
        self.dataSubInsertContainer.setStyleSheet(u"")
        self.verticalLayout_27 = QVBoxLayout(self.dataSubInsertContainer)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.fnameInsertData = QLineEdit(self.dataSubInsertContainer)
        self.fnameInsertData.setObjectName(u"fnameInsertData")
        self.fnameInsertData.setMinimumSize(QSize(0, 50))
        self.fnameInsertData.setFont(font6)
        self.fnameInsertData.setCursor(QCursor(Qt.IBeamCursor))
        self.fnameInsertData.setStyleSheet(u"	background-color: rgb(134, 134, 134);\n"
"	border-radius:10px;\n"
"	padding-left:10px;")

        self.verticalLayout_27.addWidget(self.fnameInsertData)

        self.lnameInsertData = QLineEdit(self.dataSubInsertContainer)
        self.lnameInsertData.setObjectName(u"lnameInsertData")
        self.lnameInsertData.setMinimumSize(QSize(0, 50))
        self.lnameInsertData.setFont(font6)
        self.lnameInsertData.setStyleSheet(u"	background-color: rgb(134, 134, 134);\n"
"	border-radius:10px;\n"
"	padding-left:10px;")

        self.verticalLayout_27.addWidget(self.lnameInsertData)

        self.ageInsertData = QLineEdit(self.dataSubInsertContainer)
        self.ageInsertData.setObjectName(u"ageInsertData")
        self.ageInsertData.setMinimumSize(QSize(0, 50))
        self.ageInsertData.setFont(font6)
        self.ageInsertData.setStyleSheet(u"	background-color: rgb(134, 134, 134);\n"
"	border-radius:10px;\n"
"	padding-left:10px;")

        self.verticalLayout_27.addWidget(self.ageInsertData)

        self.phonenumInsertData = QLineEdit(self.dataSubInsertContainer)
        self.phonenumInsertData.setObjectName(u"phonenumInsertData")
        self.phonenumInsertData.setMinimumSize(QSize(0, 50))
        self.phonenumInsertData.setFont(font6)
        self.phonenumInsertData.setStyleSheet(u"	background-color: rgb(134, 134, 134);\n"
"	border-radius:10px;\n"
"	padding-left:10px;")

        self.verticalLayout_27.addWidget(self.phonenumInsertData)

        self.emailInsertData = QLineEdit(self.dataSubInsertContainer)
        self.emailInsertData.setObjectName(u"emailInsertData")
        self.emailInsertData.setMinimumSize(QSize(0, 50))
        self.emailInsertData.setFont(font6)
        self.emailInsertData.setStyleSheet(u"	background-color: rgb(134, 134, 134);\n"
"	border-radius:10px;\n"
"	padding-left:10px;")

        self.verticalLayout_27.addWidget(self.emailInsertData)


        self.horizontalLayout_24.addWidget(self.dataSubInsertContainer)


        self.verticalLayout_29.addWidget(self.labDataInsert)

        self.addcancelWidgetBtn = QWidget(self.widget_2)
        self.addcancelWidgetBtn.setObjectName(u"addcancelWidgetBtn")
        self.addcancelWidgetBtn.setMinimumSize(QSize(0, 80))
        self.horizontalLayout_26 = QHBoxLayout(self.addcancelWidgetBtn)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.cancelBtn = QPushButton(self.addcancelWidgetBtn)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(0, 50))
        font12 = QFont()
        font12.setFamily(u"URW Gothic [urw]")
        font12.setPointSize(20)
        font12.setBold(True)
        font12.setWeight(75)
        self.cancelBtn.setFont(font12)
        self.cancelBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_26.addWidget(self.cancelBtn)

        self.addBtn = QPushButton(self.addcancelWidgetBtn)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setMinimumSize(QSize(0, 50))
        self.addBtn.setFont(font12)
        self.addBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_26.addWidget(self.addBtn)


        self.verticalLayout_29.addWidget(self.addcancelWidgetBtn, 0, Qt.AlignBottom)


        self.horizontalLayout_22.addWidget(self.widget_2)


        self.verticalLayout_28.addWidget(self.addMainContainer)


        self.horizontalLayout_11.addWidget(self.addPersonContainer)

        self.mainPages.addWidget(self.page_5)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_19 = QHBoxLayout(self.page)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.widget_4 = QWidget(self.page)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_7 = QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 83, -1, 103)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 51, -1, 42)
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(150, 156))
        self.label_2.setStyleSheet(u"	background-color: transparent;\n"
"	background: transparent;")
        self.label_2.setPixmap(QPixmap(u"backgrounds/information-logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.widget_5, 0, Qt.AlignTop)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy3.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy3)
        self.widget_6.setMinimumSize(QSize(770, 0))
        self.widget_6.setMaximumSize(QSize(770, 200))
        self.widget_6.setStyleSheet(u"background-color: rgb(131, 131, 131);")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_21.setSpacing(6)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(12, 10, 10, 10)
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(745, 175))
        self.widget_7.setStyleSheet(u"background-color: rgb(4, 88, 197);")
        self.verticalLayout_12 = QVBoxLayout(self.widget_7)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.widget_7)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(770, 175))
        self.plainTextEdit.setMaximumSize(QSize(800, 175))
        font13 = QFont()
        font13.setFamily(u"Fira Code Retina")
        font13.setPointSize(20)
        font13.setBold(True)
        font13.setWeight(75)
        self.plainTextEdit.setFont(font13)
        self.plainTextEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setOverwriteMode(False)

        self.verticalLayout_12.addWidget(self.plainTextEdit, 0, Qt.AlignHCenter)


        self.horizontalLayout_21.addWidget(self.widget_7)


        self.verticalLayout_7.addWidget(self.widget_6, 0, Qt.AlignHCenter)


        self.horizontalLayout_19.addWidget(self.widget_4, 0, Qt.AlignTop)

        self.mainPages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_31 = QHBoxLayout(self.page_2)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.widget_8 = QWidget(self.page_2)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_13 = QVBoxLayout(self.widget_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 6, -1, 54)
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 55, -1, 48)
        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(150, 156))
        self.label_5.setStyleSheet(u"	background-color: transparent;\n"
"	background: transparent;")
        self.label_5.setPixmap(QPixmap(u"backgrounds/helo_logo.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_5, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.widget_9, 0, Qt.AlignTop)

        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy3.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy3)
        self.widget_10.setMinimumSize(QSize(950, 400))
        self.widget_10.setMaximumSize(QSize(900, 400))
        self.widget_10.setStyleSheet(u"background-color: rgb(131, 131, 131);")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_30.setSpacing(6)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(10, 10, 10, 10)
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"background-color: rgb(4, 88, 197);")
        self.verticalLayout_16 = QVBoxLayout(self.widget_11)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_2 = QPlainTextEdit(self.widget_11)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        font14 = QFont()
        font14.setFamily(u"Fira Code Retina")
        font14.setPointSize(15)
        self.plainTextEdit_2.setFont(font14)
        self.plainTextEdit_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.plainTextEdit_2)


        self.horizontalLayout_30.addWidget(self.widget_11)


        self.verticalLayout_13.addWidget(self.widget_10, 0, Qt.AlignHCenter)


        self.horizontalLayout_31.addWidget(self.widget_8)

        self.mainPages.addWidget(self.page_2)

        self.verticalLayout_10.addWidget(self.mainPages)


        self.verticalLayout_9.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_14 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_15 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_9 = QLabel(self.popupNotificationSubContainer)
        self.label_9.setObjectName(u"label_9")
        font15 = QFont()
        font15.setFamily(u"Fira Code SemiBold")
        font15.setPointSize(13)
        font15.setBold(True)
        font15.setWeight(75)
        self.label_9.setFont(font15)

        self.verticalLayout_15.addWidget(self.label_9)

        self.frame_8 = QFrame(self.popupNotificationSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        font16 = QFont()
        font16.setFamily(u"Fira Code Light")
        font16.setPointSize(15)
        self.label_8.setFont(font16)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.closeNotificationBtn = QPushButton(self.frame_8)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        self.closeNotificationBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u"icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon12)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_15.addWidget(self.frame_8)


        self.verticalLayout_14.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_9.addWidget(self.popupNotificationContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_9 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.footerContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)


        self.horizontalLayout_9.addWidget(self.frame_9)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.sizeGrip)


        self.verticalLayout_9.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Accueil", None))
#if QT_CONFIG(tooltip)
        self.addpersonBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Add Person", None))
#endif // QT_CONFIG(tooltip)
        self.addpersonBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter Personne", None))
#if QT_CONFIG(tooltip)
        self.databaseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Database", None))
#endif // QT_CONFIG(tooltip)
        self.databaseBtn.setText(QCoreApplication.translate("MainWindow", u"Base de Donn\u00e9es", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information about the app", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Get more help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"aide", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SpaceCF recognizer PFE", None))
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.homeTitle.setText(QCoreApplication.translate("MainWindow", u"Detecter et Reconna\u00eetre des visages", None))
        self.videoLive.setText("")
#if QT_CONFIG(tooltip)
        self.cameraActiveBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Activat Camera", None))
#endif // QT_CONFIG(tooltip)
        self.cameraActiveBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"|", None))
#if QT_CONFIG(tooltip)
        self.cameraDesactiveBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Desactivat Camera", None))
#endif // QT_CONFIG(tooltip)
        self.cameraDesactiveBtn.setText("")
        self.fnameLab.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.lnameLab.setText(QCoreApplication.translate("MainWindow", u"Prenom :", None))
        self.ageLab.setText(QCoreApplication.translate("MainWindow", u"Age :", None))
        self.phonenumLab.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 telephone :", None))
        self.emailLab.setText(QCoreApplication.translate("MainWindow", u"Email :", None))
        self.fnameData.setText("")
        self.lnameData.setText("")
        self.ageData.setText("")
        self.phonenumData.setText("")
        self.emailData.setText("")
        self.recognizeBtn.setText(QCoreApplication.translate("MainWindow", u"Reconna\u00eetre le Visage", None))
        self.clearDataBtn.setText(QCoreApplication.translate("MainWindow", u"Effacer  les Donnees", None))
        self.databaseTitle.setText(QCoreApplication.translate("MainWindow", u"Afficher la base de donn\u00e9es", None))
        ___qtablewidgetitem = self.database.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.database.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem2 = self.database.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Prenom", None));
        ___qtablewidgetitem3 = self.database.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem4 = self.database.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"num de  telephone", None));
        ___qtablewidgetitem5 = self.database.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.homeTitle_3.setText(QCoreApplication.translate("MainWindow", u"Ajouter des Personnes", None))
        self.videoLive_3.setText("")
#if QT_CONFIG(tooltip)
        self.cameraActiveBtn_3.setToolTip(QCoreApplication.translate("MainWindow", u"Activat Camera", None))
#endif // QT_CONFIG(tooltip)
        self.cameraActiveBtn_3.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"|", None))
#if QT_CONFIG(tooltip)
        self.cameraDesactiveBtn_3.setToolTip(QCoreApplication.translate("MainWindow", u"Desactivat Camera", None))
#endif // QT_CONFIG(tooltip)
        self.cameraDesactiveBtn_3.setText("")
        self.screenshotBtn.setText(QCoreApplication.translate("MainWindow", u"prendre une photo", None))
        self.changeScreenshotBtn.setText(QCoreApplication.translate("MainWindow", u"Changer la Photo", None))
        self.fnameInsertLab.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.lnameInsertLab.setText(QCoreApplication.translate("MainWindow", u"Prenom :", None))
        self.ageInsertLab.setText(QCoreApplication.translate("MainWindow", u"Age :", None))
        self.phonenumInsertLab.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Telephone :", None))
        self.emailInsertLab.setText(QCoreApplication.translate("MainWindow", u"Email :", None))
        self.fnameInsertData.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.lnameInsertData.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prenom", None))
        self.ageInsertData.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.phonenumInsertData.setText("")
        self.phonenumInsertData.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00b0 Telephone :", None))
        self.emailInsertData.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.cancelBtn.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.addBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.label_2.setText("")
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"	L'application SpaceCF Recognizer PFE peut reconna\u00eetre, d\u00e9tecter et distinguer les visages des personnes, ainsi que stocker leurs informations et vous permettre d'y acc\u00e9der rapidement en fonction de leurs photos.", None))
        self.label_5.setText("")
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"	Pour reconna\u00eetre des visages, allez sur la page d'accueil, activez la cam\u00e9ra en utilisant le bouton situ\u00e9 en bas du cadre vid\u00e9o, puis cliquez sur le bouton \"Reconna\u00eetre les visages\". Vous pouvez afficher les informations de donn\u00e9es \u00e0 c\u00f4t\u00e9 du cadre vid\u00e9o.\n"
"\n"
"Pour ins\u00e9rer les donn\u00e9es des personnes, rendez-vous sur la page \"Ajouter une personne\", activez la cam\u00e9ra en utilisant le bouton situ\u00e9 en bas du cadre vid\u00e9o, prenez une capture d'\u00e9cran de votre visage ou des visages des personnes que vous souhaitez ins\u00e9rer, saisissez les informations des personnes dans les cases appropri\u00e9es, puis cliquez sur le bouton \"Ajouter\".\n"
"\n"
"Vous pouvez afficher les donn\u00e9es des personnes sur la page \"Base de donn\u00e9es\".", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Notification de Message", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Copyright Charai && Fariz", None))
    # retranslateUi

