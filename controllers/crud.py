from sqlalchemy import text
import sys
from pprint import pprint


class crud_controller:
    def __init__(self, conn, table):
        self.conn = conn
        self.table = table

    def getAll(self):
        stmp = self.conn.execute(self.table.select())
        return stmp

    def get(self, where):
        stmp = self.conn.execute(text("SELECT * FROM "+str(self.table)+" WHERE "+where))
        return stmp

    def insert(self, obj):
        stmp = self.conn.execute(self.table.insert(), obj)
        return stmp

    def raw(self, query):
        stmp = self.conn.execute(text(query))
        return stmp
