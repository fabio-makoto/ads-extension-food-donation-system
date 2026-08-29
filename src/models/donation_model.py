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


def find_donation_by_id(db: QSqlDatabase, donation_id: int) -> dict | None:
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
        QMessageBox.critical(None, "Erro ao consultar doação", query.lastError().text())
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
    
    donations: list[dict] = []

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


def update_donation(db: QSqlDatabase, donation_id: int, food: str, quantity: int) -> bool:
    # cria uma consulta associada à conexão com o banco de dados
    query = QSqlQuery(db)

    # prepara o comando SQL para atualizar o alimento e a quantidade da doação
    query.prepare("""
        UPDATE donations
        SET food = :food, quantity = :quantity
        WHERE id = :id
    """)

    # associa os valores recebidos aos parâmetros do comando SQL
    query.bindValue(":food", food)
    query.bindValue(":quantity", quantity)
    query.bindValue(":id", donation_id)

    if not query.exec():
        # verifica se ocorreu algum erro ao executar o update
        QMessageBox.critical(None, "Erro ao editar a doação", query.lastError().text())
        return False
    
    if query.numRowsAffected() == 0:
        # verifica se alguma doação foi encontrada e alterada
        return False
    
    return True


def delete_donation(db: QSqlDatabase, donation_id: int) -> bool:
    query = QSqlQuery(db)

    # prepara o comando SQL para excluir uma doação pelo ID
    query.prepare("""
        DELETE FROM donations
        WHERE id = :id
    """)

    # associa o ID recebido ao parâmetro do comando SQL
    query.bindValue(":id", donation_id)

    if not query.exec():
        # verifica se ocorreu algum erro ao deletar uma doação
        QMessageBox.critical(None, "Erro ao excluir doação", query.lastError().text())
        return False
    
    # verifica se alguma doação foi realmente excluída
    if query.numRowsAffected() == 0:
        return False
    
    return True


def find_all_donations(db: QSqlDatabase) -> list[dict]:
    # cria uma consulta para buscar todas as doações cadastradas
    query = QSqlQuery(db)

    # prepara a consulta para buscar todas as doações cadastradas
    # utilizando o ORDER BY para as doações mais recentes aparecerem primeiro
    query.prepare("""
        SELECT id, name, food, quantity, date
        FROM donations
        ORDER BY date DESC, id DESC
    """)

    if not query.exec():
        # verifica se ocorreu algum erro ao executar a busca
        QMessageBox.critical(None, "Erro ao listar doações", query.lastError().text())
        return []

    donations: list[dict] = []

    # percorre todos os registros encontrados
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


def get_donation_summary(db: QSqlDatabase) -> list[dict]:
    # cria a consulta utilizando a conexão com o banco de dados
    query = QSqlQuery(db)

    # agrupa os registros por alimento e soma as quantidades doadas
    query.prepare("""
        SELECT food, SUM(quantity) AS total_quantity
        FROM donations
        GROUP BY food
        ORDER BY total_quantity DESC
    """)

    # executa a consulta e retorna uma lista vazia em caso de erro
    if not query.exec():
        return []
    
    # lista que armazenará o resumo das doações
    summary: list[dict] = []

    # percorre os resultados retornados pela consulta
    while query.next():
        summary.append({
            "food": query.value("food"),
            "quantity": query.value("total_quantity")
        })
    
    # retorna os alimentos e suas respectivas quantidades totais
    return summary


def get_total_donations(db: QSqlDatabase) -> int:
    # cria a consulta utilizando a conexão com o banco de dados
    query = QSqlQuery(db)

    # conta quantas doações estão cadastradas
    query.prepare("""
        SELECT COUNT(*) AS total 
        FROM donations
    """)

    # executa a consulta e retorna zero em caso de erro
    if not query.exec():
        QMessageBox.critical(None, "Erro ao gerar relatório", query.lastError().text())
        return 0

    # verifica se a consulta retornou um resultado
    if query.next():
        return int(query.value("total"))

    return 0


def get_total_items(db: QSqlDatabase) -> int:
    # cria a consulta utilizando a conexão com o banco de dados
    query = QSqlQuery(db)

    # soma a quantidade de todos os itens doados
    query.prepare("""
        SELECT SUM(quantity) AS total
        FROM donations
    """)

    # executa a consulta e retorna zero em caso de erro
    if not query.exec():
        QMessageBox.critical(None, "Erro ao gerar relatório", query.lastError().text())
        return 0

    # verifica se a consulta retornou um resultado
    if query.next():
        total = query.value("total")

        # caso a tabela esteja vazia, SUM retorna NULL
        if total is not None:
            return int(total)
    
    return 0