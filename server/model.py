import mysql.connector.pooling
import json
import spacy
import networkx as nx

course_to_umbrella = {}

course_to_umbrella["100"] = ["Unknown"]
course_to_umbrella["125"] = ["Unknown"]
course_to_umbrella["126"] = ["Unknown"]
course_to_umbrella["173"] = ["Unknown"]
course_to_umbrella["210"] = ["Unknown"]
course_to_umbrella["225"] = ["Unknown"]
course_to_umbrella["233"] = ["Unknown"]
course_to_umbrella["241"] = ["Unknown"]
course_to_umbrella["357"] = ["Unknown"]
course_to_umbrella["361"] = ["Unknown"]
course_to_umbrella["374"] = ["Unknown"]
course_to_umbrella["242"] = ["Unknown"]
course_to_umbrella["231"] = ["Unknown"]
course_to_umbrella["232"] = ["Unknown"]

course_to_umbrella["421"] = ["Software Foundations"]
course_to_umbrella["422"] = ["Software Foundations"]
course_to_umbrella["426"] = ["Software Foundations", "Machines"]
course_to_umbrella["427"] = ["Software Foundations"]
course_to_umbrella["428"] = ["Software Foundations"]
course_to_umbrella["429"] = ["Software Foundations"]
course_to_umbrella["476"] = ["Software Foundations", "Algorithms and Models of Computation"]
course_to_umbrella["477"] = ["Software Foundations", "Algorithms and Models of Computation"]
course_to_umbrella["492"] = ["Software Foundations"]
course_to_umbrella["493"] = ["Software Foundations"]
course_to_umbrella["494"] = ["Software Foundations"]
course_to_umbrella["498"] = ["Software Foundations", "Algorithms and Models of Computation", "Intelligence and Big Data", "Human and Social Impact", "Media", "Scientific, Parallel, and High Performance Computing", "Distributed Systems, Networking, and Security", "Machines"]
course_to_umbrella["522"] = ["Software Foundations"]
course_to_umbrella["524"] = ["Software Foundations", "Distributed Systems, Networking, and Security"]
course_to_umbrella["526"] = ["Software Foundations", "Machines"]
course_to_umbrella["527"] = ["Software Foundations"]
course_to_umbrella["528"] = ["Software Foundations"]
course_to_umbrella["576"] = ["Software Foundations", "Algorithms and Models of Computation", "Intelligence and Big Data"]
course_to_umbrella["598"] = ["Software Foundations", "Algorithms and Models of Computation", "Intelligence and Big Data", "Media", "Machines"]

course_to_umbrella["413"] = ["Algorithms and Models of Computation"]
course_to_umbrella["473"] = ["Algorithms and Models of Computation"]
course_to_umbrella["475"] = ["Algorithms and Models of Computation"]
course_to_umbrella["481"] = ["Algorithms and Models of Computation"]
course_to_umbrella["482"] = ["Algorithms and Models of Computation", "Scientific, Parallel, and High Performance Computing"]
course_to_umbrella["571"] = ["Algorithms and Models of Computation"]
course_to_umbrella["572"] = ["Algorithms and Models of Computation"]
course_to_umbrella["573"] = ["Algorithms and Models of Computation"]
course_to_umbrella["574"] = ["Algorithms and Models of Computation"]
course_to_umbrella["575"] = ["Algorithms and Models of Computation"]
course_to_umbrella["579"] = ["Algorithms and Models of Computation"]
course_to_umbrella["583"] = ["Algorithms and Models of Computation"]
course_to_umbrella["584"] = ["Algorithms and Models of Computation", "Machines"]

