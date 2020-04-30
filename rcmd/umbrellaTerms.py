umbrella_to_course = {}

sf_list = [421, 422, 426, 427, 428, 429, 476, 477, 492, 493, 494, 498, 522, 524, 526, 527, 528, 576, 598]
umbrella_to_course["Software Foundations"] = sf_list

amc_list = [413, 473, 475, 476, 477, 481, 482, 498, 571, 572, 573, 574, 575, 576, 579, 583, 584, 598]
umbrella_to_course["Algorithms and Models of Computation"] = amc_list

ibd_list = [410, 411, 412, 414, 440, 443, 445, 446, 447, 466, 467, 498, 510, 511, 512, 543, 544, 546, 548, 566, 576, 598]
umbrella_to_course["Intelligence and Big Data"] = ibd_list

hsi_list = [460, 461, 463, 465, 467, 468, 498, 563, 565]
umbrella_to_course["Human and Social Impact"] = hsi_list

media_list = [414, 418, 419, 445, 465, 467, 468, 498, 519, 565, 598]
umbrella_to_course["Media"] = media_list

sphpc_list = [419, 450, 457, 466, 482, 483, 484, 498, 519, 554, 555, 556, 558]
umbrella_to_course["Scientific, Parallel, and High Performance Computing"] = sphpc_list

dsns_list = [423, 424, 425, 431, 436, 438, 439, 460, 461, 463, 483, 484, 498, 523, 524, 525, 538, 563]
umbrella_to_course["Distributed Systems, Networking, and Security"] = dsns_list

mach_list = [423, 424, 426, 431, 433, 484, 498, 523, 526, 533, 536, 541, 584, 598]
umbrella_to_course["Machines"] = mach_list

unknown_list = [100, 125, 126, 173, 210, 225, 233, 241, 357, 361, 374, 242, 231, 232]
umbrella_to_course["Unknown"] = unknown_list

# ############################################################################################

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