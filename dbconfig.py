import mysql.connector
class Configer:
    mysql={
        'host' : "kennycolsh.mysql.pythonanywhere-services.com",# "localhost",
        'username': "kennycolsh", #"root",
        'password': "Lesharp12" , #"Lesharp12",
        #'port': "3308" , #"Lesharp12",
        'database':"kennycolsh$popcars" ##"kennycolsh$popcars"
    }

           # self.db = mysql.connector.connect(
        #host ="localhost", user="root",
       # password="",database="popcars"
       # )
configer = Configer()