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

@app.route('/instructor/<instructor_id>', methods = ['DELETE'])
def delete_instructor(instructor_id):
    return database.delete_instructor(instructor_id)

@app.route('/course/<course_id>', methods = ['DELETE'])
def delete_course(course_id):
    return database.delete_course(course_id)

@app.route('/assignment', methods = ['DELETE'])
def delete_assignment():
    instructor_id = request.args['instructor_id']
    course_id = request.args['course_id']
    return database.delete_assignment(instructor_id, course_id)

@app.route('/instructor', methods = ['PUT'])
def update_instructor():
    json = request.json
    return database.update_instructor(json)

@app.route('/course', methods = ['PUT'])
def update_course():
    json = request.json
    return database.update_course(json)

if __name__ == '__main__':
    database.create_tables()
    app.run(debug = True)