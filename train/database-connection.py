class DatabaseConnection():
    connected: bool
    db_name: str
    def __init__(self, db_name: str):
        self.connected = False
        self.db_name = db_name

    def __enter__(self):
        self.connected = True
        print(f'Connected from inside {self.db_name}')
        return self

    def __exit__(self, exc_type, exc_value, stacktrace):
        self.connected = False
        print('Desconnected')

with DatabaseConnection('MyConn') as db:
    print(f"I`m executing something --> {db.connected}")