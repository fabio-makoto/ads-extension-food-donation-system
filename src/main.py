import sys

from pathlib import Path

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
    )
from PySide6.QtCore import QDate, QLocale

from database.connection import create_connection, create_tables
from src.models.donation_model import (
    find_all_donations, find_donation_by_id, insert_donation, find_donations_by_name, update_donation,
    delete_donation, get_donation_summary, get_total_donations, get_total_items
    )

from src.views.main_window_ui import Ui_MainWindow


app = QApplication(sys.argv)

# carrega o estilo da aplicação
style_path = Path.cwd() / "assets" / "styles" / "base.qss"

with open(style_path, "r", encoding="utf-8") as file:
    app.setStyleSheet(file.read()) 

# cria e configura a janela principal
window = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(window)

# configura a largura das colunas da tabela de consulta
search_header = ui.searchTable.horizontalHeader()

search_header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  # ocupa apenas o espaço necessário ID
search_header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)  # ocupa todo espaço disponivel NOME
search_header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)  # ocupa todo espaço disponivel ALIMENTO
search_header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)  # ocupa apenas o espaço necessário QUANTIDADE
search_header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)  # ocupa apenas o espaço necessário DATA

# configura a largura das colunas da tabela do relatório
report_header = ui.reportTable.horizontalHeader()

report_header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)  # ocupa todo espaço disponivel ALIMENTO
report_header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)  # ocupa apenas o espaço necessário QUANTIDADE

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
def register_donation() -> None:
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
def search_donations() -> None:
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

        # verifica se o valor informado para o ID é numérico
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


# função que irá carregar a doação para editá-la
def load_donation_for_edit() -> None:
    donation_id = ui.editIdLineEdit.text().strip()

    if not donation_id:
        # verifica se o line edit do id não está vazio
        QMessageBox.warning(window, "Campo obrigatório", "Informe o ID da doação.")
        return
    
    if not donation_id.isdigit():
        # verifica se o valor informado é um digito
        QMessageBox.warning(window, "ID inválido", "Informe um ID válido.")
        return
    
    donation = find_donation_by_id(db, int(donation_id))

    if donation is None:
        # caso seja informado um ID que não corresponda a nenhuma doação registrada
        QMessageBox.information(window, "Doação não encontrada", "Nenhuma doação foi encontrada com esse ID.")

        # limpa os dados da busca anterior
        ui.editNameLineEdit.clear()
        ui.editFoodComboBox.setCurrentIndex(-1)
        ui.editQuantitySpinBox.setValue(1)
        ui.editDateEdit.clear()

        # desabilita os campos de edição
        ui.editFoodComboBox.setEnabled(False)
        ui.editQuantitySpinBox.setEnabled(False)
        ui.saveEditButton.setEnabled(False)

        return
    
    # preenche os dados encontrados
    ui.editNameLineEdit.setText(donation["name"])

    # procura dentro do combo box o alimento que corresponde ao alimento salvo no banco de dados
    index = ui.editFoodComboBox.findText(donation["food"])
    if index >= 0:
        ui.editFoodComboBox.setCurrentIndex(index)
    
    ui.editQuantitySpinBox.setValue(donation["quantity"])

    date = QDate.fromString(donation["date"], "yyyy-MM-dd")
    ui.editDateEdit.setDate(date)

    # habilita os campos que podem ser editados
    ui.editFoodComboBox.setEnabled(True)
    ui.editQuantitySpinBox.setEnabled(True)
    ui.saveEditButton.setEnabled(True)

    # impede que o ID seja alterado após carregar a doação
    ui.editIdLineEdit.setEnabled(False)


# função que irá salvar a edição da doação
def save_donation_edit() -> None:
    donation_id = ui.editIdLineEdit.text().strip()
    food = ui.editFoodComboBox.currentText()
    quantity = ui.editQuantitySpinBox.value()

    if not donation_id:
        # verifica se o campo do id não está vazio
        QMessageBox.warning(window, "Campo obrigatório", "Informe o ID da doação.")
        return
    
    if update_donation(db, int(donation_id), food, quantity):
        QMessageBox.information(window, "Doação atualizada", "Doação atualizada com sucesso.")

        # limpa os campos após a atualização
        ui.editIdLineEdit.clear()
        ui.editNameLineEdit.clear()
        ui.editFoodComboBox.setCurrentIndex(-1)
        ui.editQuantitySpinBox.setValue(1)
        ui.editDateEdit.clear()

        # desabilita e habilita novamente os campos de edição
        ui.editFoodComboBox.setEnabled(False)
        ui.editQuantitySpinBox.setEnabled(False)
        ui.saveEditButton.setEnabled(False)
        ui.editIdLineEdit.setEnabled(True)


