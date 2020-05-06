import database
import json

def insert_scraped_data():
    f = open('../scraped_data/web_scraped_data.json')
    arr = json.load(f)
    f.close()

    professors = set()
    courses = {}

    course_number_to_id = {}

    # select unique prof names and course numbers
    print("inserting courses...")
    for x in arr:
        professors.add(x['instructor'])
        
        course_number = int(x['courseNumber'])
        if course_number not in courses:
            courses[course_number] = { "courseNumber": course_number,  "description": x['description'].replace("'", r"\'"), "creditHours": int(x['creditHrs'].split()[0]) }
            course_id = database.insert_course(courses[course_number])

            course_number_to_id[course_number] = course_id
    print("inserting courses done")

    # insert profs
    print("inserting profs...")
    name_to_id = {}
    for prof in professors:
        d = { "name": prof }
        name_to_id[prof] = database.insert_instructor(d)
    print("inserting profs done")

    print("inserting profs assignments...")
    # insert assignments
    values_string = ''
    for x in arr:
        semester = x['term']
        prof_name = x['instructor']
        course_number = int(x['courseNumber'])

        prof_id = name_to_id[prof_name]
        course_id = course_number_to_id[course_number]
        year = int(x['calendarYear'])

        values_string += f'(NULL, {prof_id}, {course_id}, \"{semester}\", {year}),'
    
    values_string = values_string[:-1]
    insert_string = f'INSERT INTO assignment VALUES {values_string}'
    database.run_raw_query(insert_string)
    print("inserting profs assignments done")

    print("inserting related instructors...")
    # insert related instructors
    values_string = ''
    for course_number in courses.keys():
        course_id = course_number_to_id[course_number]

        ids = database.get_all_instructors_teaching_course(course_id)

        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                d = { "relatedInstructorID1": ids[i], "relatedInstructorID2": ids[j] }
                values_string += f'(NULL, {ids[i]}, {ids[j]}),'
                
    values_string = values_string[:-1]
    insert_string = f'INSERT INTO related_instructor VALUES {values_string}'
    database.run_raw_query(insert_string)

    print("inserting related instructors done")

database.create_tables()
print('created tables')
database.clear_all_tables()
print('cleared tables')
insert_scraped_data()
print('inserted data')