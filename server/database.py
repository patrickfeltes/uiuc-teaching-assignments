import mysql.connector
import json

connection = mysql.connector.connect(user='root', host='localhost', database='teaching_assignments')

def create_tables():
    cursor = connection.cursor()
    cursor.execute('SHOW TABLES')
    existing_tables = list(map(lambda x : x[0], cursor.fetchall()))

    instructor_table_query = '''
        CREATE TABLE `instructor` (
            `instructorID` int(11) NOT NULL AUTO_INCREMENT,
            `name` varchar(255) NOT NULL,
            `qualifications` varchar(255),
            `atUIUC` BOOLEAN,
            `semesterAvailable` varchar(255),
            PRIMARY KEY (`instructorID`)
        )
    '''
    if 'instructor' not in existing_tables:
        cursor.execute(instructor_table_query)

    course_table_query = '''
        CREATE TABLE `course` (
            `courseID` int(11) NOT NULL AUTO_INCREMENT,
            `crn` int(11) NOT NULL,
            `semester` varchar(255),
            `description` varchar(255),
            `numStudents` int(11),
            `dept` varchar(255),
            `undergrad` BOOLEAN,
            `year` int(11),
            `online` BOOLEAN,
            `creditHours` int(11),
            PRIMARY KEY (`courseID`)
        )
    '''

    if 'course' not in existing_tables:
        cursor.execute(course_table_query)

    assignment_table_query = '''
        CREATE TABLE `assignment` (
            `assignmentID` int(11) NOT NULL AUTO_INCREMENT,
            `instructorID` int(11) NOT NULL,
            `courseID` int(11) NOT NULL,
            PRIMARY KEY (`assignmentID`),
            FOREIGN KEY (`instructorID`) REFERENCES `instructor` (`instructorID`) ON DELETE CASCADE,
            FOREIGN KEY (`courseID`) REFERENCES `course` (`courseID`) ON DELETE CASCADE
        )
    '''

    if 'assignment' not in existing_tables:
        cursor.execute(assignment_table_query)

    cursor.close()

def get_from_table(table_name):
    cursor = connection.cursor()
    query = f'SELECT * FROM {table_name}'
    cursor.execute(query)
    
    results = cursor.fetchall()
    key_names = list(map(lambda x : x[0], cursor.description))
    keyed_results = list(map(lambda x : dict(zip(key_names, x)), results))
    json_string = json.dumps(keyed_results)

    cursor.close()
    return json_string

def get_instructors():
    return get_from_table('instructor')

def get_courses():
    return get_from_table('course')

def get_assignments():
    return get_from_table('assignment')

def insert_instructor(json):
    cursor = connection.cursor()
    
    query = f'''
        INSERT INTO instructor
        VALUES(NULL, '{json['name']}', '{json['qualifications']}', {json['atUIUC']}, '{json['semesterAvailable']}')
    '''
    cursor.execute(query)
    connection.commit()
    new_primary_key = cursor.lastrowid

    cursor.close()
    return new_primary_key

def insert_course(json):
    cursor = connection.cursor()
    
    query = f'''
        INSERT INTO course
        VALUES(NULL, {json['crn']}, '{json['semester']}', '{json['description']}', {json['numStudents']}, '{json['dept']}', {json['undergrad']}, {json['year']}, {json['online']}, {json['creditHours']})
    '''
    cursor.execute(query)
    connection.commit()
    new_primary_key = cursor.lastrowid

    cursor.close()
    return new_primary_key

def insert_assignment(json):
    cursor = connection.cursor()
    
    query = f'''
        INSERT INTO assignment
        VALUES(NULL, {json['instructorID']}, {json['courseID']})
    '''
    cursor.execute(query)
    connection.commit()
    new_primary_key = cursor.lastrowid

    cursor.close()
    return new_primary_key

