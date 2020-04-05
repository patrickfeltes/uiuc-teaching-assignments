from flask import Flask
import database

app = Flask(__name__)

@app.route('/instructors', methods = ['GET'])
def get_instructors():
    return database.get_instructors()

@app.route('/courses', methods = ['GET'])
def get_courses():
    return database.get_courses()

@app.route('/assignments', methods = ['GET'])
def get_assignments():
    return database.get_assignments()





if __name__ == '__main__':
    database.create_tables()

    app.run(debug = True)