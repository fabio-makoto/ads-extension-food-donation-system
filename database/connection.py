from pathlib import Path

from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QMessageBox


def create_connection():
    # cria o caminho onde o banco de dados será criado, que será no diretório atual do connection.py
    db_path = Path(__file__).resolve().parent / "donations.db"
    
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(str(db_path))  # cria o banco de dados

    if not db.open():
        # se o banco de dados não abrir, mostra uma mensagem de erro do próprio QtSql
        QMessageBox.critical(None, "Erro ao abrir o banco de dados", db.lastError().text())  
        return None
    
    return db  # retorna o banco de dados aberto
