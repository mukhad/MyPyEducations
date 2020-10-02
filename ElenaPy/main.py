import csv
import datetime as dt

# import pandas as pd
# df = pd.read_csv('elena_12_17_out.csv')
# print(df)

sy_in = [0*i for i in range(6)]
sy_out = [0*i for i in range(6)]

sum_out = 0
eout = list()
with open('elena_12_17_out.csv', "r") as f:
    sr = csv.reader(f, delimiter=',')
    for row in sr:
        eout.append(row)
        # print(' ** '.join(row))
        d = dt.datetime.strptime(row[0], "%d.%m.%Y")
        for i in range(len(sy_out)):
            if d.year == i + 2012:
                sy_out[i] += float(row[2])
        sum_out += float(row[2])


stead = [0*i for i in range(165)]
stead_sum = [0*i for i in range(165)]
sum_in = 0
skWt = 0
ein = list()
with open('elena_12_17_in.csv', "r") as f:
    sr = csv.reader(f, delimiter=',')
    for row in sr:

        try:
            n = int(row[2])
        except ValueError:
            i = 1
            while row[2][0:i].isdigit():
                i += 1
            n = float(row[2][0:i - 1])
            # print row[2] + "  ->  " + str(n)

        d = dt.datetime.strptime(row[0], "%d.%m.%Y")

        for i in range(len(sy_in)):
            if d.year == i + 2012:
                sy_in[i] += float(row[6])
        # print (row[0] + "  ->  " + row[2])
        sum_in += float(row[6])

        i = 0
        d0 = dt.datetime.strptime(eout[i][0], "%d.%m.%Y")
        while (d < d0):
            i += 1
            d0 = dt.datetime.strptime(eout[i][0], "%d.%m.%Y")
        kWt = float(row[6])/float(eout[i][3])


        if d.year == 2017:
            if(kWt > 0):
                stead[int(n)] += 1
            stead_sum[int(n)] += kWt # float(row[6])
            skWt += kWt

        row.append(kWt)
        row.append(eout[i][3])
        ein.append(row)


print ("Sum in: %10.2f   len: %d" % (sum_in,len(ein)))
print ("Sum out: %10.2f   len: %d" % (sum_out,len(eout)))
print ("Sum_in - Sum_out: %10.2f" % (sum_in - sum_out))

for i in range(len(sy_in)):
    r = sy_in[i] - sy_out[i]
    print ("%d   %10.2f    %10.2f  %10.2f  %10.2f pc" % (i + 2012, sy_in[i], sy_out[i], r, r/sy_in[i]*100))

print (ein[0:10])
print (eout[0])

opl = len(stead) - stead.count(0)
print ("max:  " + str(max(stead)) + "  cnt: "  + str(opl) )
print ("kWt:  " + str(max(stead_sum)) + "  cnt: "  + str(len(stead_sum) - stead_sum.count(0)) )
print ("skWt:   " + str(skWt))