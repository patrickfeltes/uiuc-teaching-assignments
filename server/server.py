from flask import Flask, request
import database

app = Flask(__name__)

@app.route('/instructor', methods = ['GET'])
def get_instructors():
    return database.get_instructors()

@app.route('/course', methods = ['GET'])
def get_courses():
    return database.get_courses()

@app.route('/assignment', methods = ['GET'])
def get_assignments():
    return database.get_assignments()

@app.route('/instructor', methods = ['POST'])
def insert_instructor():
    json = request.json
    json['instructorID'] = database.insert_instructor(json)
    return json

@app.route('/course', methods = ['POST'])
def insert_course():
    json = request.json
    json['courseID'] = database.insert_course(json)
    return json

@app.route('/assignment', methods = ['POST'])
def insert_assignment():
    json = request.json
    database.insert_assignment(json)
    return json

if __name__ == '__main__':
    database.create_tables()
    app.run(debug = True)