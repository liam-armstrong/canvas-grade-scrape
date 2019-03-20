from bs4 import BeautifulSoup
import re

html = BeautifulSoup(open('grades.html'), "lxml")
file = open('out.csv', 'w')

for assignment in html.find_all('tr', {'class' : 'student_assignment'}):
    title = assignment.find('th', {'class' : 'title'})
    link = title.a['href']
    title = assignment.find('th', {'class' : 'title'}).get_text().strip().replace("\n", " ")

    score = assignment.find('span', {'class' : 'grade'}).get_text()
    if score:
        score = re.search(r'(\d)+', score)
        if score != None:
            score = score.group(0)
        else:
            break

    possible = assignment.find('td', {'class' : 'possible'}).get_text()
    if possible:
        possible = re.search(r'(\d)+', possible)
        if possible != None:
            possible = possible.group(0)
        else:
            break
        
    file.write(title + ", " + link + " ," + score + "," + possible + "," + "\n") 
        

