from bs4 import BeautifulSoup
import re

html = BeautifulSoup(open('grades.html'), "lxml")
total_earned = 0
total_possible = 0

grades_counted = 0
possible_counted = 0

total_assignments = 0

for assignment in html.find_all('tr', {'class' : 'student_assignment'}):
    score = assignment.find('span', {'class' : 'grade'}).get_text()
    if score:
        score = re.search(r'(\d)+', score)
        if score != None:
            score = score.group(0)
            print(score)
            total_earned += float(score)
            grades_counted += 1
        else:
            break

    possible = assignment.find('td', {'class' : 'possible'}).get_text()
    if possible:
        possible = re.search(r'(\d)+', possible)
        if possible != None:
            possible = possible.group(0)
            print(possible)
            total_possible += float(possible)
            possible_counted += 1

    total_assignments += 1

print("total earned: " + str(total_earned))
print("total possible: " + str(total_possible))
print("total average: " + str((round((total_earned/total_possible), 3)) * 100) + "%")

print("\ngrades counted: " + str(grades_counted))
print("possible counted: " + str(possible_counted))
print("total assignments counted: " + str(total_assignments))
