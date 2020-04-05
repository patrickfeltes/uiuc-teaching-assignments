import mysql.connector

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
            `instructorID` int(11) NOT NULL,
            `courseID` int(11) NOT NULL,
            PRIMARY KEY (`instructorID`, `courseID`),
            FOREIGN KEY (`instructorID`) REFERENCES `instructor` (`instructorID`),
            FOREIGN KEY (`courseID`) REFERENCES `course` (`courseID`)
        )
    '''

    if 'assignment' not in existing_tables:
        cursor.execute(assignment_table_query)
    
