import csv
import operator
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import datetime
import numpy as np

years = list()
i = 0
vacanciesYears = {}
salaryYears = {}
salaryCity = {}
cities = list()
vacanciesCities = {}

def analysisYears(line):
    global years
    date = datetime.datetime.strptime(line[6], '%Y-%m-%dT%H:%M:%S+%f')
    nDate = int(datetime.datetime.strftime(date, "%Y"))
    years.append(nDate)

def counterDict(years, result):
    for i in years:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

def get_LKey(d):
    keys = list(d.keys())
    if len(keys) == 0:
        return 0
    else:
        return keys[-1]

def analysisSalary(line):
    global salaryYears
    date = datetime.datetime.strptime(line[6], '%Y-%m-%dT%H:%M:%S+%f')
    nDate = int(datetime.datetime.strftime(date, "%Y"))

    if line[2] == '':
        minSalary = 0
    else:
        minSalary = float(line[2])
        if line[4] == 'USD':
            minSalary = minSalary * 65
    if line[3] == '':
        maxSalary = 0
    else:
        maxSalary = float(line[3])
        if line[4] == 'USD':
            maxSalary = maxSalary * 65

    if minSalary == 0:
        average = maxSalary
    else:
        if maxSalary == 0:
            average = minSalary
        else:
            average = (minSalary + maxSalary) / 2

    early = get_LKey(salaryYears)

    if nDate == early:
        n = salaryYears.pop(nDate)
        if average == 0:
            average = n
        else:
            average = (average + n) / 2
        salaryYears[nDate] = average
    else:
        salaryYears[nDate] = average

def analysisCitySal(line):
    global salaryCity
    city = line[5]
    if line[2] == '':
        minSalary = 0
    else:
        minSalary = float(line[2])
        if line[4] == 'USD':
            minSalary = minSalary * 65
    if line[3] == '':
        maxSalary = 0
    else:
        maxSalary = float(line[3])
        if line[4] == 'USD':
            maxSalary = maxSalary * 65

    if minSalary == 0:
        average = maxSalary
    else:
        if maxSalary == 0:
            average = minSalary
        else:
            average = (minSalary + maxSalary) / 2

    for search in salaryCity:
        if city == search:
            n = salaryCity.pop(city)
            if average == 0:
                average = n
                break
            else:
                average = (average + n) / 2
                break
    salaryCity[city] = average

def cityVacCount(line):
    global cities
    city = line[5]
    cities.append(city)


with open('vacancies_with_skills.csv', encoding="utf8") as csv_file:
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')

    for line in reader:
        if (line[0] == '1С Разработчик') or (line[0] == '1с Разработчик') or (line[0] == '1C Разработчик') or (line[0] == '1c Разработчик'):
            analysisYears(line)
            analysisSalary(line)
            analysisCitySal(line)
            cityVacCount(line)
        if (line[0] == '1С разработчик') or (line[0] == '1с разработчик') or (line[0] == '1C разработчик') or (line[0] == '1c разработчик'):
            analysisYears(line)
            analysisSalary(line)
            analysisCitySal(line)
            cityVacCount(line)
        if (line[0] == '1С') or (line[0] == '1с') or (line[0] == '1C') or (line[0] == '1c'):
            analysisYears(line)
            analysisSalary(line)
            analysisCitySal(line)
            cityVacCount(line)
        if (line[0] == '1 С') or (line[0] == '1 с') or (line[0] == '1 C') or (line[0] == '1 c'):
            analysisYears(line)
            analysisSalary(line)
            analysisCitySal(line)
            cityVacCount(line)
        if (line[0] == '1С программист') or (line[0] == '1с программист') or (line[0] == '1C Программист') or (line[0] == '1c Программист'):
            analysisYears(line)
            analysisSalary(line)
            analysisCitySal(line)
            cityVacCount(line)

counterDict(years, vacanciesYears)

graphsY = pd.Series(vacanciesYears)
plt.title("Динамика количества вакансий по годам")
plt.bar(graphsY.index, height=graphsY)
plt.xticks(np.arange(2004, max(graphsY.index), 1))
plt.show()

graphsS = pd.Series(salaryYears)
plt.title("Динамика уровня зарплат по годам (RUR)")
plt.bar(graphsS.index, height=graphsS)
plt.xticks(np.arange(2004, max(graphsS.index), 1))
plt.show()

ascendingF = {}
sorted_keys = sorted(salaryCity, key=salaryCity.get)
for i in sorted_keys:
    ascendingF[i] = salaryCity[i]
sortedSalaryCity = dict(reversed(list(ascendingF.items())))

graphsC = pd.Series(sortedSalaryCity)
plt.title("Средний уровень зарплат по городам (RUR)")
plt.bar(graphsC.index, height=graphsC)
plt.yticks(np.arange(0, max(graphsC), 25000))
plt.xticks(rotation=90)
plt.show()

counterDict(cities, vacanciesCities)
ascendingS = {}
sorted_keys = sorted(vacanciesCities, key=vacanciesCities.get)
for i in sorted_keys:
    ascendingS[i] = vacanciesCities[i]
sortedCitiesVac = dict(reversed(list(ascendingS.items())))

graphsV = pd.Series(sortedCitiesVac)
plt.title("Доля вакансий по городам")
plt.bar(graphsV.index, height=graphsV)
plt.yticks(np.arange(0, max(graphsV), 10))
plt.xticks(rotation=90)
plt.show()