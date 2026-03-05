# NAME: scraper.py
# AUTHOR: Jeffrey Fosgate
# DESCRIPTION: A simple web scraper for finding test listings. Currently only has support for one test website with three job listings.
# LAST MODIFIED: March 5, 2026

from bs4 import BeautifulSoup
import requests
import re
import csv
import os # For current-working-directory testing.

FIELD_NAMES = ["title","company","skills"]
CSV_DIR = "jobs.csv"
QUINLAN_TEST_SITE = "https://cs.usm.maine.edu/~james.quinlan/cos470s26/jobs/"
ZIPRECRUITER_REMOTE = "https://www.ziprecruiter.com/jobs-search?search=Computer+Science&location=Remote" # TODO: Develop support for ZipRecruiter using this URL.

test_site = requests.get(QUINLAN_TEST_SITE)
#zip_recruiter = requests.get(ZIPRECRUITER_REMOTE)

job_listings = []

# Web Scraping Test Site by James Quinlan

test_site_BS = BeautifulSoup(test_site.content, "html.parser")
test_site_joblistings = [joblisting_tag.get_text("href") for joblisting_tag in test_site_BS.find_all("a",{"href":re.compile(r"job")})]

for listing in test_site_joblistings:
    job_listing_site = BeautifulSoup(requests.get(QUINLAN_TEST_SITE+listing).content, "html.parser")
    job_title, job_company, job_skills = job_listing_site.find("h1").contents[0], job_listing_site.find("div",{"class":"company"}).contents[0], ""
    for skill in [skill.contents[0] for skill in job_listing_site.find_all("li")]:
        job_skills += skill+";"
    job_skills = job_skills.strip(';')

    job_listing = {"title":job_title, "company":job_company, "skills":job_skills}
    job_listings.append(job_listing)

# TODO: Insert code for ZipRecruiter web scraping here!

# Final compilation of all found job listings.

with open(__file__+'\\..\\jobs.csv',mode='w+') as jobs_file:
    csvwriter = csv.DictWriter(jobs_file, fieldnames=FIELD_NAMES)
    csvwriter.writeheader()
    for listing in job_listings:
        csvwriter.writerow(listing)