# October 13, 2016
# CS F003A - Foothill College

import re
import csv
pattern = re.compile("(\d\d\d)-(\d\d\d)-(\d\d\d\d)")

m = pattern.match("408-646-9337")

print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))

pattern2 = re.compile("^\d\d\d")
# ^ - match at beginning
# $ - match at the end
# [..] - match any single character in brackets


result = pattern2.sub("669", "408-646-9337")
print(result)

# Write to a file, overwritten every time
write_file = open("output_example.txt", "w")
write_file.write("This is my first output file in Python 3.5.2.\nToday is October 13, 2016\n")
write_file.close()


# In order to update, use +
write_file = open("output_example.txt", "a")
write_file.write("This  is a new new line")
write_file.close()

# Overwritten at the beginning of the text
write_file = open("output_example.txt", "r+")
write_file.write("This  is a new new new new new line\n")
write_file.close()

with open("../Assignment/CSV_Database_of_Last_Names.csv") as csvFile:
    fieldnames = ["Count", "Description", "Customer", "Amount"]
    rows = csv.DictReader(csvFile)
    for row in rows:
        lines.append(row["lastname"])
