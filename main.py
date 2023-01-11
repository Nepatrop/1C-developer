import csv
import operator

count = 0

with open('vacancies_with_skills.csv', encoding="utf8") as csv_file:
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')

    for line in reader:
        if (line[0] == '1С Разработчик') or (line[0] == '1с Разработчик') or (line[0] == '1C Разработчик') or (line[0] == '1c Разработчик'):
            print(line)
            count += 1
        if (line[0] == '1С разработчик') or (line[0] == '1с разработчик') or (line[0] == '1C разработчик') or (line[0] == '1c разработчик'):
            print(line)
            count += 1
        if (line[0] == '1С') or (line[0] == '1с') or (line[0] == '1C') or (line[0] == '1c'):
            print(line)
            count += 1
        if (line[0] == '1 С') or (line[0] == '1 с') or (line[0] == '1 C') or (line[0] == '1 c'):
            print(line)
            count += 1
print(count)