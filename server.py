#!flask/bin/python
from flask import Flask , jsonify,  request, abort, make_response
from Databases import carsDAO
import mysql.connector


#app = Flask(__name__, static_url_path='', static_folder='.')
app = Flask(__name__)
#cars = [
#    {
 #       "id":1, "reg":"181 G 1234","make":"Ford", "model":"Modeo", "price":18000, "totalvotes":2
#    },
#    {
 #       "id":2, "reg":"11 MO 1234", "make":"Nissan", "model":"Almera", "price":1245, "totalvotes":3
 #   },
 #   {
 #       "id":3, "reg":"test", "make":"Nissan", "model":"Almera", "price":6587, "totalvotes":4
 #   },
 #    {
 #        "id":4, "reg":"12 D 1234", "make":"Nissan", "model":"Almera", "price":12457, "totalvotes":5
 #   }
#]
Votes = [
    {
        "id":1, "name":"first act"
    },
    {
        "id":2, "name":"second Act"
    }
 
]
nextID = 5

nextVID = 3


#curl "http://127.0.0.1:5000/cars"
@app.route('/cars', methods=['GET'])
def get_cars():
    allcars = carsDAO.getall() 
    return jsonify(allcars)

#curl "http://127.0.0.1:5000/cars/1"
@app.route('/cars/<int:id>')
def findbyID(id):
    foundCar = carsDAO.findbyid(id)
    return jsonify(foundCar)
  

#CREATE
# sample test
# curl -i -H "Content-Type:application/json" -X POST -d '{"id":5,"reg":"12 D 99999","make":"Fiat","model":"Punto","price":3000}' http://localhost:5000/cars
# for windows use this one
#curl -i -X POST -H "Content-Type:application/json" -d "{\"reg\":\"12 D 1234\",\"make\":\"Fiat\",\"model\":\"cied\",\"price\":\"12345\",\"totalvotes\":\"1\" }" http://localhost:5000/cars
@app.route('/cars', methods=['POST'])
def create():

    if not request.json:
        abort(400)

    car={
        
        "reg":  request.json['reg'],
        "make": request.json['make'],
        "model":request.json['model'],
        "price":request.json['price'],
        "totalvotes":request.json['totalvotes'],
    }
    
    values =(car['reg'],car['make'],car['model'],car['price'],car['totalvotes'])
    newid = carsDAO.create(values)
    car['id']= newid
    return jsonify(car)
    
 #UPDATE   
 #curl -i -H "Content-Type:application/json" -X PUT -d "{\"reg\":\"12 D 1234\",\"make\":\"Fiat\",\"model\":\"uno\",\"price\":9900}" http://localhost:5000/cars/1
 #curl -i -H "Content-Type:application/json" -X PUT -d "{\"reg\":\"12 D 1234\",\"make\":\"Fiat\",\"model\":\"cied\",\"price\":\"12345\",\"totalvotes\":\"1\" }" http://localhost:5000/cars/10
@app.route('/cars/<int:id>', methods=['PUT'])
def update(id):
    foundCars=carsDAO.findbyid(id)
    if not foundCars:
      abort(404)

    if not request.json:
       abort(400)
    
    reqjson = request.json

    if 'reg' in reqjson: 
        foundCars['reg'] =reqjson['reg']
        
    if 'make' in reqjson: 
        foundCars['make'] =reqjson['make']
        
    if 'model' in reqjson: 
        foundCars['model'] =reqjson['model']
        
    if 'price' in reqjson: 
        foundCars['price'] =reqjson['price']
        
    if 'totalvotes' in reqjson: 
        foundCars['totalvotes'] =reqjson['totalvotes']
        

    values =(foundCars['reg'],foundCars['make'],foundCars['model'],foundCars['price'],foundCars['totalvotes'],foundCars['id'])
    
    carsDAO.update(values)
    return jsonify(foundCars)

#DELETE
#curl -X DELETE "http://127.0.0.1:5000/cars/2"
@app.route('/cars/<int:id>', methods=['DELETE'])
def delete(id):
    carsDAO.delete(id)
    return  jsonify( { 'Car Removed':True })

########VOTING#######################################################################


#leader board
@app.route('/vote/leaderboard', methods=['GET'])
def getLeaderboard():
    allvotes = carsDAO.getall() 
    return jsonify(allvotes)

#CREATE
# curl -X POST "http://127.0.0.1:5000/vote/1
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"totalvotes\":\"12\" }" http://localhost:5000/vote/10
@app.route('/vote/<int:id>', methods=['PUT'])
def addvote(id):
    foundCars=carsDAO.findbyid(id)
    if not foundCars:
      abort(404)

    if not request.json:
       abort(400)
    
    reqjson = request.json
    #newvote =  parseInt(reqjson['totalvotes'])
    #oldvote =  parseInt(foundCars['totalvotes'])

    #finalvote = newvote + oldvote

    if 'totalvotes' in reqjson:
        foundCars['totalvotes'] =  reqjson['totalvotes'] 
    
    values =(foundCars['totalvotes'] ,foundCars['id'])
    
    carsDAO.updateleader(values)
    return jsonify(foundCars)


##################ERROR HANDLING ########################################################
@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)
    
if __name__ == '__main__' :
    app.run(debug= True)