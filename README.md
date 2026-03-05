# Job-Requirement-Web-Scrapper
A simple web scraper designed as part of a class programing exercise.

## Features:
- Data scrapping for a designated webpage
- Keyword analysis for skillset matching
- Computation of skill-gap score for job requirements and possesed skillsets

## Technologies used:
- Python

## Usage:
1. Add personal skill keywords to skills.txt
2. Run scraper.py
3. Run matcher.py
4. Run generator.py

## Project Structure:
- scraper.py:   Program file which scrapes a designated website (via url) for keywords related to job title, technical skills and company name. Found keywords are then added to jobs.csv in their respective categories.
- jobs.csv:     Data file used to store and organise keywords in colums: title,company,skills
- matcher.py:   Program file which analyzes and compares data within jobs.csv to keywords in skills.txt to determine the skill-gap score for a given job.
- skills.txt:   User data file to be filled with skillset keywords used by the user.
- generator.py: Generates an ATS friendly resume bullet with the format: action verb + task + impact

## License:
The programs and files within this project repository are for classroom use only

## Acknowledgments:
### Alex Bard:
- matcher.py
- repository and project management
### Jeffrey Fosgate:
- scraper.py
- generator.py

### Course:
University of Southern Maine, COS 470 Topics in Computer Science

