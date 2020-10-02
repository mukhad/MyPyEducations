import csv
import datetime as dt

import matplotlib.pyplot as plt

sum_all = 0
sum_el = 0
sum_el_cnt = 0
conversation_errors = 0
conversation_errors_list = list()

pay_type = set()

sum_by_month = [0*i for i in range(12)]

with open('elena_2018_in.csv', "r") as f:
    sr = csv.reader(f, delimiter=';')

    for row in sr:

        try:
            n = int(row[2])
        except ValueError:
            try:
                i = 1
                while row[2][0:i].isdigit():
                   i += 1
                n = float(row[2][0:i - 1])
                # print row[2] + "  ->  " + str(n)
            except ValueError:
                n=0
                conversation_errors+=1
                conversation_errors_list.append(row)
        if n == 69:
            print(row)


        d = dt.datetime.strptime(row[0], "%d.%m.%y")

        row_val = float(row[5])
        sum_all += row_val
        pay_type.add(row[6])
        if row[6] == "возмещение электроэнергии":
            if row_val > 2000:
                sum_el_cnt += 1
                sum_el += row_val
            sum_by_month[d.month-1] += row_val



print ("sum all: {0}".format(sum_all))
print ("sum el: {0}    cnt: {1}".format(sum_el,sum_el_cnt))

print("===============")
print("conversation_errors: {0}".format(conversation_errors))
for i in conversation_errors_list:
    print(i)

print("===============")
print(sum_by_month)
s=0
for i in sum_by_month:
    s+=i
print("------------\n{0}".format(s))

with open("sum_by_month_2018.txt", "w") as file:
    for i in sum_by_month:
        print(i, file=file)

plt.plot(sum_by_month)
plt.show()