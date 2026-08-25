import sys

from pathlib import Path

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
    )
from PySide6.QtCore import QDate, QLocale

from database.connection import create_connection, create_tables
from src.models.donation_model import (
    find_all_donations, find_donation_by_id, insert_donation, find_donations_by_name, update_donations,
    delete_donation
    )

from src.views.main_window_ui import Ui_MainWindow


app = QApplication(sys.argv)

# carrega o estilo da aplicação
style_path = Path(__file__).resolve().parent.parent / "assets" / "styles" / "base.qss"

with open(style_path, "r", encoding="utf-8") as file:
    app.setStyleSheet(file.read()) 

# cria e configura a janela principal
window = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(window)

# configura a largura das colunas da tabela de consulta
header = ui.searchTable.horizontalHeader()

header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)

# adiciona os alimentos ao comboBox
ui.comboBoxFood.addItems([
    "Pacote de arroz 5 kg",
    "Pacote de arroz 1 kg",
    "Pacote de feijão 1 kg",
    "Pacote de açúcar 1 kg",
    "Pacote de macarrão 500 g",
    "Caixa de leite 1 L",
    "Óleo 900 ml",
])

# função que irá fazer o tratamento dos campos e do registro da doação
def register_donation():
    name = ui.lineEditName.text().strip()
    food = ui.comboBoxFood.currentText()
    quantity = ui.spinBoxQuantity.value()
    date = ui.dateEditDonate.date().toString("yyyy-MM-dd")

    if not name:
        # se o line edit do nome estiver vazio um pop-up irá aparecer
        QMessageBox.warning(window, "Campo obrigatório", "Informe o nome do doador.")
        return
    
    if ui.comboBoxFood.currentIndex() == -1:
        # se não estiver selecionado nenhum alimento no comboBox
        QMessageBox.warning(window, "Campo obrigatório", "Selecione um alimento.")
        return
    
    if insert_donation(db, name, food, quantity, date):
        # concluindo o registro da doação no db
        QMessageBox.information(window, "Doação cadastrada", "Doação cadastrada com sucesso.")

        ui.lineEditName.clear()
        ui.comboBoxFood.setCurrentIndex(-1)
        ui.spinBoxQuantity.setValue(1)
        ui.dateEditDonate.setDate(QDate.currentDate())


# função que irá fazer a busca das doações e verificar qual radio button está preenchido
def search_donations():
    search_text = ui.searchLineEdit.text().strip()
    
    # limpa os resultados anteriores da tabela
    ui.searchTable.setRowCount(0)

    # busca todas as doações
    if ui.searchAllRadioButton.isChecked():
        donations = find_all_donations(db)

        if not donations:
            QMessageBox.information(window, "Nenhuma doação", "Nenhuma doação está cadastrada no sistema.")
            return

    elif ui.searchByIdRadioButton.isChecked():
        if not search_text:
            QMessageBox.warning(
                window, "Campo obrigatório", "Informe um ID para realizar a busca."
            )
            return

        # verifica se o valor informado para o ID é númerico
        if not search_text.isdigit():
            QMessageBox.warning(window, "ID inválido", "Informe um ID válido.")
            return
        
        donation = find_donation_by_id(db, int(search_text))

        if donation is None:
            QMessageBox.information(window, "Doação não encontrada", "Nenhuma doação foi encontrada com esse ID.")
            return
        
        # como a busca por ID retorna apenas uma doação,
        # transforma o resultado em uma lista
        donations = [donation]
    
    else:
        if not search_text:
            QMessageBox.warning(
                window, "Campo obrigatório", "Informe um nome para realizar a busca."
            )
            return

        donations = find_donations_by_name(db, search_text)

        if not donations:
            QMessageBox.information(window, "Doação não encontrada", "Nenhuma doação foi encontrada com esse nome.")
            return
    
    # adiciona os resultados encontrados na tabela
    for donation in donations:
        row = ui.searchTable.rowCount()
        ui.searchTable.insertRow(row)

        ui.searchTable.setItem(row, 0, QTableWidgetItem(str(donation["id"])))
        ui.searchTable.setItem(row, 1, QTableWidgetItem(donation["name"]))
        ui.searchTable.setItem(row, 2, QTableWidgetItem(donation["food"]))
        ui.searchTable.setItem(row, 3, QTableWidgetItem(str(donation["quantity"])))

        # converte a data do banco para o formato brasileiro
        date = QDate.fromString(donation["date"], "yyyy-MM-dd")

        ui.searchTable.setItem(row, 4, QTableWidgetItem(date.toString("dd/MM/yyyy")))


# definindo a página inicial antes de iniciar o sistema
ui.stackedWidget.setCurrentWidget(ui.homePage)

# Navegação entre as páginas
# Página inicial para Cadastro de doação
ui.donateButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.donatePage))

# Cadastro de doação para Página inicial
ui.backButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.homePage))

# Configura a data da doação
ui.dateEditDonate.setLocale(QLocale(QLocale.Language.Portuguese, QLocale.Country.Brazil))
ui.dateEditDonate.setDate(QDate.currentDate())

# Página inicial para Consulta de doações
ui.searchButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.searchPage))

# Consulta de doações para Página inicial
ui.searchBackButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.homePage))

# desabilita o campo de busca quando "Todos os registros" estiver selecionado
def toggle_search_field(checked: bool):
    if checked:
        ui.searchLineEdit.clear()
    
    ui.searchLineEdit.setEnabled(not checked)
    

ui.searchAllRadioButton.toggled.connect(toggle_search_field)

# cria a conexão com o banco de dados
db = create_connection()

if db is not None:
    create_tables(db)

# registra uma nova doação
ui.registerDonationButton.clicked.connect(register_donation)

# consulta uma doação
ui.searchButtonPage.clicked.connect(search_donations)

# mostra a janela do sistema
window.show()

sys.exit(app.exec())