course_to_umbrella["410"] = ["Intelligence and Big Data"]
course_to_umbrella["411"] = ["Intelligence and Big Data"]
course_to_umbrella["412"] = ["Intelligence and Big Data"]
course_to_umbrella["414"] = ["Intelligence and Big Data", "Media"]
course_to_umbrella["440"] = ["Intelligence and Big Data"]
course_to_umbrella["443"] = ["Intelligence and Big Data"]
course_to_umbrella["445"] = ["Intelligence and Big Data", "Media"]
course_to_umbrella["446"] = ["Intelligence and Big Data"]
course_to_umbrella["447"] = ["Intelligence and Big Data"]
course_to_umbrella["466"] = ["Intelligence and Big Data", "Scientific, Parallel, and High Performance Computing"]
course_to_umbrella["467"] = ["Intelligence and Big Data", "Human and Social Impact", "Media"]
course_to_umbrella["510"] = ["Intelligence and Big Data"]
course_to_umbrella["511"] = ["Intelligence and Big Data"]
course_to_umbrella["512"] = ["Intelligence and Big Data"]
course_to_umbrella["543"] = ["Intelligence and Big Data"]
course_to_umbrella["544"] = ["Intelligence and Big Data"]
course_to_umbrella["546"] = ["Intelligence and Big Data"]
course_to_umbrella["548"] = ["Intelligence and Big Data"]
course_to_umbrella["566"] = ["Intelligence and Big Data"]

course_to_umbrella["460"] = ["Human and Social Impact", "Distributed Systems, Networking, and Security"]
course_to_umbrella["461"] = ["Human and Social Impact", "Distributed Systems, Networking, and Security"]
course_to_umbrella["463"] = ["Human and Social Impact", "Distributed Systems, Networking, and Security"]
course_to_umbrella["465"] = ["Human and Social Impact", "Media"]
course_to_umbrella["468"] = ["Human and Social Impact", "Media"]
course_to_umbrella["563"] = ["Human and Social Impact", "Distributed Systems, Networking, and Security"]
course_to_umbrella["565"] = ["Human and Social Impact", "Media"]

course_to_umbrella["418"] = ["Media"]
course_to_umbrella["419"] = ["Media", "Scientific, Parallel, and High Performance Computing"]
course_to_umbrella["519"] = ["Media", "Scientific, Parallel, and High Performance Computing"]

course_to_umbrella["450"] = ["Scientific, Parallel, and High Performance Computing"]
course_to_umbrella["457"] = ["Scientific, Parallel, and High Performance Computing"]
course_to_umbrella["483"] = ["Scientific, Parallel, and High Performance Computing", "Distributed Systems, Networking, and Security"]
course_to_umbrella["484"] = ["Scientific, Parallel, and High Performance Computing", "Distributed Systems, Networking, and Security", "Machines"]
course_to_umbrella["553"] = ["Scientific, Parallel, and High Performance Computing"]
course_to_umbrella["555"] = ["Scientific, Parallel, and High Performance Computing"]
course_to_umbrella["556"] = ["Scientific, Parallel, and High Performance Computing"]
course_to_umbrella["558"] = ["Scientific, Parallel, and High Performance Computing"]

course_to_umbrella["423"] = ["Distributed Systems, Networking, and Security", "Machines"]
course_to_umbrella["424"] = ["Distributed Systems, Networking, and Security", "Machines"]
course_to_umbrella["425"] = ["Distributed Systems, Networking, and Security"]
course_to_umbrella["431"] = ["Distributed Systems, Networking, and Security", "Machines"]
course_to_umbrella["436"] = ["Distributed Systems, Networking, and Security"]
course_to_umbrella["438"] = ["Distributed Systems, Networking, and Security"]
course_to_umbrella["439"] = ["Distributed Systems, Networking, and Security"]
course_to_umbrella["523"] = ["Distributed Systems, Networking, and Security", "Machines"]
course_to_umbrella["525"] = ["Distributed Systems, Networking, and Security"]
course_to_umbrella["538"] = ["Distributed Systems, Networking, and Security"]

course_to_umbrella["433"] = ["Machines"]
course_to_umbrella["533"] = ["Machines"]
course_to_umbrella["536"] = ["Machines"]
course_to_umbrella["541"] = ["Machines"]


