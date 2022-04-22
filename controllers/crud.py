class crud_controller:
    def __init__(self, conn, table):
        self.conn = conn
        self.table = table

    def getAll(self):
        get = self.conn.execute(self.table.select())
        return [x.items() for x in get]
