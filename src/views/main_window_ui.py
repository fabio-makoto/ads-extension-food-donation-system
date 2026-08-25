# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 700)
        MainWindow.setMinimumSize(QSize(800, 700))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(800, 700))
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayoutHomePage = QVBoxLayout(self.homePage)
        self.verticalLayoutHomePage.setSpacing(8)
        self.verticalLayoutHomePage.setObjectName(u"verticalLayoutHomePage")
        self.logoLabel = QLabel(self.homePage)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(150, 160))
        self.logoLabel.setMaximumSize(QSize(390, 160))
        self.logoLabel.setPixmap(QPixmap(u"../images/logo.png"))
        self.logoLabel.setScaledContents(True)

        self.verticalLayoutHomePage.addWidget(self.logoLabel, 0, Qt.AlignHCenter)

        self.titleLabel = QLabel(self.homePage)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(0, 40))
        self.titleLabel.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayoutHomePage.addWidget(self.titleLabel)

        self.donateButton = QPushButton(self.homePage)
        self.donateButton.setObjectName(u"donateButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.donateButton.sizePolicy().hasHeightForWidth())
        self.donateButton.setSizePolicy(sizePolicy)
        self.donateButton.setMinimumSize(QSize(250, 45))
        self.donateButton.setMaximumSize(QSize(250, 45))
        self.donateButton.setLayoutDirection(Qt.LeftToRight)
        self.donateButton.setAutoFillBackground(False)
        self.donateButton.setStyleSheet(u"")
        self.donateButton.setAutoDefault(False)
        self.donateButton.setFlat(False)

        self.verticalLayoutHomePage.addWidget(self.donateButton, 0, Qt.AlignHCenter)

        self.searchButton = QPushButton(self.homePage)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMinimumSize(QSize(250, 45))
        self.searchButton.setMaximumSize(QSize(250, 45))
        self.searchButton.setStyleSheet(u"")

        self.verticalLayoutHomePage.addWidget(self.searchButton, 0, Qt.AlignHCenter)

        self.editButton = QPushButton(self.homePage)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setMinimumSize(QSize(250, 45))
        self.editButton.setMaximumSize(QSize(250, 45))
        self.editButton.setStyleSheet(u"")

        self.verticalLayoutHomePage.addWidget(self.editButton, 0, Qt.AlignHCenter)

        self.deleteButton = QPushButton(self.homePage)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setMinimumSize(QSize(250, 45))
        self.deleteButton.setMaximumSize(QSize(250, 45))
        self.deleteButton.setStyleSheet(u"")

        self.verticalLayoutHomePage.addWidget(self.deleteButton, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.homePage)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(250, 45))
        self.pushButton.setMaximumSize(QSize(250, 45))
        self.pushButton.setStyleSheet(u"")

        self.verticalLayoutHomePage.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.aboutButton = QPushButton(self.homePage)
        self.aboutButton.setObjectName(u"aboutButton")
        self.aboutButton.setMinimumSize(QSize(250, 45))
        self.aboutButton.setMaximumSize(QSize(250, 45))
        self.aboutButton.setStyleSheet(u"")

        self.verticalLayoutHomePage.addWidget(self.aboutButton, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.homePage)
        self.donatePage = QWidget()
        self.donatePage.setObjectName(u"donatePage")
        self.gridLayoutDonatePage = QGridLayout(self.donatePage)
        self.gridLayoutDonatePage.setObjectName(u"gridLayoutDonatePage")
        self.gridLayoutDonatePage.setVerticalSpacing(12)
        self.registerDonationButton = QPushButton(self.donatePage)
        self.registerDonationButton.setObjectName(u"registerDonationButton")

        self.gridLayoutDonatePage.addWidget(self.registerDonationButton, 8, 0, 1, 2, Qt.AlignHCenter)

        self.donateTitleLabel = QLabel(self.donatePage)
        self.donateTitleLabel.setObjectName(u"donateTitleLabel")
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        self.donateTitleLabel.setFont(font1)

        self.gridLayoutDonatePage.addWidget(self.donateTitleLabel, 1, 0, 1, 2, Qt.AlignHCenter)

        self.verticalSpacerUpTitle = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayoutDonatePage.addItem(self.verticalSpacerUpTitle, 0, 0, 1, 2)

        self.spinBoxQuantity = QSpinBox(self.donatePage)
        self.spinBoxQuantity.setObjectName(u"spinBoxQuantity")
        self.spinBoxQuantity.setMinimum(1)

        self.gridLayoutDonatePage.addWidget(self.spinBoxQuantity, 6, 1, 1, 1)

        self.quantityLabel = QLabel(self.donatePage)
        self.quantityLabel.setObjectName(u"quantityLabel")

        self.gridLayoutDonatePage.addWidget(self.quantityLabel, 6, 0, 1, 1)

        self.backButton = QPushButton(self.donatePage)
        self.backButton.setObjectName(u"backButton")

        self.gridLayoutDonatePage.addWidget(self.backButton, 11, 0, 1, 2, Qt.AlignHCenter)

        self.foodLabel = QLabel(self.donatePage)
        self.foodLabel.setObjectName(u"foodLabel")

        self.gridLayoutDonatePage.addWidget(self.foodLabel, 4, 0, 1, 1)

        self.dateLabel = QLabel(self.donatePage)
        self.dateLabel.setObjectName(u"dateLabel")

        self.gridLayoutDonatePage.addWidget(self.dateLabel, 7, 0, 1, 1)

        self.dateEditDonate = QDateEdit(self.donatePage)
        self.dateEditDonate.setObjectName(u"dateEditDonate")
        self.dateEditDonate.setCalendarPopup(True)

        self.gridLayoutDonatePage.addWidget(self.dateEditDonate, 7, 1, 1, 1)

        self.lineEditName = QLineEdit(self.donatePage)
        self.lineEditName.setObjectName(u"lineEditName")

        self.gridLayoutDonatePage.addWidget(self.lineEditName, 3, 1, 1, 1)

        self.nameLabel = QLabel(self.donatePage)
        self.nameLabel.setObjectName(u"nameLabel")

        self.gridLayoutDonatePage.addWidget(self.nameLabel, 3, 0, 1, 1)

        self.comboBoxFood = QComboBox(self.donatePage)
        self.comboBoxFood.setObjectName(u"comboBoxFood")

        self.gridLayoutDonatePage.addWidget(self.comboBoxFood, 4, 1, 1, 1)

        self.verticalSpacerDownTitle = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayoutDonatePage.addItem(self.verticalSpacerDownTitle, 12, 0, 1, 2)

        self.stackedWidget.addWidget(self.donatePage)
        self.searchPage = QWidget()
        self.searchPage.setObjectName(u"searchPage")
        self.gridLayout = QGridLayout(self.searchPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.searchButtonPage = QPushButton(self.searchPage)
        self.searchButtonPage.setObjectName(u"searchButtonPage")

        self.gridLayout.addWidget(self.searchButtonPage, 5, 1, 1, 2)

        self.searchBackButton = QPushButton(self.searchPage)
        self.searchBackButton.setObjectName(u"searchBackButton")

        self.gridLayout.addWidget(self.searchBackButton, 7, 0, 1, 3, Qt.AlignHCenter)

        self.searchByIdRadioButton = QRadioButton(self.searchPage)
        self.searchByIdRadioButton.setObjectName(u"searchByIdRadioButton")

        self.gridLayout.addWidget(self.searchByIdRadioButton, 2, 0, 1, 2)

        self.searchTable = QTableWidget(self.searchPage)
        if (self.searchTable.columnCount() < 5):
            self.searchTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.searchTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.searchTable.setObjectName(u"searchTable")
        self.searchTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.searchTable.setAlternatingRowColors(True)
        self.searchTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.searchTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.searchTable, 6, 0, 1, 3)

        self.searchByNameRadioButton = QRadioButton(self.searchPage)
        self.searchByNameRadioButton.setObjectName(u"searchByNameRadioButton")
        self.searchByNameRadioButton.setChecked(True)

        self.gridLayout.addWidget(self.searchByNameRadioButton, 3, 0, 1, 2)

        self.searchLineEdit = QLineEdit(self.searchPage)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.gridLayout.addWidget(self.searchLineEdit, 5, 0, 1, 1)

        self.radioButtonLabel = QLabel(self.searchPage)
        self.radioButtonLabel.setObjectName(u"radioButtonLabel")

        self.gridLayout.addWidget(self.radioButtonLabel, 1, 0, 1, 1)

        self.searchTitleLabel = QLabel(self.searchPage)
        self.searchTitleLabel.setObjectName(u"searchTitleLabel")

        self.gridLayout.addWidget(self.searchTitleLabel, 0, 0, 1, 3, Qt.AlignHCenter)

        self.searchAllRadioButton = QRadioButton(self.searchPage)
        self.searchAllRadioButton.setObjectName(u"searchAllRadioButton")

        self.gridLayout.addWidget(self.searchAllRadioButton, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.searchPage)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.donateButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Doa\u00e7\u00e3o de Alimentos", None))
        self.logoLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Sistema de Doa\u00e7\u00e3o de Alimentos", None))
        self.donateButton.setText(QCoreApplication.translate("MainWindow", u"DOAR", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"CONSULTAR", None))
        self.editButton.setText(QCoreApplication.translate("MainWindow", u"EDITAR DOA\u00c7\u00c3O", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR DOA\u00c7\u00c3O", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"RELAT\u00d3RIO", None))
        self.aboutButton.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.registerDonationButton.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR DOA\u00c7\u00c3O", None))
        self.donateTitleLabel.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR DOA\u00c7\u00c3O", None))
        self.quantityLabel.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.foodLabel.setText(QCoreApplication.translate("MainWindow", u"Alimento:", None))
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"Data da doa\u00e7\u00e3o:", None))
        self.dateEditDonate.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.lineEditName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe o nome do doador...", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Nome do doador:", None))
        self.comboBoxFood.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione um alimento...", None))
        self.searchButtonPage.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.searchBackButton.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.searchByIdRadioButton.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem = self.searchTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        ___qtablewidgetitem1 = self.searchTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        ___qtablewidgetitem2 = self.searchTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Alimento", None))
        ___qtablewidgetitem3 = self.searchTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        ___qtablewidgetitem4 = self.searchTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.searchByNameRadioButton.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.radioButtonLabel.setText(QCoreApplication.translate("MainWindow", u"Buscar por:", None))
        self.searchTitleLabel.setText(QCoreApplication.translate("MainWindow", u"CONSULTAR DOA\u00c7\u00c3O", None))
        self.searchAllRadioButton.setText(QCoreApplication.translate("MainWindow", u"Todos os Registros", None))
    # retranslateUi

