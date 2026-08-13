from pathlib import Path

from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QMessageBox


def create_connection() -> QSqlDatabase | None:
    # define o caminho do banco de dados no mesmo diretório do connection.py
    db_path = Path(__file__).resolve().parent / "donations.db"
    
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(str(db_path))  # define o caminho do banco de dados

    if not db.open():
        # se o banco de dados não abrir, mostra uma mensagem de erro do próprio QtSql
        QMessageBox.critical(None, "Erro ao abrir o banco de dados", db.lastError().text())  
        return None
    
    return db  # retorna o banco de dados aberto


def create_tables(db: QSqlDatabase) -> bool: 
    schema_path = Path(__file__).resolve().parent / "schema.sql"  # pega o caminho do arquivo schema.sql
    
    with open(schema_path, "r", encoding="utf-8") as file:
        schema = file.read()  # lê o arquivo schema.sql e armazena na variável schema

    query = QSqlQuery(db)

    if not query.exec(schema):  # executa o comando SQL que está no arquivo schema.sql
        # se o comando SQL não for executado, mostra uma mensagem de erro do próprio QtSql
        QMessageBox.critical(None, "Erro ao criar as tabelas", query.lastError().text())
        return False  
    
    return True  # retorna True se as tabelas forem criadas com sucesso
