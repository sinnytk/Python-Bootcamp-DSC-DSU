import csv

# Name print diagonally
with open('txt.csv') as songFile:
    data = csv.reader(songFile,delimiter=',')
    count = 0
    for row in data:
        for i in row[0]:
            print(' '*count,i)
            count += 1
        count = 0

# Add Record
with open("txt.csv",mode='a') as class_record:
    fieldnames = ['name', 'roll number','age','marks']
    record_entry = csv.DictWriter(class_record,fieldnames=fieldnames)
    count = 0
    more = True
    
    while more:
        name = input('name:')
        roll_number = int(input('Roll Number:'))
        age = int(input('Age:'))
        marks = int(input('Marks'))

        record_entry.writerow({'name':name,'roll number':roll_number,'age':age,'marks':marks})
        
        ans = input('Do you want to add more')
        if ans == 'no':
            more = False

with open('txt.csv') as read_record:
    read_entry = csv.DictReader(read_record)
    
    print('Name | Roll numbers | Age | Marks')
    
    for row in read_entry:
        print(row['name'],' | ',row['roll number'],' | ',row['age'],' | ',row['marks'])