# função que irá carregar a doação para excluir
def load_donation_for_delete() -> None:
    donation_id = ui.deleteIdLineEdit.text().strip()

    if not donation_id:
        # verifica se o campo do id está vazio
        QMessageBox.warning(
            window, "Campo obrigatório", "Informe o ID da doação."
        )
        return
    
    if not donation_id.isdigit():
        # verifica se o valor informado é válido para ID
        QMessageBox.warning(
            window, "ID inválido", "Informe um ID válido."
        )
        return
    
    donation = find_donation_by_id(db, int(donation_id))

    # checa se a função encontrou alguma doação com o ID informado
    if donation is None:
        QMessageBox.information(
            window, "Doação não encontrada", "Nenhuma doação foi encontrada com esse ID."
        )

        # caso não encontre nenhuma doação, limpe os campos 
        ui.deleteNameLineEdit.clear()
        ui.deleteFoodLineEdit.clear()
        ui.deleteQuantitySpinBox.setValue(0)
        ui.deleteDateEdit.clear()

        # desabilita novamente o botão de exclusão
        ui.confirmDeleteButton.setEnabled(False)

        # impede que o ID seja alterado após carregar a doação
        ui.deleteIdLineEdit.setEnabled(False)

        return
    
    # preenche os dados encontrados
    ui.deleteNameLineEdit.setText(donation["name"])
    ui.deleteFoodLineEdit.setText(donation["food"])
    ui.deleteQuantitySpinBox.setValue(donation["quantity"])

    date = QDate.fromString(donation["date"], "yyyy-MM-dd")
    ui.deleteDateEdit.setDate(date)

    # habilita o botão de excluir doação
    ui.confirmDeleteButton.setEnabled(True)


# função para confirmar a exclusão da doação
def confirm_delete_donation() -> None:
    donation_id = ui.deleteIdLineEdit.text().strip()

    if not donation_id:
        # verifica se o campo do ID está vazio
        QMessageBox.warning(window, "Campo obrigatório", "Informe o ID da doação.")
        return

    # cria a caixa de mensagem de confirmação e pega a resposta
    answer = QMessageBox.question(window, "Confirmar exclusão", "Deseja realmente excluir esta doação?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

    if answer == QMessageBox.StandardButton.Yes:
        if delete_donation(db, int(donation_id)):
            QMessageBox.information(window, "Doação excluída", "Doação excluída com sucesso.")

            # limpa os campos preenchidos
            ui.deleteIdLineEdit.clear()
            ui.deleteNameLineEdit.clear()
            ui.deleteFoodLineEdit.clear()
            ui.deleteQuantitySpinBox.setValue(0)
            ui.deleteDateEdit.clear()

            # habilita e desabilita novamente os botoes e line edit
            ui.confirmDeleteButton.setEnabled(False)
            ui.deleteIdLineEdit.setEnabled(True)


# carrega as informações do relatório
def load_report() -> None:
    # busca o resumo das doações no banco de dados
    summary = get_donation_summary(db)

    # busca a quantidade total de doações cadastradas
    total_donations = get_total_donations(db)

    # busca a quantidade total de itens doados
    total_items = get_total_items(db)

    # exibe o total de doações no label
    ui.totalDonationsValueLabel.setText(str(total_donations))

    # exibe o total de itens doados no relatório
    ui.totalItemsValueLabel.setText(str(total_items))

    # verifica se existem doações cadastradas
    if summary:
        # o primeiro item é o mais doado, pois a consulta está em ordem decrescente
        top_food = str(summary[0]["food"])

        # exibe o alimento mais doado no relatório
        ui.topFoodValueLabel.setText(top_food)
    else:
        # exibe um traço caso não existam doações
        ui.topFoodValueLabel.setText("-")

    # limpa os dados que já estiverem na tabela
    ui.reportTable.setRowCount(0)

    # percorre cada alimento retornado pela consulta
    for item in summary:
        # pega o número da próxima linha disponivel
        row = ui.reportTable.rowCount()

        ui.reportTable.insertRow(row)

        # adiciona o nome do alimento na primeira coluna
        ui.reportTable.setItem(row, 0, QTableWidgetItem(str(item["food"])))

        # adiciona a quantidade total na segunda coluna
        ui.reportTable.setItem(row, 1, QTableWidgetItem(str(item["quantity"])))


# função que atualiza os dados do relatório e depois abre a página
def open_report_page() -> None:
    load_report()

    ui.stackedWidget.setCurrentWidget(ui.reportPage)


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

# Página inicial para Edição de doação
ui.editButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.editPage))

# Edição de doação para Página inicial
ui.editBackButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.homePage))

# Página inicial para Página de excluir doação
ui.deleteButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.deletePage))

# Página de excluir doação para Página inicial
ui.deleteBackButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.homePage))

# Página inicial para Página de relatórios
ui.reportButton.clicked.connect(open_report_page)

# Página de relatórios para Página inicial
ui.reportBackButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.homePage))

# Página inicial para Página de sobre
ui.aboutButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.aboutPage))

# Página de sobre para Página inicial
ui.aboutBackButton.clicked.connect(lambda: ui.stackedWidget.setCurrentWidget(ui.homePage))

# desabilita o campo de busca quando "Todos os registros" estiver selecionado
def toggle_search_field(checked: bool) -> None:
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

# carrega uma doação buscada pelo id
ui.editSearchButton.clicked.connect(load_donation_for_edit)

# salva a edição da doação
ui.saveEditButton.clicked.connect(save_donation_edit)

# carrega uma doação buscada pelo id para exclusão
ui.deleteSearchButton.clicked.connect(load_donation_for_delete)

# confirma a exclusão da doação
ui.confirmDeleteButton.clicked.connect(confirm_delete_donation)

# atualiza os dados do relatório
ui.refreshReportButton.clicked.connect(load_report)

# mostra a janela do sistema
window.show()

sys.exit(app.exec())
