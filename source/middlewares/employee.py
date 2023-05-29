import connect

class employee():
    def __init__(self):
        self.db = connect.login()
        