# https://www.youtube.com/watch?v=sAuGH1Kto2I
# https://stackoverflow.com/questions/19522990/python-catch-exception-and-continue-try-block
# https://stackoverflow.com/questions/50079650/write-data-from-multiple-site-to-json-file-beautifulsoup

import bs4 as bs
import urllib.request
import pandas as pd
import json

schedules = urllib.request.urlopen('https://courses.illinois.edu/cisapp/explorer/schedule.xml').read()
soup = bs.BeautifulSoup(schedules, 'xml')

data = []

for url in soup.find_all('calendarYear'):
    calendarYear = urllib.request.urlopen(url['href']).read()
    calendarYearSoup = bs.BeautifulSoup(calendarYear, 'xml')
    for calendarYearUrl in calendarYearSoup.find_all('term'):
        term = urllib.request.urlopen(calendarYearUrl['href']).read()
        termSoup = bs.BeautifulSoup(term, 'xml')
        for subject in termSoup.find_all('subject'):
            if subject['id'] == 'CS':
                cs = urllib.request.urlopen(subject['href'])
                csSoup = bs.BeautifulSoup(cs, 'xml')
                for csCourseUrl in csSoup.find_all('course'):
                    try:
                        csCourse = urllib.request.urlopen(csCourseUrl['href'])
                        csCourseSoup = bs.BeautifulSoup(csCourse, 'xml')
                        csCourseDescription = csCourseSoup.description
                        csCourseCreditHrs = csCourseSoup.creditHours
                        for csSectionUrl in csCourseSoup.find_all('section'):
                            item = {}
                            csSection = urllib.request.urlopen(csSectionUrl['href'])
                            csSectionSoup = bs.BeautifulSoup(csSection, 'xml')
                            
                            item['calendarYear'] = csSectionSoup.calendarYear
                            item['term'] = csSectionSoup.term
                            item['courseNumber'] = csSectionSoup.course['id']
                            item['instructor'] = csSectionSoup.meeting.instructor
                            item['description'] = csCourseDescription
                            item['creditHrs'] = csCourseCreditHrs 
                            data.append(item)
                    except:
                        print("ERROR")
                        continue
                        
with open("web_scraped_data.json", "w") as wJson:
    json.dump(data, wJson, ensure_ascii=False)
