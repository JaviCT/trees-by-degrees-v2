import csv


l1=-0.113125
l2=51.498084
l3=-0.043430
l4=51.519612
for line in open("../data/london.csv"):
    try:
        csv_row = line.split(',')
        cord1=float(csv_row[8])
        cord2=float(csv_row[9])
        if cord1> l1  and cord1 < l3 and cord2> l2  and cord2 < l4:
            print(csv_row[8], csv_row[9])

            with open('out.csv', 'a') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',')
                spamwriter.writerow([
                cord1,
                cord2
                ])
    except:
        print('oops')
