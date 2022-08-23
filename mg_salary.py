# mg_salary overtime check

# type the following into your terminal to run the file:

#      python3 mg_salary.py "mg_salary.csv"

# don't forget the quotation marks around the file name

import pandas as pd
import sys

file_name = sys.argv[1]

mg_salary = pd.DataFrame(pd.read_csv(file_name))

print()

count = 0
for index, row in mg_salary.iterrows():
    if index > 200:
        break
    if row["Total Hours"] > 40:
        print(row["Name"] + " worked " + str(row["Total Hours"] - 40) + " overtime hours during the week of " + str(row["Week"]))
        count += 1

print()
print("Process complete. Detected " + str(count) + " employee(s) that worked overtime hours.")
print()