import sys

from PySide6.QtWidgets import QApplication

from database.connection import create_connection, create_tables
from src.models.donation_model import find_donation_by_id, insert_donation, find_donations_by_name


app = QApplication(sys.argv)

db = create_connection()

if db is not None:
    create_tables(db)
