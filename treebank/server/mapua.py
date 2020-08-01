import re


COURSES = (
    'GENERAL CHEMISTRY FOR ENGINEERS LECTURE',
    'GENERAL CHEMISTRY FOR ENGINEERS LABORATORY',
    'COMPUTER ENGINEERING AS A DISCIPLINE',
    'PROGRAMMING LOGIC AND DESIGN',
    'PHYSICAL ACTIVITIES TOWARD HEALTH AND FITNESS ONE',
    'PHYSICAL ACTIVITIES TOWARD HEALTH AND FITNESS 1',
    'THE CONTEMPORARY WORLD',
    'CALCULUS 1',
    'CALCULUS ONE',
    'NATIONAL SERVICE TRAINING PROGRAM 1',
    'NATIONAL SERVICE TRAINING PROGRAM ONE',
    'OBJECT ORIENTED PROGRAMMING',
    'PHYSICAL ACTIVITIES TOWARD HEALTH AND FITNESS 2',
    'PHYSICAL ACTIVITIES TOWARD HEALTH AND FITNESS TWO',
    'UNDERSTANDING THE SELF',
    'SCIENCE',
    'CALCULUS 2',
    'CALCULUS TWO',
    'LINEAR ALGEBRA WITH COMPUTER APPLICATION',
    'NATIONAL SERVICE TRAINING PROGRAM 2',
    'NATIONAL SERVICE TRAINING PROGRAM TWO',
    'DISCRETE MATHEMATICS',
    'PHYSICAL ACTIVITIES TOWARD HEALTH AND FITNESS 3',
    'PHYSICAL ACTIVITIES TOWARD HEALTH AND FITNESS THREE',
    'READINGS IN PHILIPPINE HISTORY',
    'ART APPRECIATION',
    'CALCULUS 3',
    'CALCULUS THREE',
    'NATIONAL SERVICE TRAINING PROGRAM 3',
    'NATIONAL SERVICE TRAINING PROGRAM THREE',
    'PHYSICS FOR ENGINEERING',
    'PHYSICS FOR ENGINEERING - LABORATORY',
    'DATA STRUCTURES AND ALGORITHMS',
    'FUNDAMENTALS OF ELECTRICAL CIRCUITS',
    'FUNDAMENTALS OF ELECTRICAL CIRCUITS LABORATORY',
    'PHYSICAL ACTIVITIES TOWARD HEALTH AND FITNESS 4',
    'PHYSICAL ACTIVITIES TOWARD HEALTH AND FITNESS FOUR',
    'MATHEMATICS IN THE MODERN WORLD',
    'ETHICS',
    'DIFFERENTIAL EQUATIONS',
    'NATIONAL SERVICE TRAINING PROGRAM 4',
    'NATIONAL SERVICE TRAINING PROGRAM FOUR',
    'COMPUTER AIDED DRAFTING',
    'OPERATING SYSTEMS',
    'FUNDAMENTALS OF ELECTRONIC CIRCUITS',
    'FUNDAMENTALS OF ELECTRONIC CIRCUITS LABORATORY',
    'PURPOSIVE COMMUNICATION',
    'THE LIFE AND WORKS OF RIZAL',
    'INTRODUCTION TO BIOMEDICAL ENGINEERING',
    'LOGIC CIRCUITS AND DESIGN',
    'LOGIC CIRCUITS AND DESIGN LABORATORY',
    'FUNDAMENTALS OF MIXED SIGNALS AND SENSORS',
    'INTERNATIONAL STUDENT EXCHANGE EXPERIENCE',
    'FILIPINO SA EPEKTIBONG KOMUNIKASYONG PAMPROPESYUNAL',
    'ENGINEERING DATA ANALYSIS',
    'SOFTWARE DESIGN',
    'SOFTWARE DESIGN LABORATORY',
    'MICROPROCESSORS',
    'MICROPROCESSORS LABORATORY',
    'INTRODUCTION TO HDL',
    'APPLIED DATA SCIENCE',
    'MGA PILING BASA SA KONTEMPORARYONG PANITIKANG PILIPINO',
    'EMBEDDED SYSTEMS',
    'EMBEDDED SYSTEMS LABORATORY',
    'COMPUTER ENGINEERING DRAFTING AND DESIGN',
    'NUMERICAL METHODS',
    'METHODS OF RESEARCH FOR CPE',
    'DATA AND DIGITAL COMMUNICATIONS 1',
    'DATA AND DIGITAL COMMUNICATIONS ONE',
    'GREAT BOOKS',
    'COMPUTER ARCHITECTURE AND ORGANIZATION',
    'COMPUTER ARCHITECTURE AND ORGANIZATION LABORATORY',
    'DATA AND DIGITAL COMMUNICATIONS 2',
    'DATA AND DIGITAL COMMUNICATIONS TWO',
    'FEEDBACK AND CONTROL SYSTEMS',
    'CPE THESIS 1',
    'CPE THESIS ONE',
    'BASIC OCCUPATIONAL SAFETY AND HEALTH',
    'COMPUTER NETWORKS AND SECURITY 1',
    'COMPUTER NETWORKS AND SECURITY ONE',
    'CPE PRACTICE AND DESIGN 1',
    'CPE PRACTICE AND DESIGN ONE',
    'DIGITAL SIGNAL AND PROCESSING',
    'DIGITAL SIGNAL AND PROCESSING LABORATORY',
    'CPE THESIS 2',
    'CPE THESIS TWO',
    'COMPUTER NETWORKS AND SECURITY 2',
    'COMPUTER NETWORKS AND SECURITY TWO',
    'CPE PRACTICE AND DESIGN 2',
    'CPE PRACTICE AND DESIGN TWO',
    'CPE LAWS AND PROFESSIONAL PRACTICE',
    'CPE THESIS 3',
    'CPE THESIS THREE',
    'ENGINEERING ECONOMICS',
    'TECHNOPRENEURSHIP',
    'TECHNOPRENEURSHIP 101',
    'TECHNOPRENEURSHIP ONE ZERO ONE',
    'CPE PRACTICE AND DESIGN 3',
    'CPE PRACTICE AND DESIGN THREE',
    'EMERGING TECHNOLOGIES IN COMPUTER ENGINEERING',
    'PROJECT MANAGEMENT',
    'INTRODUCTION TO ARTIFICIAL INTELIGENCE',
    'SEMINARS AND FIELD TRIPS',
    'ON-THE-JOB TRAINING',
    'ON THE JOB TRAINING',
    'STUDENT GLOBAL EXPERIENCE'
)

