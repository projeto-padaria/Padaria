import connect

connectObj = connect.Connect()

class employee():
    def __init__(self):
        self.db = connectObj.Login()

if __name__ == '__main__': 
    employee()