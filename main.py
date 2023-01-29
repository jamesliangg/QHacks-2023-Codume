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


resumeDict = {"name": None, "address": None, "email": None, "Phone": None, "LinkedIn": None, "Summary": None, "Edcuation":None, "Programming Languages":None}
print(resumeDict)
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

        elif flags["flag2"] == True:
            if "email".lower() in line.lower():
                substring = line.split(':')[1]
                resumeDict["email"]=substring
                #line = f.readline().rstrip()
                flags["flag2"] = False

        elif flags["flag3"] == True:
            if "phone".lower() in line.lower():
                substring = line.split(':')[1]
                resumeDict["Phone"]=substring
                #line = f.readline().rstrip()
                flags["flag3"] = False

        elif flags["flag4"] == True:
            if "LinkedIn".lower() in line.lower():
                substring = line.split(':')[1]
                resumeDict["LinkedIn"]=substring
                #line = f.readline().rstrip()
                flags["flag4"] = False

        elif flags["flag5"] == True:
            if "summary".lower() in line.lower():
                substring = line.split(':')[1]
                resumeDict["Summary"]=substring
                #line = f.readline().rstrip()
                flags["flag5"] = False

        elif flags["flag6"] == True:
            if "education".lower() in line.lower():
                substring = line.split(':')[1]
                resumeDict["Edcuation"]=substring
                #line = f.readline().rstrip()
                flags["flag6"] = False

        elif flags["flag7"] == True:
            if "programming languages".lower() in line.lower():
                substring = line.split(':')[1]
                resumeDict["Programming Languages"]=substring
                #line = f.readline().rstrip()
                flags["flag7"] = False

        elif flags["flag8"] == True:
            if "Experience #1".lower() in line.lower():
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

        elif flags["flag9"] == True:
            if "Experience #2".lower() in line.lower():
                listoflines = []
                while line:
                    if line !='':
                        line = f.readline().rstrip()
                        print(line)
                        listoflines.append(line)
                        #substring = line.split(':')[1]
                        resumeDict["Experience #2"]=listoflines
                        #line = f.readline().rstrip()
                        flags["flag8"] = False




experiences = open("experiences.txt",'r')
read_input(experiences)
print (resumeDict)
#print("The list of languages you need for your resume is listed below: ")
#print(find_keywords_in_string(languages, jobDescription))
