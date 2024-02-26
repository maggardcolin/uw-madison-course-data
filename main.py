from courseScraper import findLinks, parseCoursesIntoJSON, getSubjectName
from datetime import datetime
import json, os
os.system('cls')

debug = True

if debug:
    scrapeOption = 'y'
else:
    scrapeOption = input("Update course catalog? (y/n): ")
if scrapeOption == 'y':
    links = findLinks()
    output = []

    if debug:
        for i in range(1):
            link = links[i]
            subjectInfo = parseCoursesIntoJSON(link)
            subjectName = getSubjectName()
            output.append([subjectName] + [subjectInfo])
    else:
        for link in links:
            subjectInfo = parseCoursesIntoJSON(link)
            subjectName = getSubjectName()
            output.append([subjectName] + [subjectInfo])
    now = datetime.now()
    current_date_time = now.strftime("%m-%d-%Y")
    with open(f"./output/UWCourseCatalog_{current_date_time}.json", 'w') as file:
        json.dump(output, file, indent = 4)
else:
    print("Have a nice day!")