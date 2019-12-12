#!/usr/bin/env python
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
class Configsnow:
    #engine = create_engine(
        ##'snowflake://{user}:{password}@{account}/'.format(
            #user='kenny.colsh@alkermes.com',
            #password='Qazplm13',
            #account='fh25363.us-east-1.privatelink',
        #)
    #)

    def work():
        engine1 = create_engine(URL(
        account = 'fh25363.us-east-1.privatelink',
        user = 'kenny.colsh@alkermes.com',
        password = 'Qazplm13',
        database = 'DEVELOPMENT_POC',
        schema = 'MAIN',
        warehouse = 'DEVELOPMENT_COMPUTE_WH',
        role='DEVELOPMENT_RW',
    ))
        connection = engine1.connect()
        try:

            #connection = engine1.connect()
            results = connection.execute('select current_version()').fetchone()
            
            results = connection.execute('select * from cars')
            returnArray =[]
            for result in results:
                colname =['reg','make','model','price','totalvotes']
                item={}
                for i, colName in enumerate(colname):
                    value = result[i]
                    item[colName] = value
                returnArray.append(item)

            print(returnArray)
            #print(results[0])
        finally:
            connection.close()
            engine1.dispose()


    work()

    def create():
        engine1 = create_engine(URL(
        account = 'fh25363.us-east-1.privatelink',
        user = 'kenny.colsh@alkermes.com',
        password = 'Qazplm13',
        database = 'DEVELOPMENT_POC',
        schema = 'MAIN',
        warehouse = 'DEVELOPMENT_COMPUTE_WH',
        role='DEVELOPMENT_RW',
    ))
        connection = engine1.connect()
        try:
            #connection = engine1.connect()
            #results = connection.execute('select current_version()').fetchone()
            connection.execute('insert into cars (reg, make, model, price, totalvotes) values(select reg, make, model, price, totalvotes from cars)')
            return 1
        finally:
            connection.close()
            engine1.dispose()
    create()

configsnow= Configsnow()