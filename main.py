from datefinder import find_dates
from dateutil.parser import parse
from dateutil.rrule import rrule, MONTHLY


def find_date(elements):
    for element in elements:
        matches = list(find_dates(element))
        if matches:
            return matches[0].strftime("%m/%d/%Y")
    return None

def find_date_range(elements):
    for element in elements:
        try:
            start_date = None
            end_date = None
            for date in element.split("-"):
                date = parse(date, fuzzy=True)
                if not start_date:
                    start_date = date
                elif date > start_date:
                    end_date = date
            if end_date:
                return (start_date.strftime("%m/%d/%Y"), end_date.strftime("%m/%d/%Y"))
            else:
                return start_date.strftime("%m/%d/%Y")
        except ValueError:
            continue
    return None

#this is the bank of languages that we will use
languages = ['Python', 'JavaScript', 'Java', 'C#', 'C++', 'PHP', 'Ruby', 'Swift', 'Kotlin', 'Go', 'Ruby on Rails']

flags = {
    "flag1": True,
    "flag2": True,
    "flag3": True,
    "flag4": True,
    "flag5": True,
    "flag6": True,
    "flag7": True,
    "flag8": True,
    "flag9": True,
    "flag10": True,
    "flag11": True,
    "flag12": True,
    "flag13": True,
    "flag14": True,
    "flag15": True,
    "flag16": True,
    "flag17": True,
    "flag18": True,
    "flag19": True,
    "flag20": True,
}
#this is job description, extracting the keywords from the job description
#jobDescription = input("Enter the job description: ")
def find_keywords_in_string(keywords, string):
    found_keywords = []
    for keyword in keywords:
        if keyword in string:
            found_keywords.append(keyword)
    return found_keywords

