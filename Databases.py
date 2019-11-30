import mysql.connector

class CarsDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host ="localhost", user="root",
        password="",database="popcars"
        )

    def create(self,values):
        cursor = self.db.cursor()
        sql="insert into cars (reg, make, model, price, totalvotes) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid


    def update(self,values):
        cursor = self.db.cursor()
        sql="update cars set reg =%s,make =%s,model =%s,price =%s,totalvotes =%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def getall(self):
        cursor = self.db.cursor()
        sql="select * from cars"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def findbyid(self,id):
        cursor = self.db.cursor()
        sql="select * from cars where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result

    def delete(self,id):
        cursor = self.db.cursor()
        sql="DELETE from cars where id= %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")

carsDAO = CarsDAO()








