from pathlib import Path

from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QMessageBox


def create_connection() -> QSqlDatabase | None:
    # define o caminho do banco de dados no mesmo diretório do connection.py
    db_path = Path(__file__).resolve().parent / "donations.db"
    
    # cria a conexão utilizando o SQLite
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(str(db_path))

    # verifica se a conexão com o banco de dados foi aberta
    if not db.open():
        QMessageBox.critical(None, "Erro ao abrir o banco de dados", db.lastError().text())  
        return None
    
    # retorna a conexão aberta
    return db


def create_tables(db: QSqlDatabase) -> bool:
    # define o caminho do arquivo que contém a estrutura do banco
    schema_path = Path(__file__).resolve().parent / "schema.sql"
    
    # lê os comandos SQL do arquivo
    with open(schema_path, "r", encoding="utf-8") as file:
        schema = file.read()

    # cria uma consulta utilizando a conexão com o banco
    query = QSqlQuery(db)

    # executa o comando SQL responsável pela criação das tabelas
    if not query.exec(schema):
        QMessageBox.critical(None, "Erro ao criar as tabelas", query.lastError().text())
        return False  
    
    # retorna True se as tabelas forem criadas com sucesso
    return True 
