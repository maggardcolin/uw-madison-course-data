from courseScraper import findLinks, parseCoursesIntoJSON
from datetime import datetime
import json

scrapeOption = input("Update course catalog? (y/n): ")
if scrapeOption == 'y':
    subjects = findLinks()
    output = []
    for subject in subjects:
        courses = parseCoursesIntoJSON()
        output.append(courses)
        pass
    # get current time and add to json file, this will be deleted later and is intermediary
    now = datetime.now()
    current_date_time = now.strftime("%m-%d-%Y")
    with open(f"category_links_{current_date_time}.json", 'w') as file:
        json.dump(courses, file, indent = 4)
else:
    print("Have a nice day!")