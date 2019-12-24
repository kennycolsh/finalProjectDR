import mysql.connector
class Configer:
    mysql={
        'host' : "localhost",# "kennycolsh.mysql.pythonanywhere-services.com",# "localhost",
        'username': "root", #"root",
        'password': "" , #"Lesharp12",
        'port': "3308" , #"Lesharp12",
        'database':"popcars" ##"kennycolsh$popcars"
    }

           # self.db = mysql.connector.connect(
        #host ="localhost", user="root",
       # password="",database="popcars"
       # )
configer = Configer()