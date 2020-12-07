import os

# Write a program that opens the mean_temp.txt file in append+ mode
# Write a new line for "\nRio de Janeiro,Brazil,30.0,18.0"

# Grab the colum headings
# 1. Use .seek() to move the pointer to the beginning of the file
# 2. Read the first line of text into a variable called: headings
# 3. Convert headings into a list using .split(',') which splits on each comma

FILE_PATH = "./program1/mean_temp.txt"
NEW_RECORD = "\nRio de Janeiro,Brazil,30.0,18.0"
LINE_FORMAT = "City of {0} month ave: highest high is {1} Celsius"

mean_temps = open(FILE_PATH, "a+")

mean_temps.write(NEW_RECORD)

mean_temps.seek(0, 0)

headings = mean_temps.readline()
headings = headings.strip()
headings = headings.split(',')

line = mean_temps.readline()
while line:
    line = line.strip()

    if len(line) > 0:
        city_temp = line.split(',')
        city_name = city_temp[0]
        high_temp = city_temp[2]
        output_line = LINE_FORMAT.format(city_name, high_temp)
        print(output_line)

    line = mean_temps.readline()

mean_temps.close()
