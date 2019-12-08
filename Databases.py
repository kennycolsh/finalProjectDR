import mysql.connector
#import dbconfig as config
from dbconfig import Configer

class CarsDAO:
    db = mysql.connector.connect(
        host =Configer.mysql['host'],
        user =Configer.mysql['username'],
        password=Configer.mysql["password"],
        database=Configer.mysql["database"]
    )
    
  
       # self.db = mysql.connector.connect(
        #host ="localhost", user="root",
       # password="",database="popcars"
       # )

    def create(self,values):
        
        cursor = self.db.cursor()
        sql="insert into cars (reg, make, model, price, totalvotes) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
        #return 1

    
    def update(self,values):

        cursor = self.db.cursor()
        sql="update cars set reg =%s,make =%s,model =%s,price =%s,totalvotes =%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def getall(self):
        cursor = self.db.cursor()
        sql="select * from cars"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray =[]
        for result in results:
            returnArray.append(self.converttodic(result))

        return returnArray

    def findbyid(self,id):
        cursor = self.db.cursor()
        sql="select * from cars where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.converttodic(result)

    def delete(self,id):
        cursor = self.db.cursor()
        sql="DELETE from cars where id= %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()

    def converttodic(self, result):
        colname =['id','reg','make','model','price','totalvotes']
        item={}
        if result:
            for i, colName in enumerate(colname):
                value = result[i]
                item[colName] = value
        return item

#####################VOTES#########################
    def getLeaderboard(self):
        cursor = self.db.cursor()
        sql="select * from cars order by totalvotes asc"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray =[]
        for result in results:
            returnArray.append(self.converttodic(result))

        return returnArray

    def updateleader(self,values):
        cursor = self.db.cursor()
        sql="update cars set totalvotes =%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()


carsDAO = CarsDAO()








