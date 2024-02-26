# this scrapes uw madison's course catalog

# author: Colin Maggard

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

headless = True
if headless:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # to make sure it is allowed to run headless
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    # suppresses DevTools message
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options = chrome_options)
else:
    driver = webdriver.Chrome()

# this is called by main file
def findLinks():    

    print("Now finding links on the UW Madison course catalog page.")

    links = []

    driver.get(f"https://guide.wisc.edu/courses/")
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.visibility_of_element_located((By.ID, 'atozindex')))
        index = driver.find_element(By.ID, 'atozindex')
        subjects = index.find_elements(By.CSS_SELECTOR, 'ul li a')
        for subject in subjects:
            try:
                link = subject.get_attribute('href')
                links.append(link)
                #print(link)
            except Exception:
                pass
        return links
    except TimeoutException:
        print("Timeout while waiting for course catalog to load.")

def parseCoursesIntoJSON(link: str):

    courseInfoForGivenSubject = []

    driver.get(link)
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'page-title')))
        subjectName = driver.find_element(By.CLASS_NAME, 'page-title').text
        courseInfoForGivenSubject.append({'subject-name', subjectName})
        courses = driver.find_elements(By.CLASS_NAME, 'courseblock')
        print(f"Now parsing through courses in {subjectName}")
        for course in courses:
            try:
                courseCode = course.find_element(By.CLASS_NAME, 'courseblockcode').text
                #print(courseCode)



                # add info to list
                courseInfoForGivenSubject.append({'course-code': courseCode})
            except Exception:
                pass
        return courseInfoForGivenSubject
    except TimeoutException:
        print("Timeout while waiting for courses to load.")