def check_same_umbrella(c1, c2):
    if c1 not in course_to_umbrella or c2 not in course_to_umbrella:
        return False
    if course_to_umbrella[c1] and course_to_umbrella[c2]:
        for t1 in course_to_umbrella[c1]:
            for t2 in course_to_umbrella[c2]:
                if t1 == t2:
                    return True
        return False
    else:
        return False


# recommendation part
connection_pool = mysql.connector.pooling.MySQLConnectionPool(user='root', host='localhost', pool_name="pool", database='teaching_assignments')
prereq_dict = {}

def update_prereq():
    global prereq_dict
    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    query = """
                SELECT * FROM course
            """
    cursor.execute(query)
    for item in cursor.fetchall():
        course = item[1]
        description = item[2]
        prereq_idx = description.find("Prerequisite")

        if prereq_idx == -1:
            continue

        prereq_and_after = description[prereq_idx:]

        first_period_idx = prereq_and_after.find(".")
        prereqs = prereq_and_after[:first_period_idx]

        prereqs = prereqs.replace(" ", "")

        for idx in range(len(prereqs) - 1):
            temp = ""
            temp += prereqs[idx] + prereqs[idx + 1]

            if temp == "CS":
                prereq = prereqs[(idx + 2):(idx + 5)]
                if prereq.isnumeric():
                    if course in prereq_dict:
                        if prereq not in prereq_dict[course]:
                            prereq_dict[course].append(prereq)
                    else:
                        prereq_list = []
                        prereq_list.append(prereq)
                        prereq_dict[course] = prereq_list

    cursor.close()
    connection.close()

def compute_similarities():
    update_prereq()

    connection = connection_pool.get_connection()
    cursor = connection.cursor()
    query = """
        SELECT courseID, courseNumber, description
        FROM course
    """
    cursor.execute(query)

    results = cursor.fetchall()
    connection.close()
    cursor.close()

    nlp = spacy.load("en_core_web_lg")
    nlp_arr = []
    for i in range(len(results)):
        nlp_arr.append(nlp(results[i][2]))


    similarities = []
    for i in range(len(results)):
        course1 = results[i]
        for j in range(i + 1, len(results)):
            course2 = results[j]
            
            # if different course number
            if course1[1] != course2[1] and course2[1] in prereq_dict:
                prereq = prereq_dict[course2[1]]
            else:
                prereq = []

            is_umbrella = check_same_umbrella(str(course1[1]), str(course2[1]))

            # check similarity of course descriptions
            sim_score = nlp_arr[i].similarity(nlp_arr[j])

            if str(course1[1]) in prereq:
                # course 1 is a preqreq of course2
                if is_umbrella:
                    score = (1/3) * sim_score + (2/3)
                else:
                    score = 0.5 * sim_score + (2/3)
            else:
                score = sim_score

            similarities.append((course1[0], course2[0], score))
    
    connection = connection_pool.get_connection()
    cursor = connection.cursor()

    similarities_string = ','.join(map(repr, similarities)) + ';'
    
    delete_query = '''
        DELETE FROM course_similarity;
    '''
    cursor.execute(delete_query)

    insert_query = f'''
        INSERT INTO course_similarity VALUE {similarities_string}
    '''
    cursor.execute(insert_query)

    connection.commit()
    cursor.close()
    connection.close()

