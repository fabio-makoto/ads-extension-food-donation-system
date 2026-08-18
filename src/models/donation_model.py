from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QMessageBox


def insert_donation(db: QSqlDatabase, name: str, food: str, quantity: int, date: str) -> bool:
    # cria uma consulta associada à conexão com o banco de dados
    query = QSqlQuery(db)

    # prepara o comando SQL utilizando parâmetros para receber os valores
    query.prepare("""
        INSERT INTO donations (name, food, quantity, date)
        VALUES (:name, :food, :quantity, :date)
    """)

    # associa os valores recebidos pela função aos parâmetros do comando SQL
    query.bindValue(":name", name)
    query.bindValue(":food", food)
    query.bindValue(":quantity", quantity)
    query.bindValue(":date", date)

    if not query.exec():
        # se o comando SQL não rodar, aparecerá um pop-up com a mensagem de erro retornado pelo QtSql
        QMessageBox.critical(None, "Erro ao cadastrar doação", query.lastError().text())
        return False
    
    # retorna True se a doação for inserida com sucesso
    return True


def find_donation_by_id(db: QSqlDatabase, donation_id: int) -> None:
    # cria uma consulta associada à conexão com o banco de dados
    query = QSqlQuery(db)

    # prepara o comando SQL para buscar uma doação pelo ID
    query.prepare("""
        SELECT id, name, food, quantity, date
        FROM donations
        WHERE id = :id
    """)

    # associa o ID recebido ao parâmetro do comando SQL
    query.bindValue(":id", donation_id)

    if not query.exec():
        # se o comando SQL não rodar, aparecerá um pop-up com a mensagem de erro retornado pelo QtSql
        QMessageBox.critical(None, "Erro ao consulta doação", query.lastError().text())
        return None

    if query.next():
        # verifica se a consulta encontrou algum registro
        return {
            "id": query.value("id"),
            "name": query.value("name"),
            "food": query.value("food"),
            "quantity": query.value("quantity"),
            "date": query.value("date")
        }
    
    return None


def find_donations_by_name(db: QSqlDatabase, name: str) -> list[dict]:
    query = QSqlQuery(db)

    # prepara a consulta para buscar doações que contenham o nome informado
    query.prepare("""
        SELECT id, name, food, quantity, date
        FROM donations
        WHERE name LIKE :name
        ORDER BY name, id
    """)

    # adiciona % antes e depois do nome para permitir uma busca parcial
    query.bindValue(":name", f"%{name}%")

    if not query.exec():
        # verifica se ocorreu algum erro ao executar a consulta
        QMessageBox.critical(None, "Erro ao consultar doações", query.lastError().text())
        return []
    
    donations = []

    # percorre todos os registros encontrados pela consulta
    while query.next():
        donation = {
            "id": query.value("id"),
            "name": query.value("name"),
            "food": query.value("food"),
            "quantity": query.value("quantity"),
            "date": query.value("date")
        }

        donations.append(donation)
    
    return donations

