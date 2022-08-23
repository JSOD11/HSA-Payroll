# HSA_payroll
Harvard Student Agencies is the largest student-run business in the world, with 500+ workers and over $10M in yearly revenue. This is software I wrote for Harvard Student Agencies in order to automate the payroll error-checking process.

HSA Corporate as well as five of its component agencies have hourly workers:

* [Harvard Student Agencies](https://hsa.net)
* [The Harvard Shop](https://www.theharvardshop.com)
* [Cleaners and Dorm Essentials](https://dormessentials.hsa.net)
* [HSA Tutoring](https://hsatutoring.com)
* [Trademark Tours](https://trademarktours.com)
* [The Academies by HSA](https://www.academies.hsa.net)

The previous process of verifying hours for hourly workers across HSA and its agencies was error-ridden and required large amounts of manual labor from business office workers within HSA. I automated this job by writing software that can be run by payroll managers in order to scan for a variety of errors before payroll is submitted to the business office and logged in ADP. Time is saved by reducing the amount of physical work required to check long excel sheets, and time is also saved by allowing payroll managers to check their hourly workers' hours themselves very quickly rather than needing the BO to check first, then communicate this back to the payroll manager, who then communicates this back to the hourlies, and then the reverse. 

This process has significantly reduced internal headache and catches more errors than before.

## Types of errors

This software checks for a variety of possible errors:

* Employee logged overlapping work intervals
* Employee logged unusually long work intervals
* Employee began a work interval at an unusual time
* Employee worked overtime hours and was not compensated correctly
* Employee worked on a Sunday but is not being paid the Sunday rate
* Employee is not being paid the correct hourly rate for their agency-specific role

## Implementation

The general structure that allows this problem to be solved is the creation of a dictionary containing each employee's name as a key. This key maps to another dictionary, the keys of which are the days that employee worked in the current payroll cycle. Each of these days maps to a list of lists, which contains the  intervals that were worked on the given day, sorted by start time. This allows for us to easily pass through a day and see if there are any overlapping intervals: If an employee worked from [a,b] and [c,d], and the intervals are sorted by start time, then there is an overlapping work interval iff c < b. To compare dates in the form of 12:30 PM, I took each date and mapped it to a number in the range [0, 86400] (the number of seconds in the day).

After solving this problem and organizing the data in this way, the rest of the checks came rather naturally. For example, this allows us to very easily determine the length of work intervals and inspect the start times of work intervals. The other issues can also be quite easily checked by looping over the data entries.
