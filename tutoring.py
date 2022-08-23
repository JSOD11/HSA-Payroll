# tutoring payroll check

# type the following into your terminal to run the file:

#      python3 tutoring.py "tutoring.csv"

# don't forget the quotation marks around the file name

import pandas as pd
import sys
from collections import defaultdict

def main():

  file_name = sys.argv[1]
  tutoring = pd.DataFrame(pd.read_csv(file_name))

  error_count = 0

  # we will store employees in a dict of dicts, value is a list of lists
  employee_dict = defaultdict(lambda: defaultdict(list))

  for index, row in tutoring.iterrows():
      # dealing with at most 300 employees — increase this number if more are hired
      if index > 300:
          break
      start, end = timeConverter(row["Start Time"]), timeConverter(row["End Time"])
      # edge case in which the interval starts before 12AM and ends after 12AM
      if isinstance(end, int) and isinstance(start, int) and end < start:
          end += 86400
      # use custom data structure to keep days separate for each employee, add intervals to each day
      employee_dict[row["Name"]][row["Date"]].append([start, end])
      
  for employee in employee_dict:
      if isinstance(employee, float):
          nan = employee
      else:
          # sort intervals by start time
          for date in employee_dict[employee]:
              employee_dict[employee][date].sort()
      
  del employee_dict[nan]

  print()
  for employee in employee_dict:
      for date in employee_dict[employee]:
          intervals = employee_dict[employee][date]
          for j in range(len(intervals) - 1):
              if intervals[j][1] > intervals[j + 1][0]:
                  print("OVERLAP  " + employee + " has an overlapping work interval logged on " + date)
                  error_count += 1
          for start, end in intervals:
              if end - start > 14400:
                  print("LONG     " + employee + " has a work interval lasting longer than 4 hours on " + date)
                  error_count += 1
                  
              if 0 <= start <= 21600:
                  print("START    " + employee + " has a work interval starting between 12AM and 6AM on " + date)
                  error_count += 1
              
  print()
  print("Process complete. Detected " + str(error_count) + " possible error(s).")
  print()

def timeConverter(string):
    
    # function that converts string XX:XX XM --> integer in [0:86400]
    
    if not isinstance(string, str):
        return None
    
    res = 0
    
    if string[:2] == "12":
        res -= 43200
    
    j = 0
    
    hour = []
    while j < len(string):
        if string[j] == ":":
            j += 1
            break
        else:
            hour.append(string[j])
            j += 1
    
    minute = []
    while j < len(string):
        if string[j] == " ":
            j += 1
            break
        else:
            minute.append(string[j])
            j += 1
    
    res += int("".join(hour))*3600 + int("".join(minute))*60
    
    if string[j:] == "PM" or string[j:] == "pm":
        return res + 43200
    else:
        return res

main()