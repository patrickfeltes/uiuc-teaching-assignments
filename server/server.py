from flask import Flask, request
import database
import json

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

@app.route('/related_instructor', methods = ['GET'])
def get_related_instructors():
    return database.get_related_instructors()    

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
    json['assignmentID'] = database.insert_assignment(json)
    return json

@app.route('/related_instructor', methods = ['POST'])
def insert_related_instructor():
    json = request.json
    json['relatedID'] = database.insert_related_instructor(json)
    return json

@app.route('/instructor/<instructor_id>', methods = ['DELETE'])
def delete_instructor(instructor_id):
    return database.delete_instructor(instructor_id)

@app.route('/course/<course_id>', methods = ['DELETE'])
def delete_course(course_id):
    return database.delete_course(course_id)

@app.route('/assignment/<assignment_id>', methods = ['DELETE'])
def delete_assignment(assignment_id):
    return database.delete_assignment(assignment_id)

@app.route('/related_instructor/<related_id>', methods = ['DELETE'])
def delete_related_instructor(related_id):
    return database.delete_related_instructor(related_id)

@app.route('/instructor', methods = ['PUT'])
def update_instructor():
    json = request.json
    return database.update_instructor(json)

@app.route('/course', methods = ['PUT'])
def update_course():
    json = request.json
    return database.update_course(json)

@app.route('/assignment', methods = ['PUT'])
def update_assignment():
    json = request.json
    return database.update_assignment(json)

@app.route('/related_instructor', methods = ['PUT'])
def update_related_instructor():
    json = request.json
    return database.update_related_instructor(json)

if __name__ == '__main__':
    app.run(debug = False)