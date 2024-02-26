# UW Madison Course Data

## What's included
- Course data for 187 subjects, including codes, titles, credits, and descriptions
- Additional fields related to requisites, designations, last semester taught, and repeatability

## How I made the dataset
- Selenium web scraping
- Parsing into JSON format using Python's json library

## Sample Data
*GitHub does not allow display of files this large (current dataset is 116772 lines long), so please download to see the full data.*\
\
{
"course-code": "COMP SCI/E C E  252",\
"course-title": "INTRODUCTION TO COMPUTER ENGINEERING",\
"credits": "3",\
"description": "Logic components built with transistors, rudimentary Boolean algebra, basic combinational logic design, basic synchronous sequential logic design, basic computer organization and design, introductory machine- and assembly-language programming.",\
"mortarboard": false,\
"Requisites:": "None",\
"Course Designation:": "Level - Elementary\nL&S Credit - Counts as Liberal Arts and Science credit in L&S",\
"Repeatable for Credit:": "No",\
"Last Taught:": "Spring 2024"},

### Data sourced from https://guide.wisc.edu/courses/