def create_graph(connection):
    graph = nx.DiGraph()
    # creating edges between instructors and courses they've taught
    cursor = connection.cursor()
    instructor_name_query = """
        SELECT name, instructorID
        FROM instructor
    """
    cursor.execute(instructor_name_query)

    instructors = list(set(i for i in cursor.fetchall()))

    cursor.close()

    cursor = connection.cursor()
    query = '''
        SELECT instructorID, c.courseNumber
        FROM assignment
        NATURAL JOIN
        course c
    '''
    cursor.execute(query)
    assignments = list(set(i for i in cursor.fetchall()))
    cursor.close()

    assignments_dict = {}
    for x in assignments:
        if x[0] in assignments_dict:
            assignments_dict[x[0]].append(x[1])
        else:
            assignments_dict[x[0]] = [x[1]]

    # edges between instructors and courses they've taught
    for i in range(len(instructors)):
        if instructors[i][1] not in assignments_dict.keys():
            continue
        taught_courses = assignments_dict[instructors[i][1]]
        for j in range(len(taught_courses)):
            graph.add_edge(f'i{instructors[i][1]}', f'c{taught_courses[j]}', weight=0)

    # creating edges between related courses
    cursor = connection.cursor()

    course_name_query = """
        SELECT *
        FROM course_similarity
    """

    cursor.execute(course_name_query)
    courses = list(set(i for i in cursor.fetchall()))

    course_id_number_query = '''
        SELECT courseID, courseNumber
        FROM course
    '''
    cursor.execute(course_id_number_query)
    course_id_numbers = list(set(i for i in cursor.fetchall()))

    course_id_to_num = {}
    for i in range(len(course_id_numbers)):
        course_id_to_num[course_id_numbers[i][0]] = course_id_numbers[i][1]

    cursor.close()

    for i in range(len(courses)):
        if graph.has_edge(f'c{courses[i][0]}', f'c{courses[i][1]}'):
            continue
        course0_num = course_id_to_num[courses[i][0]]
        course1_num = course_id_to_num[courses[i][1]]

        graph.add_edge(f'c{course0_num}', f'c{course1_num}', weight=1 / courses[i][2])
        graph.add_edge(f'c{course1_num}', f'c{course0_num}', weight=1 / courses[i][2])

    # creating edges between related instructors
    cursor = connection.cursor()

    related_instructor_query = """
        SELECT *
        FROM related_instructor
    """

    cursor.execute(related_instructor_query)
    related_instructors = list(set(i for i in cursor.fetchall()))

    cursor.close()

    for i in range(len(related_instructors)):
        if graph.has_edge(f'i{related_instructors[i][1]}', f'i{related_instructors[i][2]}'):
            current_weight = graph[f'i{related_instructors[i][1]}'][f'i{related_instructors[i][2]}']['weight']
            new_weight = current_weight * (4.0 / current_weight) / (4.0 / current_weight + 1)
            graph[f'i{related_instructors[i][1]}'][f'i{related_instructors[i][2]}']['weight'] = new_weight
            graph[f'i{related_instructors[i][2]}'][f'i{related_instructors[i][1]}']['weight'] = new_weight
        else:
            graph.add_edge(f'i{related_instructors[i][1]}', f'i{related_instructors[i][2]}', weight=4)
            graph.add_edge(f'i{related_instructors[i][2]}', f'i{related_instructors[i][1]}', weight=4)

    return graph

def best_courses(instructor_id):
    connection = connection_pool.get_connection()
    cursor = connection.cursor()

    graph = create_graph(connection)
    paths = nx.single_source_dijkstra(graph, f'i{instructor_id}')[0]

    best_ten_courses = [int(key[1:]) for key in paths.keys() if key[0] == 'c' and paths[key] != 0][:10]
    
    select_query = f'SELECT * FROM course WHERE courseNumber IN {repr(tuple(best_ten_courses))}'
    
    cursor.execute(select_query)
    results = cursor.fetchall()
    key_names = list(map(lambda x : x[0], cursor.description))
    keyed_results = list(map(lambda x : dict(zip(key_names, x)), results))

    ordered_keyed_results = []
    for i in range(len(best_ten_courses)):
        for j in range(len(keyed_results)):
            if keyed_results[j]["courseNumber"] == best_ten_courses[i]:
                ordered_keyed_results.append(keyed_results[j])
        
    json_string = json.dumps(ordered_keyed_results)

    cursor.close()
    connection.close()

    return json_string

