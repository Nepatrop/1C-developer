import csv
import operator

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import datetime

years = list()
i = 0
resultY = {}
salary = {}

def analysisYears(line):
    global years
    date = datetime.datetime.strptime(line[6], '%Y-%m-%dT%H:%M:%S+%f')
    nDate = int(datetime.datetime.strftime(date, "%Y"))
    years.append(nDate)

def counterYears(years, resultY):
    for i in years:
        if i in resultY:
            resultY[i] += 1
        else:
            resultY[i] = 1

def get_LKey(d):
    keys = list(d.keys())
    if len(keys) == 0:
        return 0
    else:
        return keys[-1]

def analysisSalary(line):
    global salary
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

    early = get_LKey(salary)

    if nDate == early:
        n = salary.pop(nDate)
        if average == 0:
            average = n
        else:
            average = (average + n) / 2
        salary[nDate] = average
    else:
        salary[nDate] = average

def analysisCitySal(line):



with open('vacancies_with_skills.csv', encoding="utf8") as csv_file:
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')

    for line in reader:
        if (line[0] == '1С Разработчик') or (line[0] == '1с Разработчик') or (line[0] == '1C Разработчик') or (line[0] == '1c Разработчик'):
            analysisYears(line)
            analysisSalary(line)
        if (line[0] == '1С разработчик') or (line[0] == '1с разработчик') or (line[0] == '1C разработчик') or (line[0] == '1c разработчик'):
            analysisYears(line)
            analysisSalary(line)
        if (line[0] == '1С') or (line[0] == '1с') or (line[0] == '1C') or (line[0] == '1c'):
            analysisYears(line)
            analysisSalary(line)
        if (line[0] == '1 С') or (line[0] == '1 с') or (line[0] == '1 C') or (line[0] == '1 c'):
            analysisYears(line)
            analysisSalary(line)
        if (line[0] == '1С программист') or (line[0] == '1с программист') or (line[0] == '1C Программист') or (line[0] == '1c Программист'):
            analysisYears(line)
            analysisSalary(line)

counterYears(years, resultY)

graphsY = pd.Series(resultY)
plt.title("Динамика количества вакансий по годам")
plt.bar(graphsY.index, height=graphsY)
print(resultY)
plt.show()

graphsS = pd.Series(salary)
plt.title("Динамика уровня зарплат по годам (RUR)")
plt.bar(graphsS.index, height=graphsS)
print(salary)
plt.show()