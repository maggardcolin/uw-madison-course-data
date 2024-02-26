# UW Madison Course Data

## What's included
- Course data for 187 subjects, including codes, titles, credits, and descriptions
- Additional fields related to requisites, designations, last semester taught, and repeatability

## How I made the dataset
- Selenium web scraping
- Parsing into JSON format using Python's json library

## Sample Data
*GitHub does not allow display of files this large (current dataset is 116772 lines long), so please download to see the full data.*\
"COMPUTER SCIENCES (COMP SCI)",\
&nbsp;&nbsp;&nbsp;&nbsp;[\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"course-code": "COMP SCI/L I S&nbsp;&nbsp;102",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"course-title": "INTRODUCTION TO COMPUTING",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"credits": "3",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"description": "Provides a broad overview of computing at an introductory level, including topics such as security, robotics, and artificial intelligence. Increases understanding of how computers work and how algorithms solve problems. Design and implement creative applications in an introductory coding environment. Provides a broad overview of computing and algorithms without an emphasis on programming.",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"mortarboard": true,\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Requisites:": "MATH 96 or placement into MATH 141. MATH 118 does not fulfill the prerequisite. Not open to students with credit for COMP SCI 300 or 320",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Course Designation:": "Gen Ed - Quantitative Reasoning Part A\nBreadth - Natural Science\nLevel - Elementary\nL&S Credit - Counts as Liberal Arts and Science credit in L&S",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Repeatable for Credit:": "No",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Last Taught:": "Spring 2024"\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"course-code": "COMP SCI 200",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"course-title": "PROGRAMMING I",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"credits": "3",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"description": "Learn the process of incrementally developing small (200-500 lines) programs along with the fundamental Computer Science topics. These topics include: problem abstraction and decomposition, the edit-compile-run cycle, using variables of primitive and more complex data types, conditional and loop-based flow control, basic testing and debugging techniques, how to define and call functions (methods), and IO processing techniques. Also teaches and reinforces good programming practices including the use of a consistent style, and meaningful documentation. Intended for students who have no prior programming experience.",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"mortarboard": true,\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Requisites:": "Satisfied Quantitative Reasoning (QR) A requirement or declared in the Capstone Certificate in Computer Sciences for Professionals",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Course Designation:": "Gen Ed - Quantitative Reasoning Part B\nBreadth - Natural Science\nLevel - Elementary\nL&S Credit - Counts as Liberal Arts and Science credit in L&S"\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"course-code": "COMP SCI 220",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"course-title": "DATA SCIENCE PROGRAMMING I",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"credits": "4",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"description": "Introduction to Data Science programming using Python. No previous programming experience required. Emphasis on analyzing real datasets in a variety of forms and visual communication.",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"mortarboard": true,\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Requisites:": "Satisfied Quantitative Reasoning (QR) A requirement or declared in the Professional Capstone Program in Computer Sciences. Not open to students with credit for COMP SCI 301.",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Course Designation:": "Gen Ed - Quantitative Reasoning Part B\nBreadth - Natural Science\nLevel - Elementary\nL&S Credit - Counts as Liberal Arts and Science credit in L&S",\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp

### Data sourced from https://guide.wisc.edu/courses/
