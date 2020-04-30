import json

def prerequisite_finder():
    f = open("web_scraped_data.json")
    arr = json.load(f)
    f.close()

    # dicitonary
    prereq_dict = {}

    for item in arr:
        course = item['courseNumber']
        description = item['description']
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

    return prereq_dict