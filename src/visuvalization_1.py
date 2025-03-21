import csv
import datetime
import pandas as pd
from itertools import filterfalse
from statistics import median, mean, mode
from math import isnan
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits import mplot3d
import sys
# Path to your CSV file
csv_file = 'Bicycle_Thefts_Open_Data.csv'

# Initialize an empty list to hold the dictionaries
csv_data = []
bicycle_price = []
occ_report_time_diff = []

# Bargraph variables
bike_type_all_records = []
status_all_records = []
neighbourhood_all_records = []

# Box plot
price_neighbourhood = []

# Histogram variables
occ_month_all_records = ['January',
                         'February',
                         'March',
                         'April',
                         'May',
                         'June',
                         'July',
                         'August',
                         'September',
                         'October',
                         'November',
                         'December',
                         ]
occ_hour_all_records = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                        10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

# scatter plot
bike_cost = []
bike_speed = []
bike_type = []
bike_color = []

# Heat Map

heat_map_all_records = [[], [], [], [], [], [], []]


# Open and read the CSV file
with open('Bicycle_Thefts_Open_Data.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    # Convert each row into a dictionary and append it to the list
    for row in reader:
        csv_data.append(dict(row))
        bicycle_price.append(row['BIKE_COST'])
        # Graph 1
        bike_type_all_records.append(row['BIKE_TYPE'])
        status_all_records.append(row['STATUS'])
        neighbourhood_all_records.append(int(row['HOOD_140']))

        # Graph 2
        # bike price same as analytics
        occ_month_all_records.append(row['OCC_MONTH'])
        occ_hour_all_records.append(row['OCC_HOUR'])

        # graph 3
        price_neighbourhood.append({'neighbourhood': int(
            row['HOOD_140']), 'bike_cost': float(row['BIKE_COST']) if row['BIKE_COST'] else 0})

        # graph 4
        bike_cost.append(float(row['BIKE_COST']) if row['BIKE_COST'] else 0)
        bike_speed.append(float(row['BIKE_SPEED']) if row['BIKE_SPEED'] else 0)
        bike_type.append(row['BIKE_TYPE_CODE'])
        bike_color.append(row['BIKE_COLOUR_HEX'])

# 'BIKE_COST', 'OCC_HOUR', 'OCC_MONTH', 'BIKE_SPEED', 'HOOD_140', 'LONG_WGS84', 'LAT_WGS84'
        # graph 5
        heat_map_all_records[0].append(
            float(row['BIKE_COST']) if row['BIKE_COST'] else 0)
        heat_map_all_records[1].append(float(row['OCC_HOUR']))
        heat_map_all_records[2].append(float(row['OCC_MONTH_CODE']))
        heat_map_all_records[3].append(
            float(row['BIKE_SPEED']) if row['BIKE_SPEED'] else 0)
        heat_map_all_records[4].append(int(row['HOOD_140']))
        heat_map_all_records[5].append(float(row['LONG_WGS84']))
        heat_map_all_records[6].append(float(row['LAT_WGS84']))

        # graph
        # datetime(year, month, day, hour, minute, second)
        a = datetime.datetime(int(row['OCC_YEAR']), 1, 1) + datetime.timedelta(
            days=int(row['OCC_DOY']) - 1, hours=int(row['OCC_HOUR']))
        b = datetime.datetime(int(row['REPORT_YEAR']), 1, 1) + datetime.timedelta(
            days=int(row['REPORT_DOY']) - 1, hours=int(row['REPORT_HOUR']))

        # returns a timedelta object
        c = b-a
        hours = c.total_seconds() / 3600
        if (hours < 50):
            occ_report_time_diff.append(hours)


# Analysis

bicycle_price = [j for j in [float(i) for i in bicycle_price if i] if j > 101]
bicycle_price = list(filterfalse(isnan, bicycle_price))
occ_report_time_diff = [float(i) for i in occ_report_time_diff if i]
occ_report_time_diff = list(filterfalse(isnan, occ_report_time_diff))
price_range = "[" + str(min(bicycle_price)) + "," + \
    str(max(bicycle_price)) + "]"
occ_range = "[" + str(min(occ_report_time_diff)) + "," + \
    str(max(occ_report_time_diff)) + "]"
d = {1: ["Mean", round(mean(bicycle_price), 3), round(mean(occ_report_time_diff), 3)],
     2: ["Median", median(bicycle_price), median(occ_report_time_diff)],
     3: ["Mode", mode(bicycle_price), "-"],
     10: ["Range", price_range, occ_range],
     5: ["Standard Deviation", round(np.std(bicycle_price), 3), "-"],
     }
print("{:<20} {:<15} {:<10} ".format('', 'Bike Price', 'Time Difference b/w'))
print("{:<20} {:<15} {:<10} ".format(
    '', '', 'Offence Occurence and Report time'))
print("-------------------------------------------------------")
for k, v in d.items():
    lang, perc, change = v
    print("{:<20} {:<15} {:<10} ".format(lang, perc, change))

# Visuvalization

# 1. Bar Graph
# 1.1 Number of Theft vs Bike Type
""" 
UN - Utility/Urban/Universal
TR - Touring
OT - Other
SC - Scooter/Single-Speed Commuter
EL - Electric
TA - Tandem
RE - Recumbent
RC - Racing
FO - Folding
TO - Track/Time Trial
RG - Rigid (no suspension)
BM - BMX (Bicycle Motocross)
MT - Mountain 
"""

bar1_data = dict((x, bike_type_all_records.count(x))
                 for x in set(bike_type_all_records))
bar1_bike_type = list(bar1_data.keys())
bar1_count = list(bar1_data.values())

fig = plt.figure(figsize=(10, 5))

plt.bar(bar1_bike_type, bar1_count, color='maroon',
        width=0.4)

plt.xlabel("Bike Type")
plt.ylabel("Count of Thefts")
plt.title("Theft Count vs Bike Type")
plt.show()

# 1.2 Number of Theft vs Status

bar2_data = dict((x, status_all_records.count(x))
                 for x in set(status_all_records))
bar2_status = list(bar2_data.keys())
bar2_count = list(bar2_data.values())

fig = plt.figure(figsize=(10, 5))

plt.bar(bar2_status, bar2_count, color='maroon',
        width=0.4)

plt.xlabel("Bicycle Theft Status (Recovered vs. Not Recovered)")
plt.ylabel("Count of Thefts")
plt.title("Theft Count vs Status")
plt.show()

# 1.3 Number of Theft vs Neighbourhood

bar3_data = dict((x, neighbourhood_all_records.count(x))
                 for x in set(neighbourhood_all_records))
bar3_neighbourhood = list(bar3_data.keys())
bar3_count = list(bar3_data.values())

fig = plt.figure(figsize=(10, 5))

plt.bar(bar3_neighbourhood, bar3_count, color='maroon',
        width=0.4)

plt.xlabel("Neighbourhood")
plt.ylabel("Count of Thefts")
plt.title("Number of Theft vs Neighbourhood")
plt.show()

# 2 Histogram
# 2.1 Theft count vs Bike Price
sns.histplot(bicycle_price, bins=30, kde=False,
             color='skyblue', edgecolor='black')

plt.xlabel('Price')
plt.ylabel('Count')
plt.title('Theft count vs Bike Price')

plt.show()


# 2.2 Theft Count vs Month
sns.histplot(occ_month_all_records, bins=30, kde=False,
             color='skyblue', edgecolor='black')

plt.xlabel('Month')
plt.ylabel('Count')
plt.title('Theft Count vs Month')

plt.show()


# 2.3 Theft Count vs Hour Of the Day

sns.histplot(occ_hour_all_records, bins=30, kde=False,
             color='skyblue', edgecolor='black')

plt.xlabel('Hour of the Day')
plt.ylabel('Count')
plt.title('Theft count vs Hour of the Day')

plt.show()

# 3

dist_neighbourhood = list(set(neighbourhood_all_records))

box_plot_data = [[], [], [], [], [], [], [], [], [], []]

for i in price_neighbourhood:
    n = i['neighbourhood'] / 14
    box_plot_data[int(n)-1].append(i['bike_cost'])


colors = ['SkyBlue', 'Coral', 'Goldenrod', 'Violet', 'Teal',
          'Tomato', 'SlateGray', 'LimeGreen', 'Orchid', 'Crimson']

fig, ax = plt.subplots()
ax.set_ylabel('Price of Bicycle')
ax.set_xlabel(
    'Neighbourhood Sections (every section contains 14 neighbourhood structures defined by Toronto gov.)')

bplot = ax.boxplot(box_plot_data,
                   patch_artist=True,  # fill with color
                   # will be used to label x-ticks
                   tick_labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# fill with colors
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

plt.show()

# 4 Scatter Plot
N = 100
z = bike_cost[:N]
x = bike_speed[:N]
y = bike_type[:N]
c = bike_color[:N]

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c=c, alpha=1)
plt.title("simple 3D scatter plot")

plt.show()

# 5 Heat Map


def get_pearson_correlation(i, j):
    corr = 0

    x_values = heat_map_all_records[i]
    y_values = heat_map_all_records[j]
    n = len(x_values)

    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_xy = sum(x * y for x, y in zip(x_values, y_values))
    sum_x2 = sum(x ** 2 for x in x_values)
    sum_y2 = sum(y ** 2 for y in y_values)

    numerator = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x2 - sum_x ** 2) *
                   (n * sum_y2 - sum_y ** 2)) ** 0.5

    if denominator == 0:
        return corr
    corr = numerator / denominator
    return corr


heat_map_data = [[None for _ in range(7)] for _ in range(7)]
atttibute_list = ['BIKE_COST', 'OCC_HOUR', 'OCC_MONTH',
                  'BIKE_SPEED', 'HOOD_140', 'LONG_WGS84', 'LAT_WGS84']


for i in range(len(atttibute_list)):
    for j in range(len(atttibute_list)):
        corr = get_pearson_correlation(i, j)
        heat_map_data[i][j] = round(corr, 3)
        # print(i,j,' = ', corr)


# plotting the heatmap
hm = sns.heatmap(data=heat_map_data,
                 annot=True,
                 xticklabels=atttibute_list,
                 yticklabels=atttibute_list
                 )

# displaying the plotted heatmap
plt.show()