ROOMS = (
    'MAPUA HVAC CENTER',
    'ME FABSHOP',
    'CCESC OFFICE',
    'CISCO LABORATORY',
    'SCHOOL OF GRADUATE STUDIES',
    'GRADUATE STUDIES LIBRARY',
    'CONFERENCE AREA',

    'NETWORK CONTROL CENTER',
    'CISCO OFFICE',
    'SMART WIRELESS LABORATORY',
    'CISCO LABORATORY',
    'CCESC TRAINING ROOM',

    'FLOUR COMPUTER LABORATORY',
    'EECE DEPARTMENT',

    'APPARATUS ROOM',
    'CHE-CHM STOCK ROOM',
    'CHE-CHM LABORATORY OFFICE',
    'PREP ROOM ',

    'MALE TOILET',
    'FEMALE TOILET'
)

COURSE_STR = 'Mapúa - Course'
COURSE_CODE_STR = 'Mapúa - Course Code'
NORTH_ROOM_STR = 'Mapúa - North Room'
NORTH_ROOM_1_STR = 'Mapúa - North Room, 1st Floor'
NORTH_ROOM_1_2_STR = 'Mapúa - North Room, 1st/2nd Floor'
NORTH_ROOM_2_STR = 'Mapúa - North Room, 2nd Floor'
NORTH_ROOM_3_STR = 'Mapúa - North Room, 3rd Floor'
NORTH_ROOM_4_STR = 'Mapúa - North Room, 4th Floor'

