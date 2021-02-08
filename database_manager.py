import sql_commands as sql
import sqlite3
from sqlite3 import Error


class DatabaseManager:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        """ create a table from the create_table_sql statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(sql.sql_create_data_table)
        except Error as e:
            print(f"error creating table: {e}")

    def insert_row_data(self, entry):
        """
        Create a new task
        :param entry:
        :return:
        """
        try:
            cur = self.conn.cursor()
            cur.execute(sql.sql_insert, entry)
            self.conn.commit()
        except Error as e:
            print(f"error inserting row: {e}")

        return cur.lastrowid