resumeDict = {"name": " ", "Github": " ", "address": " ", "email": " ", "Phone": " ", "LinkedIn": " ", "Summary": " ", "Edcuation":" ", "Programming Languages":" ", 'Experience #1':" ", 'Experience #2':" ",'Experience #3':" ",'Experience #4':" ", 'Project #1':" ", 'Project #2':" ", 'Project #3':" ",'Project #4':" "}
def read_input(f):
    informationDict = {}
    #line = f.readline().rstrip()
    for line in f:
        line = line.rstrip()

        if flags["flag1"] == True:
            if "name".lower() in line.lower():
                substring = line.split(':')[1]
                resumeDict["name"]=substring
                #line = f.readline().rstrip()
                flags["flag1"] = False

        if flags["flag2"] == True:
            if "email".lower() in line.lower() or "email address".lower() in line.lower():
                substring = line.split(':')[1]
                resumeDict["email"]=substring
                #line = f.readline().rstrip()
                flags["flag2"] = False

        if flags["flag3"] == True:
            if "phone".lower() in line.lower() or "phone number".lower() in line.lower() or "cell number".lower() in line.lower() or "number".lower() in line.lower() or "cell".lower() in line.lower():
                substring = line.split(':')[1]
                resumeDict["Phone"]=substring
                #line = f.readline().rstrip()
                flags["flag3"] = False

        if flags["flag4"] == True:
            if "LinkedIn".lower() in line.lower():
                substring = line.split(':')[1]
                resumeDict["LinkedIn"]=substring
                #line = f.readline().rstrip()
                flags["flag4"] = False

        if flags["flag17"] == True:
            if "Github".lower() in line.lower():
                substring = line.split(':')[1]
                resumeDict["Github"]=substring
                #line = f.readline().rstrip()
                flags["flag17"] = False

        if flags["flag5"] == True:
            if "summary".lower() in line.lower() or "Objective".lower() in line.lower() or "purpose".lower() in line.lower() or "intent".lower() in line.lower() or "goal".lower() in line.lower() or "aim".lower() in line.lower():
                substring = line.split(':')[1]
                resumeDict["Summary"]=substring
                #line = f.readline().rstrip()
                flags["flag5"] = False

        if flags["flag6"] == True:
            if "education".lower() in line.lower():
                substring = line.split(':')[1]
                resumeDict["Edcuation"]=substring
                #line = f.readline().rstrip()
                flags["flag6"] = False

        if flags["flag7"] == True:
            if "programming languages".lower() in line.lower():
                substring = line.split(':')[1]
                resumeDict["Programming Languages"]=substring
                #line = f.readline().rstrip()
                flags["flag7"] = False

        if flags["flag8"] == True:
            if "Experience #1".lower() in line.lower() or "Experience#1".lower() in line.lower() or "Experience 1".lower() in line.lower() or "Work Experience #1".lower() in line.lower() or "Work Experience#1".lower() in line.lower() or "Work Experience 1".lower() in line.lower():
                listoflines = []
                while line:
                    if line !='':
                        line = f.readline().rstrip()
                        print(line)
                        listoflines.append(line)
                        #substring = line.split(':')[1]
                        resumeDict["Experience #1"]=listoflines
                        #line = f.readline().rstrip()
                        flags["flag8"] = False

        if flags["flag11"] == True:
            if "Experience #2".lower() in line.lower() or "Experience#2".lower() in line.lower() or "Experience 2".lower() in line.lower() or "Work Experience #2".lower() in line.lower() or "Work Experience#2".lower() in line.lower() or "Work Experience 2".lower() in line.lower():
                listoflines = []
                while line:
                    if line !='':
                        line = f.readline().rstrip()
                        listoflines.append(line)
                        #substring = line.split(':')[1]
                        resumeDict["Experience #2"]=listoflines
                        #line = f.readline().rstrip()
                        flags["flag11"] = False

        if flags["flag14"] == True:
            if "Experience #3".lower() in line.lower():
                listoflines = []
                while line:
                    if line !='':
                        line = f.readline().rstrip()
                        listoflines.append(line)
                        #substring = line.split(':')[1]
                        resumeDict["Experience #3"]=listoflines
                        #line = f.readline().rstrip()
                        flags["flag14"] = False

        if flags["flag15"] == True:
            if "Experience #4".lower() in line.lower() or "Experience#4".lower() in line.lower() or "Experience 4".lower() in line.lower() or "Work Experience #4".lower() in line.lower() or "Work Experience#4".lower() in line.lower() or "Work Experience 4".lower() in line.lower():
                listoflines = []
                while line:
                    if line !='':
                        line = f.readline().rstrip()
                        listoflines.append(line)
                        #substring = line.split(':')[1]
                        resumeDict["Experience #4"]=listoflines
                        #line = f.readline().rstrip()
                        flags["flag15"] = False

        if flags["flag9"] == True:
            if "Project #1".lower() in line.lower() or "Project#1".lower() in line.lower() or "Project 1".lower() in line.lower():
                listoflines = []
                while line:
                    if line !='':
                        line = f.readline().rstrip()
                        print(line)
                        listoflines.append(line)
                        #substring = line.split(':')[1]
                        resumeDict["Project #1"]=listoflines
                        #line = f.readline().rstrip()
                        flags["flag9"] = False

        if flags["flag10"] == True:
            if "Project #2".lower() in line.lower() or "Project#2".lower() in line.lower() or "Project 2".lower() in line.lower():
                listoflines = []
                while line:
                    if line !='':
                        line = f.readline().rstrip()
                        print(line)
                        listoflines.append(line)
                        #substring = line.split(':')[1]
                        resumeDict["Project #2"]=listoflines
                        #line = f.readline().rstrip()
                        flags["flag10"] = False

        if flags["flag13"] == True:
            if "Project #3".lower() in line.lower() or "Project#3".lower() in line.lower() or "Project 3".lower() in line.lower():
                print(True)
                listoflines = []
                while line:
                    if line !='':
                        line = f.readline().rstrip()
                        print(line)
                        listoflines.append(line)
                        #substring = line.split(':')[1]
                        resumeDict["Project #3"]=listoflines
                        #line = f.readline().rstrip()
                        flags["flag13"] = False

        if flags["flag16"] == True:
            if "Project #4".lower() in line.lower() or "Project#4".lower() in line.lower() or "Project 4".lower() in line.lower():
                listoflines = []
                while line:
                    if line !='':
                        line = f.readline().rstrip()
                        print(line)
                        listoflines.append(line)
                        #substring = line.split(':')[1]
                        resumeDict["Project #4"]=listoflines
                        #line = f.readline().rstrip()
                        flags["flag16"] = False

def print_dict(d):
    for key, value in d.items():
        print(key,':',value,)

experiences = open("experiences.txt",'r')
read_input(experiences)
print_dict(resumeDict)
print(resumeDict.keys())
#print("The list of languages you need for your resume is listed below: ")
#print(find_keywords_in_string(languages, jobDescription))
