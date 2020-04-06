# https://www.youtube.com/watch?v=sAuGH1Kto2I

import bs4 as bs
import urllib.request
import pandas as pd

schedules = urllib.request.urlopen('https://courses.illinois.edu/cisapp/explorer/schedule.xml').read()
soup = bs.BeautifulSoup(schedules, 'xml')

for url in soup.find_all('calendarYear'):
    calendarYear = urllib.request.urlopen(url['href']).read()
    calendarYearSoup = bs.BeautifulSoup(calendarYear, 'xml')
    for calendarYearUrl in calendarYearSoup.find_all('term'):
        term = urllib.request.urlopen(calendarYearUrl['href']).read()
        termSoup = bs.BeautifulSoup(term, 'xml')
        for subject in termSoup.find_all('subject'):
            if subject['id'] == 'CS':
                cs = urllib.request.urlopen(term_itr['href'])
                csSoup = bs.BeautifulSoup(cs, 'xml')
                for csCourseUrl in csSoup.find_all('course'):
                    csCourse = urllib.request.urlopen(csCourseUrl['href'])
                    csCourseSoup = bs.BeautifulSoup(csCourse, 'xml')
                    for csSectionUrl in csCourseSoup.find_all('section'):
                        csSection = urllib.request.urlopen(csSectionUrl['href'])
                        csSectionSoup = bs.BeautifulSoup(csSection, 'xml')