def delete_instructor(instructor_id):
    cursor = connection.cursor()

    select_query = f'SELECT * FROM instructor WHERE instructorID = {instructor_id} LIMIT 1'
    cursor.execute(select_query)
    result = cursor.fetchall()[0]
    key_names = list(map(lambda x : x[0], cursor.description))
    json_result = json.dumps(dict(zip(key_names, result)))

    delete_query = f'DELETE FROM instructor WHERE instructorID = {instructor_id}'
    cursor.execute(delete_query)
    connection.commit()

    cursor.close()

    return json_result

def delete_course(course_id):
    cursor = connection.cursor()

    select_query = f'SELECT * FROM course WHERE courseID = {course_id} LIMIT 1'
    cursor.execute(select_query)
    result = cursor.fetchall()[0]
    key_names = list(map(lambda x : x[0], cursor.description))
    json_result = json.dumps(dict(zip(key_names, result)))

    delete_query = f'DELETE FROM course WHERE courseID = {course_id}'
    cursor.execute(delete_query)
    connection.commit()

    cursor.close()

    return json_result

def delete_assignment(assignment_id):
    cursor = connection.cursor()

    select_query = f'SELECT * FROM assignment WHERE assignmentID = {assignment_id} LIMIT 1'
    cursor.execute(select_query)
    result = cursor.fetchall()[0]
    key_names = list(map(lambda x : x[0], cursor.description))
    json_result = json.dumps(dict(zip(key_names, result)))

    delete_query = f'DELETE FROM assignment WHERE assignmentID = {assignment_id}'
    cursor.execute(delete_query)
    connection.commit()

    cursor.close()

    return json_result

def update_instructor(obj):
    cursor = connection.cursor()
    
    update_query = f'''
        UPDATE instructor
        SET name = '{obj['name']}', qualifications = '{obj['qualifications']}', atUIUC = {obj['atUIUC']}, semesterAvailable = '{obj['semesterAvailable']}'
        WHERE instructorID = {obj['instructorID']}
    '''

    cursor.execute(update_query)
    connection.commit()

    select_query = f'SELECT * FROM instructor WHERE instructorID = ' + str(obj['instructorID']) + ' LIMIT 1'
    cursor.execute(select_query)
    result = cursor.fetchall()[0]
    key_names = list(map(lambda x : x[0], cursor.description))
    json_result = json.dumps(dict(zip(key_names, result)))

    cursor.close()

    return json_result

def update_course(obj):
    cursor = connection.cursor()
    
    update_query = f'''
        UPDATE course
        SET crn = {obj['crn']}, semester = '{obj['semester']}', description = '{obj['description']}', numStudents = {obj['numStudents']}, dept = '{obj['dept']}', undergrad = {obj['undergrad']}, year = {obj['year']}, online = {obj['online']}, creditHours = {obj['creditHours']}
        WHERE courseID = {obj['courseID']}
    '''

    cursor.execute(update_query)
    connection.commit()

    select_query = f'SELECT * FROM course WHERE courseID = ' + str(obj['courseID']) + ' LIMIT 1'
    cursor.execute(select_query)
    result = cursor.fetchall()[0]
    key_names = list(map(lambda x : x[0], cursor.description))
    json_result = json.dumps(dict(zip(key_names, result)))

    cursor.close()

    return json_result

def update_assignment(obj):
    cursor = connection.cursor()

    update_query = f'''
        UPDATE assignment
        SET instructorID = {obj['instructorID']}, courseID = {obj['courseID']}
        WHERE assignmentID = {obj['assignmentID']}
    '''

    cursor.execute(update_query)
    connection.commit()

    select_query = f'SELECT * FROM assignment WHERE assignmentID = ' + str(obj['assignmentID']) + ' LIMIT 1'
    cursor.execute(select_query)
    result = cursor.fetchall()[0]
    key_names = list(map(lambda x : x[0], cursor.description))
    json_result = json.dumps(dict(zip(key_names, result)))

    cursor.close()

    return json_result
