import csv
with open('brain_stroke.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
print("hello world")