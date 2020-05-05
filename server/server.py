from flask import Flask, request, jsonify
import database
import json
import model

app = Flask(__name__)



@app.route('/instructor', methods = ['GET'])
def get_instructors():
    if request.args.get('instructor_id') is not None:
        instructor_id = request.args.get('instructor_id')
        return database.get_attributes_of_instructor(instructor_id)
    else:
        return database.get_instructors()

@app.route('/course', methods = ['GET'])
def get_courses():
    if request.args.get('instructor_id') is not None:
        instructor_id = request.args.get('instructor_id')
        return database.get_courses_taught_by_instructor(instructor_id)
    else:
        return database.get_courses()


@app.route('/assignment', methods = ['GET'])
def get_assignments():
    return database.get_assignments()

@app.route('/related_instructor', methods = ['GET'])
def get_related_instructors():
    if request.args.get('instructor_id') is not None:
        instructor_id = request.args.get('instructor_id')
        return database.get_instructors_related_to_this_one(instructor_id)
    else:
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

@app.route('/update_similarities', methods = ['GET'])
def update_similarities():
    model.compute_similarities()
    resp = jsonify(success=True)
    return resp

@app.route('/attributes_of_course', methods = ['GET'])
def attributes_of_course():
    course_id = request.args.get('course_id')
    return database.get_attributes_of_course(course_id)

@app.route('/get_instructors_who_taught_this_course', methods = ['GET'])
def instructors_who_taught_this_course():
    course_id = request.args.get('course_id')
    return database.get_instructors_who_taught_this_course(course_id)

@app.route('/get_courses_related_to_this_one', methods = ['GET'])
def courses_related_to_this_one():
    course_id = request.args.get('course_id')
    return database.get_courses_related_to_this_one(course_id)

@app.route('/get_recommended_courses', methods = ['GET'])
def get_recommended_courses():
    instructor_id = request.args.get('instructor_id')
    return model.best_courses(instructor_id)


if __name__ == '__main__':
    app.run(debug = False)
