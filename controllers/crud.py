from sqlalchemy import text
import sys
from pprint import pprint


class crud_controller:
    def __init__(self, conn, table):
        self.conn = conn
        self.table = table

    def getAll(self):
        stmp = self.conn.execute(self.table.select())
        return [x.items() for x in stmp]

    def get(self, where):
        stmp = self.conn.execute(text("SELECT * FROM "+str(self.table)+" WHERE "+where))
        return [x.items() for x in stmp]

    def insert(self, obj):
        stmp = self.conn.execute(self.table.insert(), obj)
        return stmp.keys()

    def raw(self, query):
        stmp = self.conn.execute(text(query))
        return [x.items() for x in stmp]
