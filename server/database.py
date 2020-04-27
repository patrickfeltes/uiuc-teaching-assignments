import mysql.connector.pooling
import json

connection_pool = mysql.connector.pooling.MySQLConnectionPool(user='root', host='localhost', database='teaching_assignments')

def create_tables():
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    cursor.execute('SHOW TABLES')
    existing_tables = list(map(lambda x : x[0], cursor.fetchall()))

    instructor_table_query = '''
        CREATE TABLE `instructor` (
            `instructorID` int(11) NOT NULL AUTO_INCREMENT,
            `name` varchar(255) NOT NULL,
            PRIMARY KEY (`instructorID`)
        )
    '''
    if 'instructor' not in existing_tables:
        cursor.execute(instructor_table_query)

    course_table_query = '''
        CREATE TABLE `course` (
            `courseID` int(11) NOT NULL AUTO_INCREMENT,
            `courseNumber` int(11) NOT NULL,
            `description` varchar(255),
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
            `semester` varchar(255),
            PRIMARY KEY (`assignmentID`),
            FOREIGN KEY (`instructorID`) REFERENCES `instructor` (`instructorID`) ON DELETE CASCADE,
            FOREIGN KEY (`courseID`) REFERENCES `course` (`courseID`) ON DELETE CASCADE
        )
    '''

    if 'assignment' not in existing_tables:
        cursor.execute(assignment_table_query)

    related_instructor_query = '''
        CREATE TABLE `related_instructor` (
            `relatedID` int(11) NOT NULL AUTO_INCREMENT,
            `relatedInstructorID1` int(11) NOT NULL,
            `relatedInstructorID2` int(11) NOT NULL,
            PRIMARY KEY (`relatedID`),
            FOREIGN KEY (`relatedInstructorID1`) REFERENCES `instructor` (`instructorID`) ON DELETE CASCADE,
            FOREIGN KEY (`relatedInstructorID2`) REFERENCES `instructor` (`instructorID`) ON DELETE CASCADE
        )
    '''

    if 'related_instructor' not in existing_tables:
        cursor.execute(related_instructor_query)

    cursor.close()
    connection.close()

def get_from_table(table_name):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    query = f'SELECT * FROM {table_name}'
    cursor.execute(query)
    
    results = cursor.fetchall()
    key_names = list(map(lambda x : x[0], cursor.description))
    keyed_results = list(map(lambda x : dict(zip(key_names, x)), results))
    json_string = json.dumps(keyed_results)

    cursor.close()
    connection.close()
    return json_string

def get_instructors():
    return get_from_table('instructor')

def get_courses():
    return get_from_table('course')

def get_assignments():
    return get_from_table('assignment')

def get_related_instructors():
    return get_from_table('related_instructor')

def insert_instructor(json):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    
    query = f'''
        INSERT INTO instructor
        VALUES(NULL, '{json['name']}')
    '''
    cursor.execute(query)
    connection.commit()
    new_primary_key = cursor.lastrowid

    cursor.close()
    connection.close()
    return new_primary_key

def insert_course(json):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    
    query = f'''
        INSERT INTO course
        VALUES(NULL, {json['courseNumber']}, '{json['description']}', {json['creditHours']})
    '''
    cursor.execute(query)
    connection.commit()
    new_primary_key = cursor.lastrowid

    cursor.close()
    connection.close()
    return new_primary_key

def insert_assignment(json):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    
    query = f'''
        INSERT INTO assignment
        VALUES(NULL, {json['instructorID']}, {json['courseID']}, '{json['semester']}')
    '''
    cursor.execute(query)
    connection.commit()
    new_primary_key = cursor.lastrowid

    cursor.close()
    connection.close()
    return new_primary_key

def insert_related_instructor(json):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    
    query = f'''
        INSERT INTO related_instructor
        VALUES(NULL, {json['relatedInstructorID1']}, {json['relatedInstructorID2']})
    '''
    cursor.execute(query)
    connection.commit()
    new_primary_key = cursor.lastrowid

    cursor.close()
    connection.close()
    return new_primary_key

def delete_instructor(instructor_id):
    connection = connection_pool.get_connection()
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
    connection.close()

    return json_result

def delete_course(course_id):
    connection = connection_pool.get_connection()
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
    connection.close()

    return json_result

def delete_assignment(assignment_id):
    connection = connection_pool.get_connection()
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
    connection.close()

    return json_result

def delete_related_instructor(related_id):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()

    select_query = f'SELECT * FROM related_instructor WHERE relatedID = {related_id} LIMIT 1'
    cursor.execute(select_query)
    result = cursor.fetchall()[0]
    key_names = list(map(lambda x : x[0], cursor.description))
    json_result = json.dumps(dict(zip(key_names, result)))

    delete_query = f'DELETE FROM related_instructor WHERE relatedID = {related_id}'
    cursor.execute(delete_query)
    connection.commit()

    cursor.close()
    connection.close()

    return json_result

def update_instructor(obj):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    
    update_query = f'''
        UPDATE instructor
        SET name = '{obj['name']}'
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
    connection.close()

    return json_result

def update_course(obj):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    
    update_query = f'''
        UPDATE course
        SET courseNumber = {obj['courseNumber']}, description = '{obj['description']}', creditHours = {obj['creditHours']}
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
    connection.close()

    return json_result

def update_assignment(obj):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()

    update_query = f'''
        UPDATE assignment
        SET instructorID = {obj['instructorID']}, courseID = {obj['courseID']}, semester = '{obj['semester']}'
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
    connection.close()

    return json_result

def update_related_instructor(obj):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()

    update_query = f'''
        UPDATE related_instructor
        SET relatedInstructorID1 = {obj['relatedInstructorID1']}, relatedInstructorID2 = {obj['relatedInstructorID2']}
        WHERE relatedID = {obj['relatedID']}
    '''

    cursor.execute(update_query)
    connection.commit()

    select_query = f'SELECT * FROM related_instructor WHERE relatedID = ' + str(obj['relatedID']) + ' LIMIT 1'
    cursor.execute(select_query)
    result = cursor.fetchall()[0]
    key_names = list(map(lambda x : x[0], cursor.description))
    json_result = json.dumps(dict(zip(key_names, result)))

    cursor.close()
    connection.close()

    return json_result
