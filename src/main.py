import sys

from PySide6.QtWidgets import QApplication

from database.connection import create_connection, create_tables


app = QApplication(sys.argv)

db = create_connection()

if db is not None:
    create_tables(db)

