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
        self.verticalLayoutCentralWidget = QVBoxLayout(self.centralwidget)
        self.verticalLayoutCentralWidget.setObjectName(u"verticalLayoutCentralWidget")
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
        self.gridLayoutSearchPage = QGridLayout(self.searchPage)
        self.gridLayoutSearchPage.setObjectName(u"gridLayoutSearchPage")
        self.searchButtonPage = QPushButton(self.searchPage)
        self.searchButtonPage.setObjectName(u"searchButtonPage")

        self.gridLayoutSearchPage.addWidget(self.searchButtonPage, 5, 1, 1, 2)

        self.searchBackButton = QPushButton(self.searchPage)
        self.searchBackButton.setObjectName(u"searchBackButton")

        self.gridLayoutSearchPage.addWidget(self.searchBackButton, 7, 0, 1, 3, Qt.AlignHCenter)

        self.searchByIdRadioButton = QRadioButton(self.searchPage)
        self.searchByIdRadioButton.setObjectName(u"searchByIdRadioButton")

        self.gridLayoutSearchPage.addWidget(self.searchByIdRadioButton, 2, 0, 1, 2)

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

        self.gridLayoutSearchPage.addWidget(self.searchTable, 6, 0, 1, 3)

        self.searchByNameRadioButton = QRadioButton(self.searchPage)
        self.searchByNameRadioButton.setObjectName(u"searchByNameRadioButton")
        self.searchByNameRadioButton.setChecked(True)

        self.gridLayoutSearchPage.addWidget(self.searchByNameRadioButton, 3, 0, 1, 2)

        self.searchLineEdit = QLineEdit(self.searchPage)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.gridLayoutSearchPage.addWidget(self.searchLineEdit, 5, 0, 1, 1)

        self.radioButtonLabel = QLabel(self.searchPage)
        self.radioButtonLabel.setObjectName(u"radioButtonLabel")

        self.gridLayoutSearchPage.addWidget(self.radioButtonLabel, 1, 0, 1, 1)

        self.searchTitleLabel = QLabel(self.searchPage)
        self.searchTitleLabel.setObjectName(u"searchTitleLabel")

        self.gridLayoutSearchPage.addWidget(self.searchTitleLabel, 0, 0, 1, 3, Qt.AlignHCenter)

        self.searchAllRadioButton = QRadioButton(self.searchPage)
        self.searchAllRadioButton.setObjectName(u"searchAllRadioButton")

        self.gridLayoutSearchPage.addWidget(self.searchAllRadioButton, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.searchPage)
        self.editPage = QWidget()
        self.editPage.setObjectName(u"editPage")
        self.gridLayoutEditPage = QGridLayout(self.editPage)
        self.gridLayoutEditPage.setObjectName(u"gridLayoutEditPage")
        self.editDateEdit = QDateEdit(self.editPage)
        self.editDateEdit.setObjectName(u"editDateEdit")
        self.editDateEdit.setEnabled(False)
        self.editDateEdit.setReadOnly(True)

        self.gridLayoutEditPage.addWidget(self.editDateEdit, 13, 2, 1, 1)

        self.editTitleLabel = QLabel(self.editPage)
        self.editTitleLabel.setObjectName(u"editTitleLabel")

        self.gridLayoutEditPage.addWidget(self.editTitleLabel, 1, 0, 1, 6, Qt.AlignHCenter)

        self.editNameLabel = QLabel(self.editPage)
        self.editNameLabel.setObjectName(u"editNameLabel")

        self.gridLayoutEditPage.addWidget(self.editNameLabel, 7, 0, 1, 2)

        self.editFoodLabel = QLabel(self.editPage)
        self.editFoodLabel.setObjectName(u"editFoodLabel")

        self.gridLayoutEditPage.addWidget(self.editFoodLabel, 9, 0, 1, 1)

        self.editFoodComboBox = QComboBox(self.editPage)
        self.editFoodComboBox.addItem("")
        self.editFoodComboBox.addItem("")
        self.editFoodComboBox.addItem("")
        self.editFoodComboBox.addItem("")
        self.editFoodComboBox.addItem("")
        self.editFoodComboBox.addItem("")
        self.editFoodComboBox.addItem("")
        self.editFoodComboBox.setObjectName(u"editFoodComboBox")
        self.editFoodComboBox.setEnabled(False)

        self.gridLayoutEditPage.addWidget(self.editFoodComboBox, 9, 2, 1, 1)

        self.editNameLineEdit = QLineEdit(self.editPage)
        self.editNameLineEdit.setObjectName(u"editNameLineEdit")
        self.editNameLineEdit.setEnabled(False)
        self.editNameLineEdit.setMaximumSize(QSize(250, 16777215))
        self.editNameLineEdit.setReadOnly(True)

        self.gridLayoutEditPage.addWidget(self.editNameLineEdit, 7, 2, 1, 1)

        self.editIdLabel = QLabel(self.editPage)
        self.editIdLabel.setObjectName(u"editIdLabel")

        self.gridLayoutEditPage.addWidget(self.editIdLabel, 2, 0, 1, 2)

        self.editQuantityLabel = QLabel(self.editPage)
        self.editQuantityLabel.setObjectName(u"editQuantityLabel")

        self.gridLayoutEditPage.addWidget(self.editQuantityLabel, 11, 0, 1, 2)

        self.editSearchButton = QPushButton(self.editPage)
        self.editSearchButton.setObjectName(u"editSearchButton")
        self.editSearchButton.setMaximumSize(QSize(150, 16777215))

        self.gridLayoutEditPage.addWidget(self.editSearchButton, 2, 3, 1, 1)

        self.editDataLabel = QLabel(self.editPage)
        self.editDataLabel.setObjectName(u"editDataLabel")

        self.gridLayoutEditPage.addWidget(self.editDataLabel, 13, 0, 1, 2)

        self.editQuantitySpinBox = QSpinBox(self.editPage)
        self.editQuantitySpinBox.setObjectName(u"editQuantitySpinBox")
        self.editQuantitySpinBox.setEnabled(False)
        self.editQuantitySpinBox.setMinimum(1)

        self.gridLayoutEditPage.addWidget(self.editQuantitySpinBox, 11, 2, 1, 1)

        self.editIdLineEdit = QLineEdit(self.editPage)
        self.editIdLineEdit.setObjectName(u"editIdLineEdit")
        self.editIdLineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayoutEditPage.addWidget(self.editIdLineEdit, 2, 2, 1, 1)

        self.verticalSpacerTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayoutEditPage.addItem(self.verticalSpacerTop, 0, 0, 1, 6)

        self.verticalSpacerBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayoutEditPage.addItem(self.verticalSpacerBottom, 17, 0, 1, 6)

        self.saveEditButton = QPushButton(self.editPage)
        self.saveEditButton.setObjectName(u"saveEditButton")
        self.saveEditButton.setEnabled(False)

        self.gridLayoutEditPage.addWidget(self.saveEditButton, 15, 0, 1, 6, Qt.AlignHCenter)

        self.editBackButton = QPushButton(self.editPage)
        self.editBackButton.setObjectName(u"editBackButton")

        self.gridLayoutEditPage.addWidget(self.editBackButton, 16, 0, 1, 6, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.editPage)
        self.deletePage = QWidget()
        self.deletePage.setObjectName(u"deletePage")
        self.gridLayout = QGridLayout(self.deletePage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.deleteIdLabel = QLabel(self.deletePage)
        self.deleteIdLabel.setObjectName(u"deleteIdLabel")

        self.gridLayout.addWidget(self.deleteIdLabel, 2, 0, 1, 1)

        self.deleteNameLabel = QLabel(self.deletePage)
        self.deleteNameLabel.setObjectName(u"deleteNameLabel")

        self.gridLayout.addWidget(self.deleteNameLabel, 3, 0, 1, 1)

        self.deleteNameLineEdit = QLineEdit(self.deletePage)
        self.deleteNameLineEdit.setObjectName(u"deleteNameLineEdit")
        self.deleteNameLineEdit.setEnabled(False)
        self.deleteNameLineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.deleteNameLineEdit, 3, 2, 1, 1)

        self.deleteDateLabel = QLabel(self.deletePage)
        self.deleteDateLabel.setObjectName(u"deleteDateLabel")

        self.gridLayout.addWidget(self.deleteDateLabel, 8, 0, 1, 1)

        self.deleteSearchButton = QPushButton(self.deletePage)
        self.deleteSearchButton.setObjectName(u"deleteSearchButton")
        self.deleteSearchButton.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.deleteSearchButton, 2, 3, 1, 1)

        self.deleteFoodLabel = QLabel(self.deletePage)
        self.deleteFoodLabel.setObjectName(u"deleteFoodLabel")

        self.gridLayout.addWidget(self.deleteFoodLabel, 5, 0, 1, 1)

        self.deleteTitleLabel = QLabel(self.deletePage)
        self.deleteTitleLabel.setObjectName(u"deleteTitleLabel")

        self.gridLayout.addWidget(self.deleteTitleLabel, 1, 0, 1, 6, Qt.AlignHCenter)

        self.deleteIdLineEdit = QLineEdit(self.deletePage)
        self.deleteIdLineEdit.setObjectName(u"deleteIdLineEdit")
        self.deleteIdLineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.deleteIdLineEdit, 2, 2, 1, 1)

        self.verticalSpacerTopDeletePage = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacerTopDeletePage, 0, 0, 1, 6)

        self.deleteQuantityLabel = QLabel(self.deletePage)
        self.deleteQuantityLabel.setObjectName(u"deleteQuantityLabel")

        self.gridLayout.addWidget(self.deleteQuantityLabel, 7, 0, 1, 1)

        self.deleteFoodLineEdit = QLineEdit(self.deletePage)
        self.deleteFoodLineEdit.setObjectName(u"deleteFoodLineEdit")
        self.deleteFoodLineEdit.setEnabled(False)
        self.deleteFoodLineEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.deleteFoodLineEdit, 5, 2, 1, 1)

        self.deleteQuantitySpinBox = QSpinBox(self.deletePage)
        self.deleteQuantitySpinBox.setObjectName(u"deleteQuantitySpinBox")
        self.deleteQuantitySpinBox.setEnabled(False)
        self.deleteQuantitySpinBox.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.deleteQuantitySpinBox, 7, 2, 1, 1)

        self.deleteDateEdit = QDateEdit(self.deletePage)
        self.deleteDateEdit.setObjectName(u"deleteDateEdit")
        self.deleteDateEdit.setEnabled(False)
        self.deleteDateEdit.setMaximumSize(QSize(250, 16777215))

        self.gridLayout.addWidget(self.deleteDateEdit, 8, 2, 1, 1)

        self.verticalSpacerBottomDeletePage = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacerBottomDeletePage, 12, 0, 1, 6)

        self.deleteBackButton = QPushButton(self.deletePage)
        self.deleteBackButton.setObjectName(u"deleteBackButton")

        self.gridLayout.addWidget(self.deleteBackButton, 11, 0, 1, 6, Qt.AlignHCenter)

        self.confirmDeleteButton = QPushButton(self.deletePage)
        self.confirmDeleteButton.setObjectName(u"confirmDeleteButton")
        self.confirmDeleteButton.setEnabled(False)

        self.gridLayout.addWidget(self.confirmDeleteButton, 9, 0, 1, 6, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.deletePage)

        self.verticalLayoutCentralWidget.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)
        self.donateButton.setDefault(False)
        self.editFoodComboBox.setCurrentIndex(-1)


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
        self.editDateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.editTitleLabel.setText(QCoreApplication.translate("MainWindow", u"EDITAR DOA\u00c7\u00c3O", None))
        self.editNameLabel.setText(QCoreApplication.translate("MainWindow", u"Nome do doador:", None))
        self.editFoodLabel.setText(QCoreApplication.translate("MainWindow", u"Alimento:", None))
        self.editFoodComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Pacote de arroz 5 kg", None))
        self.editFoodComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Pacote de arroz 1 kg", None))
        self.editFoodComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pacote de feij\u00e3o 1 kg", None))
        self.editFoodComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Pacote de a\u00e7\u00facar 1 kg", None))
        self.editFoodComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Pacote de macarr\u00e3o 500 g", None))
        self.editFoodComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Caixa de leite 1 L", None))
        self.editFoodComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u00d3leo 900 ml", None))

        self.editFoodComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione um alimento...", None))
        self.editIdLabel.setText(QCoreApplication.translate("MainWindow", u"ID da doa\u00e7\u00e3o:", None))
        self.editQuantityLabel.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.editSearchButton.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.editDataLabel.setText(QCoreApplication.translate("MainWindow", u"Data da doa\u00e7\u00e3o:", None))
        self.saveEditButton.setText(QCoreApplication.translate("MainWindow", u"SALVAR ALTERA\u00c7\u00d5ES", None))
        self.editBackButton.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.deleteIdLabel.setText(QCoreApplication.translate("MainWindow", u"ID da doa\u00e7\u00e3o:", None))
        self.deleteNameLabel.setText(QCoreApplication.translate("MainWindow", u"Nome do doador:", None))
        self.deleteDateLabel.setText(QCoreApplication.translate("MainWindow", u"Data da doa\u00e7\u00e3o:", None))
        self.deleteSearchButton.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.deleteFoodLabel.setText(QCoreApplication.translate("MainWindow", u"Alimento:", None))
        self.deleteTitleLabel.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR DOA\u00c7\u00c3O", None))
        self.deleteQuantityLabel.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.deleteBackButton.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.confirmDeleteButton.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR DOA\u00c7\u00c3O", None))
    # retranslateUi

