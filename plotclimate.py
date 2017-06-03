import matplotlib.pyplot as plt

import gzip
import csv

tempfile=gzip.open('data/temp-20170526.csv.gz','rb')
tempcsv = csv.reader(tempfile,delimiter=',')

print tempcsv.next()

tijd = []
bartemp = []
barpres = []
humidity = []

for row in tempcsv:
    tijd.append(int(row[0]))
    bartemp.append(float(row[1]))
    barpres.append(float(row[2]))
    humidity.append(float(row[3]))

fig,ax1 = plt.subplots()
ax1.plot(tijd,bartemp)
ax1.set_xlabel('time[s]')
ax1.set_ylabel('Temperature[C]')

ax2 = ax1.twinx()
ax2.plot(tijd,barpres,'r')
ax2.set_ylabel('Pressure[Pa]')

plt.show()

plt.clf()

fig,ax1 = plt.subplots()
ax1.plot(tijd,bartemp)
ax1.set_xlabel('time[s]')
ax1.set_ylabel('Temperature[C]')

ax2 = ax1.twinx()
ax2.plot(tijd,humidity,'r')
ax2.set_ylabel('Humidity[%]')
plt.show()