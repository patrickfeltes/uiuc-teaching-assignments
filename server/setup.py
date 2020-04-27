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
    for x in arr:
        professors.add(x['instructor'])
        
        course_number = int(x['courseNumber'])
        if course_number not in courses:
            courses[course_number] = { "courseNumber": course_number,  "description": x['description'].replace("'", r"\'"), "creditHours": int(x['creditHrs'].split()[0]) }
            course_id = database.insert_course(courses[course_number])

            course_number_to_id[course_number] = course_id

    # insert profs
    name_to_id = {}
    for prof in professors:
        d = { "name": prof }
        name_to_id[prof] = database.insert_instructor(d)

    # insert assignments
    for x in arr:
        semester = x['term']
        prof_name = x['instructor']
        course_number = int(x['courseNumber'])

        prof_id = name_to_id[prof_name]
        course_id = course_number_to_id[course_number]

        obj = { "courseID": course_id, "instructorID": prof_id, "semester": semester, "calendarYear": int(x['calendarYear']) }
        database.insert_assignment(obj)

    # insert related instructors
    for course_number in courses.keys():
        course_id = course_number_to_id[course_number]

        ids = database.get_all_instructors_teaching_course(course_id)

        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                d = { "relatedInstructorID1": ids[i], "relatedInstructorID2": ids[j] }
                database.insert_related_instructor(d)

database.create_tables()
database.clear_all_tables()
insert_scraped_data()