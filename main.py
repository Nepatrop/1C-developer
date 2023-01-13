import csv
import operator

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
import datetime

years = list()
i = 0
result = {}

def analysis(line):
    global years
    date = datetime.datetime.strptime(line[6], '%Y-%m-%dT%H:%M:%S+%f')
    nDate = int(datetime.datetime.strftime(date, "%Y"))
    years.append(nDate)

def counter(years, result):
    for i in years:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

with open('vacancies_with_skills.csv', encoding="utf8") as csv_file:
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')

    for line in reader:
        if (line[0] == '1С Разработчик') or (line[0] == '1с Разработчик') or (line[0] == '1C Разработчик') or (line[0] == '1c Разработчик'):
            analysis(line)
        if (line[0] == '1С разработчик') or (line[0] == '1с разработчик') or (line[0] == '1C разработчик') or (line[0] == '1c разработчик'):
            analysis(line)
        if (line[0] == '1С') or (line[0] == '1с') or (line[0] == '1C') or (line[0] == '1c'):
            analysis(line)
        if (line[0] == '1 С') or (line[0] == '1 с') or (line[0] == '1 C') or (line[0] == '1 c'):
            analysis(line)
        if (line[0] == '1С программист') or (line[0] == '1с программист') or (line[0] == '1C Программист') or (line[0] == '1c Программист'):
            analysis(line)

counter(years, result)

graphs = pd.Series(result)
plt.title("Динамика количества вакансий по годам")
plt.bar(graphs.index, height=graphs)
plt.show()

print(years)
print(result)