ENTITIES = {
    'GENERAL-CHEMISTRY-FOR-ENGINEERS-LECTURE': COURSE_STR,
    'GENERAL-CHEMISTRY-FOR-ENGINEERS-LABORATORY': COURSE_STR,
    'COMPUTER-ENGINEERING-AS-A-DISCIPLINE': COURSE_STR,
    'PROGRAMMING-LOGIC-AND-DESIGN': COURSE_STR,
    'PHYSICAL-ACTIVITIES-TOWARD-HEALTH-AND-FITNESS-1': COURSE_STR,
    'PHYSICAL-ACTIVITIES-TOWARD-HEALTH-AND-FITNESS-ONE': COURSE_STR,
    'THE-CONTEMPORARY-WORLD': COURSE_STR,
    'CALCULUS-1': COURSE_STR,
    'CALCULUS-ONE': COURSE_STR,
    'NATIONAL-SERVICE-TRAINING-PROGRAM-1': COURSE_STR,
    'NATIONAL-SERVICE-TRAINING-PROGRAM-ONE': COURSE_STR,
    'OBJECT-ORIENTED-PROGRAMMING': COURSE_STR,
    'PHYSICAL-ACTIVITIES-TOWARD-HEALTH-AND-FITNESS-2': COURSE_STR,
    'PHYSICAL-ACTIVITIES-TOWARD-HEALTH-AND-FITNESS-TWO': COURSE_STR,
    'UNDERSTANDING-THE-SELF': COURSE_STR,
    'SCIENCE': COURSE_STR,
    'CALCULUS-2': COURSE_STR,
    'CALCULUS-TWO': COURSE_STR,
    'LINEAR-ALGEBRA-WITH-COMPUTER-APPLICATION': COURSE_STR,
    'NATIONAL-SERVICE-TRAINING-PROGRAM-2': COURSE_STR,
    'NATIONAL-SERVICE-TRAINING-PROGRAM-TWO': COURSE_STR,
    'DISCRETE-MATHEMATICS': COURSE_STR,
    'PHYSICAL-ACTIVITIES-TOWARD-HEALTH-AND-FITNESS-3': COURSE_STR,
    'PHYSICAL-ACTIVITIES-TOWARD-HEALTH-AND-FITNESS-THREE': COURSE_STR,
    'READINGS-IN-PHILIPPINE-HISTORY': COURSE_STR,
    'ART-APPRECIATION': COURSE_STR,
    'CALCULUS-3': COURSE_STR,
    'CALCULUS-THREE': COURSE_STR,
    'NATIONAL-SERVICE-TRAINING-PROGRAM-3': COURSE_STR,
    'NATIONAL-SERVICE-TRAINING-PROGRAM-THREE': COURSE_STR,
    'PHYSICS-FOR-ENGINEERING': COURSE_STR,
    'PHYSICS-FOR-ENGINEERING---LABORATORY': COURSE_STR,
    'DATA-STRUCTURES-AND-ALGORITHMS': COURSE_STR,
    'FUNDAMENTALS-OF-ELECTRICAL-CIRCUITS': COURSE_STR,
    'FUNDAMENTALS-OF-ELECTRICAL-CIRCUITS-LABORATORY': COURSE_STR,
    'PHYSICAL-ACTIVITIES-TOWARD-HEALTH-AND-FITNESS-4': COURSE_STR,
    'PHYSICAL-ACTIVITIES-TOWARD-HEALTH-AND-FITNESS-FOUR': COURSE_STR,
    'MATHEMATICS-IN-THE-MODERN-WORLD': COURSE_STR,
    'ETHICS': COURSE_STR,
    'DIFFERENTIAL-EQUATIONS': COURSE_STR,
    'NATIONAL-SERVICE-TRAINING-PROGRAM-4': COURSE_STR,
    'NATIONAL-SERVICE-TRAINING-PROGRAM-FOUR': COURSE_STR,
    'COMPUTER-AIDED-DRAFTING': COURSE_STR,
    'OPERATING-SYSTEMS': COURSE_STR,
    'FUNDAMENTALS-OF-ELECTRONIC-CIRCUITS': COURSE_STR,
    'FUNDAMENTALS-OF-ELECTRONIC-CIRCUITS-LABORATORY': COURSE_STR,
    'PURPOSIVE-COMMUNICATION': COURSE_STR,
    'THE-LIFE-AND-WORKS-OF-RIZAL': COURSE_STR,
    'INTRODUCTION-TO-BIOMEDICAL-ENGINEERING': COURSE_STR,
    'LOGIC-CIRCUITS-AND-DESIGN': COURSE_STR,
    'LOGIC-CIRCUITS-AND-DESIGN-LABORATORY': COURSE_STR,
    'FUNDAMENTALS-OF-MIXED-SIGNALS-AND-SENSORS': COURSE_STR,
    'INTERNATIONAL-STUDENT-EXCHANGE-EXPERIENCE': COURSE_STR,
    'FILIPINO-SA-EPEKTIBONG-KOMUNIKASYONG-PAMPROPESYUNAL': COURSE_STR,
    'ENGINEERING-DATA-ANALYSIS': COURSE_STR,
    'SOFTWARE-DESIGN': COURSE_STR,
    'SOFTWARE-DESIGN-LABORATORY': COURSE_STR,
    'MICROPROCESSORS': COURSE_STR,
    'MICROPROCESSORS-LABORATORY': COURSE_STR,
    'INTRODUCTION-TO-HDL': COURSE_STR,
    'APPLIED-DATA-SCIENCE': COURSE_STR,
    'MGA-PILING-BASA-SA-KONTEMPORARYONG-PANITIKANG-PILIPINO': COURSE_STR,
    'EMBEDDED-SYSTEMS': COURSE_STR,
    'EMBEDDED-SYSTEMS-LABORATORY': COURSE_STR,
    'COMPUTER-ENGINEERING-DRAFTING-AND-DESIGN': COURSE_STR,
    'NUMERICAL-METHODS': COURSE_STR,
    'METHODS-OF-RESEARCH-FOR-CPE': COURSE_STR,
    'DATA-AND-DIGITAL-COMMUNICATIONS-1': COURSE_STR,
    'DATA-AND-DIGITAL-COMMUNICATIONS-ONE': COURSE_STR,
    'GREAT-BOOKS': COURSE_STR,
    'COMPUTER-ARCHITECTURE-AND-ORGANIZATION': COURSE_STR,
    'COMPUTER-ARCHITECTURE-AND-ORGANIZATION-LABORATORY': COURSE_STR,
    'DATA-AND-DIGITAL-COMMUNICATIONS-2': COURSE_STR,
    'DATA-AND-DIGITAL-COMMUNICATIONS-TWO': COURSE_STR,
    'FEEDBACK-AND-CONTROL-SYSTEMS': COURSE_STR,
    'CPE-THESIS-1': COURSE_STR,
    'CPE-THESIS-ONE': COURSE_STR,
    'BASIC-OCCUPATIONAL-SAFETY-AND-HEALTH': COURSE_STR,
    'COMPUTER-NETWORKS-AND-SECURITY-1': COURSE_STR,
    'COMPUTER-NETWORKS-AND-SECURITY-ONE': COURSE_STR,
    'CPE-PRACTICE-AND-DESIGN-1': COURSE_STR,
    'CPE-PRACTICE-AND-DESIGN-ONE': COURSE_STR,
    'DIGITAL-SIGNAL-AND-PROCESSING': COURSE_STR,
    'DIGITAL-SIGNAL-AND-PROCESSING-LABORATORY': COURSE_STR,
    'CPE-THESIS-TWO': COURSE_STR,
    'COMPUTER-NETWORKS-AND-SECURITY-2': COURSE_STR,
    'COMPUTER-NETWORKS-AND-SECURITY-TWO': COURSE_STR,
    'CPE-PRACTICE-AND-DESIGN-2': COURSE_STR,
    'CPE-PRACTICE-AND-DESIGN-TWO': COURSE_STR,
    'CPE-LAWS-AND-PROFESSIONAL-PRACTICE': COURSE_STR,
    'CPE-THESIS-3': COURSE_STR,
    'CPE-THESIS-THREE': COURSE_STR,
    'ENGINEERING-ECONOMICS': COURSE_STR,
    'TECHNOPRENEURSHIP': COURSE_STR,
    'TECHNOPRENEURSHIP-101': COURSE_STR,
    'TECHNOPRENEURSHIP-ONE-ZERO-ONE': COURSE_STR,
    'CPE-PRACTICE-AND-DESIGN-3': COURSE_STR,
    'CPE-PRACTICE-AND-DESIGN-THREE': COURSE_STR,
    'EMERGING-TECHNOLOGIES-IN-COMPUTER-ENGINEERING': COURSE_STR,
    'PROJECT-MANAGEMENT': COURSE_STR,
    'INTRODUCTION-TO-ARTIFICIAL-INTELIGENCE': COURSE_STR,
    'SEMINARS-AND-FIELD-TRIPS': COURSE_STR,
    'ON-THE-JOB-TRAINING': COURSE_STR,
    'STUDENT-GLOBAL-EXPERIENCE': COURSE_STR,

    'CM011': COURSE_CODE_STR,
    'CM011L': COURSE_CODE_STR,
    'CPE101': COURSE_CODE_STR,
    'CPE102L': COURSE_CODE_STR,
    'FW01': COURSE_CODE_STR,
    'GED105': COURSE_CODE_STR,
    'MATH146': COURSE_CODE_STR,
    'NSTP100': COURSE_CODE_STR,
    'CPE103L': COURSE_CODE_STR,
    'FW02': COURSE_CODE_STR,
    'GED101': COURSE_CODE_STR,
    'GED104': COURSE_CODE_STR,
    'MATH147': COURSE_CODE_STR,
    'MATH149': COURSE_CODE_STR,
    'NSTP200': COURSE_CODE_STR,
    'CPE111': COURSE_CODE_STR,
    'FW03': COURSE_CODE_STR,
    'GED103': COURSE_CODE_STR,
    'GED108': COURSE_CODE_STR,
    'MATH148': COURSE_CODE_STR,
    'NSTP300': COURSE_CODE_STR,
    'PHYS101': COURSE_CODE_STR,
    'PHYS101L': COURSE_CODE_STR,
    'CPE104L': COURSE_CODE_STR,
    'EE101-1': COURSE_CODE_STR,
    'EE101-1L ': COURSE_CODE_STR,
    'FW04': COURSE_CODE_STR,
    'GED102': COURSE_CODE_STR,
    'GED107': COURSE_CODE_STR,
    'MATH156': COURSE_CODE_STR,
    'NSTP400': COURSE_CODE_STR,
    'CAD30L': COURSE_CODE_STR,
    'CPE105': COURSE_CODE_STR,
    'ECEA101-1': COURSE_CODE_STR,
    'ECEA101-1L': COURSE_CODE_STR,
    'GED106': COURSE_CODE_STR,
    'RZL110': COURSE_CODE_STR,
    'BE101P': COURSE_CODE_STR,
    'CPE107': COURSE_CODE_STR,
    'CPE107L': COURSE_CODE_STR,
    'CPE112': COURSE_CODE_STR,
    'CPE128': COURSE_CODE_STR,
    'FIL100': COURSE_CODE_STR,
    'MATH142-2': COURSE_CODE_STR,
    'CPE106': COURSE_CODE_STR,
    'CPE106L': COURSE_CODE_STR,
    'CPE108': COURSE_CODE_STR,
    'CPE108L': COURSE_CODE_STR,
    'CPE114L': COURSE_CODE_STR,
    'DS100-1': COURSE_CODE_STR,
    'FIL110': COURSE_CODE_STR,
    'CPE109': COURSE_CODE_STR,
    'CPE109L': COURSE_CODE_STR,
    'CPE113L': COURSE_CODE_STR,
    'CPE115': COURSE_CODE_STR,
    'CPE117': COURSE_CODE_STR,
    'CPE118-1L': COURSE_CODE_STR,
    'LIT110': COURSE_CODE_STR,
    'CPE110': COURSE_CODE_STR,
    'CPE110L': COURSE_CODE_STR,
    'CPE118-2L': COURSE_CODE_STR,
    'CPE121': COURSE_CODE_STR,
    'CPE200-1L': COURSE_CODE_STR,
    'CPE116': COURSE_CODE_STR,
    'CPE119-1L': COURSE_CODE_STR,
    'CPE120-1D': COURSE_CODE_STR,
    'CPE122': COURSE_CODE_STR,
    'CPE122L': COURSE_CODE_STR,
    'CPE200-2L': COURSE_CODE_STR,
    'CPE119-2L': COURSE_CODE_STR,
    'CPE120-2D': COURSE_CODE_STR,
    'CPE123': COURSE_CODE_STR,
    'CPE200-3L': COURSE_CODE_STR,
    'EEA109': COURSE_CODE_STR,
    'IE103': COURSE_CODE_STR,
    'CPE120-3D': COURSE_CODE_STR,
    'CPE124': COURSE_CODE_STR,
    'CPE125': COURSE_CODE_STR,
    'CPE126': COURSE_CODE_STR,
    'CPE127F': COURSE_CODE_STR,
    'CPE199R': COURSE_CODE_STR,
    'SGE100': COURSE_CODE_STR,

    'MAPUA-HVAC-CENTER': NORTH_ROOM_1_STR,
    'ME-FABSHOP': NORTH_ROOM_1_STR,
    'CCESC-OFFICE': NORTH_ROOM_1_STR,
    'SCHOOL-OF-GRADUATE-STUDIES': NORTH_ROOM_1_STR,
    'GRADUATE-STUDIES-LIBRARY': NORTH_ROOM_1_STR,
    'CONFERENCE-AREA': NORTH_ROOM_1_STR,
    'GAIC': NORTH_ROOM_1_STR,
    'N101': NORTH_ROOM_1_STR,
    'N100': NORTH_ROOM_1_STR,
    'N103': NORTH_ROOM_1_STR,
    'N102': NORTH_ROOM_1_STR,
    'N103-B': NORTH_ROOM_1_STR,
    'N106': NORTH_ROOM_1_STR,
    'N105-A': NORTH_ROOM_1_STR,
    'N105': NORTH_ROOM_1_STR,
    'N110': NORTH_ROOM_1_STR,
    'N109': NORTH_ROOM_1_STR,
    'N109A': NORTH_ROOM_1_STR,
    'N112': NORTH_ROOM_1_STR,
    'N114': NORTH_ROOM_1_STR,

    'CISCO-LABORATORY': NORTH_ROOM_1_2_STR,

    'NETWORK-CONTROL-CENTER': NORTH_ROOM_2_STR,
    'CISCO-OFFICE': NORTH_ROOM_2_STR,
    'SMART-WIRELESS-LABORATORY': NORTH_ROOM_2_STR,
    'CCESC-TRAINING-ROOM': NORTH_ROOM_2_STR,
    'N200-A': NORTH_ROOM_2_STR,
    'N200-B': NORTH_ROOM_2_STR,
    'N201': NORTH_ROOM_2_STR,
    'N202': NORTH_ROOM_2_STR,
    'N203': NORTH_ROOM_2_STR,
    'N205-A': NORTH_ROOM_2_STR,
    'N204': NORTH_ROOM_2_STR,
    'N206': NORTH_ROOM_2_STR,
    'N205-B': NORTH_ROOM_2_STR,
    'N207': NORTH_ROOM_2_STR,
    'N209': NORTH_ROOM_2_STR,
    'N210': NORTH_ROOM_2_STR,
    'DESE': NORTH_ROOM_2_STR,
    'N211': NORTH_ROOM_2_STR,
    'N208': NORTH_ROOM_2_STR,

    'FLOUR-COMPUTER-LABORATORY': NORTH_ROOM_3_STR,
    'EECE-DEPARTMENT': NORTH_ROOM_3_STR,
    'N307': NORTH_ROOM_3_STR,
    'N304': NORTH_ROOM_3_STR,
    'N306': NORTH_ROOM_3_STR,
    'N308-A': NORTH_ROOM_3_STR,
    'N308-B': NORTH_ROOM_3_STR,
    'N309': NORTH_ROOM_3_STR,
    'N311': NORTH_ROOM_3_STR,
    'N310': NORTH_ROOM_3_STR,
    'N312': NORTH_ROOM_3_STR,
    'N313': NORTH_ROOM_3_STR,
    'N304': NORTH_ROOM_3_STR,
    'N307': NORTH_ROOM_3_STR,
    'N305': NORTH_ROOM_3_STR,
    'N303': NORTH_ROOM_3_STR,
    'N301': NORTH_ROOM_3_STR,

    'APPARATUS-ROOM': NORTH_ROOM_4_STR,
    'CHE-CHM-STOCK-ROOM': NORTH_ROOM_4_STR,
    'CHE-CHM-LABORATORY-OFFICE': NORTH_ROOM_4_STR,
    'PREP-ROOM-': NORTH_ROOM_4_STR,
    'N407-B': NORTH_ROOM_4_STR,
    'N407-A': NORTH_ROOM_4_STR,
    'N406': NORTH_ROOM_4_STR,
    'N405': NORTH_ROOM_4_STR,
    'N404': NORTH_ROOM_4_STR,
    'N403': NORTH_ROOM_4_STR,
    'N402': NORTH_ROOM_4_STR,
    'SR1': NORTH_ROOM_4_STR,
    'SR2': NORTH_ROOM_4_STR,
    'N401': NORTH_ROOM_4_STR,
    'N400': NORTH_ROOM_4_STR,
    'FAMIT': NORTH_ROOM_4_STR,

    'MALE-TOILET': NORTH_ROOM_STR,
    'FEMALE-TOILET': NORTH_ROOM_STR
}


def preprocess(sentence: str) -> str:
    for phrase in COURSES + ROOMS:
        pattern = re.compile(phrase, re.IGNORECASE)
        results = re.findall(pattern, sentence)

        if results:
            transform = [(result, re.sub(' ', '-', result))
                         for result in results]

            for old, new in transform:
                sentence = re.sub(old, new, sentence)

    return sentence


def tag_entities(tagged_words: tuple) -> list:
    ne_tags = list()
    for word, tag in tagged_words:
        entity = ENTITIES.get(word.upper())

        if entity:
            ne_tags.append((entity, word))

    return ne_tags
