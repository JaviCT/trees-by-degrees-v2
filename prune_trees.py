import csv

l1=37.784825
l2=-122.490692
l3=37.812361
l4=-122.418938
for line in open("./data/sanfrancisco.csv"):
    csv_row = line.split(',')
    if csv_row[15]=='':
        continue
    cord1=float(csv_row[15])
    cord2=float(csv_row[16])
    print(cord1,cord2)
    if cord1> l1  and cord1 < l3 and cord2> l2  and cord2 < l4:

        with open('out2.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            spamwriter.writerow([
            cord1,
            cord2
            ])
