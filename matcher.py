#compares the contents of skills.txt to jobs.csv to determine matching skills, missing skills, and a skill gap score
import csv

job_dict = dict()
skills_list = []
job_match_dict = dict()


#read from jobs.csv and add job : skills to job_dict
with open('jobs.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        job_dict[row['company']] = (row['title'], row['skills'].lower().split(";"))

#print(f"job dictionary: {job_dict}")

#add contents of skills.txt to a skills list
with open('skills.txt', 'r') as file:
    for line in file:
        skills_list.append(line.lower().rstrip('\n'))
#print(f"your skills: {skills_list}")


#loop through job_dict to check for a job with matching skills when compared to skills_list
for company in job_dict:
    matching_skills = []
    for skill in skills_list:
        #print(f"has skill: {skill} need skill: {job_dict[company]}")
        if skill.lower() in job_dict[company][1]:
            matching_skills.append(skill)
    job_match_dict[company] = (job_dict[company][0], matching_skills)

#print(job_match_dict)

#process output

for company in job_match_dict:
    matching_skill_count = 0
    required_skill_count = len(job_dict[company][1])
    print(f"Company: {company}\n")
    print(f"Job: {job_match_dict[company][0]}\n")
    print("Matching skills:")
    for skill in job_match_dict[company][1]:
        print(skill)
        matching_skill_count += 1
    print("\nMissing skills:")
    for skill in job_dict[company][1]:
        if skill not in skills_list:
            print(skill)
    print("")

    print(f"matching count: {matching_skill_count}, required count: {required_skill_count}")

    if required_skill_count > 0:
        print(f"Skill gap score: {((matching_skill_count/required_skill_count) * 100):.1f}%")

