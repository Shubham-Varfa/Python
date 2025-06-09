import csv
with open('/home/mypc/Documents/Python/student.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['RollNo', "Name", "Age", "Grade"])
    writer.writerow([101, "Lisa", 20, "A+"])
    writer.writerow([102, "Monty", 23, "B"])
    writer.writerow([103, "peir", 22, "C"])

with open ('/home/mypc/Documents/Python/student.csv', 'r') as file:
    reader = csv.reader(file)

    for r in reader:
        print(r)