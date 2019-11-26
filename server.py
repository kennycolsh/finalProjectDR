#!flask/bin/python
from flask import Flask , jsonify,  request, abort, make_response

#app = Flask(__name__, static_url_path='', static_folder='.')
app = Flask(__name__)
cars = [
    {
        "id":1, "reg":"181 G 1234","make":"Ford", "model":"Modeo", "price":18000, "totalvotes":2
    },
    {
        "id":2, "reg":"11 MO 1234", "make":"Nissan", "model":"Almera", "price":1245, "totalvotes":3
    },
    {
        "id":3, "reg":"test", "make":"Nissan", "model":"Almera", "price":6587, "totalvotes":4
    },
     {
         "id":4, "reg":"12 D 1234", "make":"Nissan", "model":"Almera", "price":12457, "totalvotes":5
    }
]
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
    return jsonify( {'Get All cars':cars})

#curl "http://127.0.0.1:5000/cars/1"
@app.route('/cars/<int:id>')
def findbyID(id):
    foundCars = list(filter(lambda c : c['id'] == id , cars))
    if len(foundCars) == 0:
        return jsonify( { 'car' : '' }),204
    return jsonify( { 'car' : foundCars[0] })
  

#CREATE
# sample test
# curl -i -H "Content-Type:application/json" -X POST -d '{"id":5,"reg":"12 D 99999","make":"Fiat","model":"Punto","price":3000}' http://localhost:5000/cars
# for windows use this one
# curl -i -H "Content-Type:application/json" -X POST -d "{\"id\":\0,\"reg\":\"12 D 1234\",\"make\":\"Fiat\",\"model\":\"Punto\",\"price\":3000}" http://localhost:5000/cars
@app.route('/cars', methods=['POST'])
def create():
    global nextID
    if not request.json:
        abort(400)
    if not 'id' in request.json:
        abort(550)
    car={
        "id":  nextID,
        "reg":  request.json['reg'],
        "make": request.json['make'],
        "model":request.json['model'],
        "price":request.json['price'],
        "totalvotes":0
    }
    nextID += 1
    cars.append(car)
    return jsonify( {'car':car }),201
    
 #UPDATE   
 #curl -i -H "Content-Type:application/json" -X PUT -d "{\"reg\":\"12 D 1234\",\"make\":\"Fiat\",\"model\":\"uno\",\"price\":9900}" http://localhost:5000/cars/1
 #curl -i -H "Content-Type:application/json" -X PUT -d "{\"make\":\"jjjjsta\"}" http://localhost:5000/cars/1
@app.route('/cars/<int:id>', methods=['PUT'])
def update(id):
    foundCars=list(filter(lambda t : t['id'] ==id, cars))
    if len(foundCars) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'reg' in request.json and type(request.json['reg']) != str:
        abort(400)
    if 'make' in request.json and type(request.json['make']) != str:
        abort(400)
    if 'model' in request.json and type(request.json['model']) is not str:
        abort(400)
    if 'price' in request.json and type(request.json['price']) is not int:
        abort(400)
    foundCars[0]['reg']  = request.json.get('reg', foundCars[0]['reg'])
    foundCars[0]['make']  = request.json.get('make', foundCars[0]['make'])
    foundCars[0]['model'] =request.json.get('model', foundCars[0]['model'])
    foundCars[0]['price'] =request.json.get('price', foundCars[0]['price'])
    return jsonify( {'car':foundCars[0]})

#DELETE
#curl -X DELETE "http://127.0.0.1:5000/cars/2"
@app.route('/cars/<int:id>', methods=['DELETE'])
def delete(id):
    foundCars = list(filter (lambda t : t['id'] == id, cars))
    if len(foundCars) == 0:
        abort(404)
    cars.remove(foundCars[0])
    return  jsonify( { 'Car Removed':True })

########VOTING#######################################################################


#leader board
@app.route('/vote/leaderboard', methods=['GET'])
def getLeaderboard():
    cars.sort(key=lambda x: x['totalvotes'], reverse =True)
    return jsonify(cars)

#CREATE
# curl -X POST "http://127.0.0.1:5000/vote/1
@app.route('/vote/<int:carid>', methods=['POST'])
def addvote(carid):
    foundCars=list(filter(lambda t : t['id'] == carid, cars))
    if len(foundCars) == 0:
        abort(404)
    if not request.json:
        abort(400) 
    if 'votes' in request.json and type(request.json['votes']) is not int:
        abort(401)   
    newvote = request.json['votes']
    foundCars[0]['totalvotes']  += newvote

    return jsonify(foundCars[0])


##################ERROR HANDLING ########################################################
@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)
if __name__ == '__main__' :
    app.run(debug= True)