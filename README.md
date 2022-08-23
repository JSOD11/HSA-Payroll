# HSA_payroll
This is software I wrote for Harvard Student Agencies in order to automate the payroll error-checking process. Harvard Student Agencies is the largest student-run business in the world, with 500+ workers and over $10M in yearly revenue.

HSA Corporate as well as five of its component agencies have hourly workers:

* [Harvard Student Agencies](https://hsa.net)
* [The Harvard Shop](https://www.theharvardshop.com)
* [Cleaners and Dorm Essentials](https://dormessentials.hsa.net)
* [HSA Tutoring](https://hsatutoring.com)
* [Trademark Tours](https://trademarktours.com)
* [The Academies by HSA](https://www.academies.hsa.net)

The previous process of verifying hours for hourly workers across HSA and its agencies was error-ridden and required large amounts of manual labor from payroll workers within HSA. I automated this job by writing software that can be run by payroll managers in order to scan for a variety of errors before payroll is submitted to the business office and logged in ADP. Time is saved by reducing the amount of physical work required to check long excel sheets, and time is also saved by allowing payroll managers to check their hourly workers' hours themselves very quickly rather than needing the BO to check first, then communicate this back to the payroll manager, who then communicates this back to the hourlies, and then the reverse. 

This process has significantly reduced internal headache and catches more errors than before.

## Types of errors

This software checks for a few types of errors:

* Employee logged overlapping work intervals
* Employee logged unusually long work intervals
* Employee began a work interval at an unusual time
* Employee worked overtime hours
* Employee worked on a Sunday but is not being paid the Sunday rate
* Employee is not being paid the correct rate for their agency-specific role

## Implementation

The general structure that allows this problem to be solved is the creation of a dictionary containing each employee's name as a key. This key maps to another dictionary, the keys of which are the days they worked in the current payroll cycle. Each of these days maps to a list of lists, which contains the  intervals that were worked on that day, sorted by start time. This allows for us to easily pass through a day and see if there are any overlapping intervals: if an employee worked from [a,b] and [c,d], and the intervals are sorted by start time, then there is an overlapping work interval iff c < b. To compare dates in the form of 12:30 PM, I took each date and mapped it to a number in the range [0, 86400] (the number of seconds in the day).

After solving this problem and organizing the data in this way, the rest of the checks came rather naturally.
