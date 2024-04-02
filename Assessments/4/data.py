import random
from random import randint
import datetime

# create data for Project Table
def end_date1():
 start_date = datetime.date(2020, 1, 1)
 end_date = datetime.date(2026, 2, 1)

 time_between_dates = end_date - start_date
 days_between_dates = time_between_dates.days
 random_number_of_days = random.randrange(days_between_dates)
 random_date = start_date + datetime.timedelta(days=random_number_of_days)
 return str(random_date)

start_date1 = datetime.date(2020, 1, 1)

with open("project.txt", "w") as f:
    for i in range(1,1001):
        f.write(str(i)+",")
        f.write("ProjectName"+str(i)+",")
        f.write(str(start_date1)+",")
        f.write(end_date1()+",")
        f.write(str(random.randint(1,5))+"\n")



# create data for Employee Table
def random_with_N_digits(n):
  range_start = 10**(n-1)
  range_end = (10**n)-1
  return str(randint(range_start, range_end))

def education():
 list1=["PhD", "MBA", "MS/MA", "BS/BA", "HS/GED"]
 b=random.randint(0,1)
 return list1[b]

def dob():
 start_date = datetime.date(1900, 1, 1)
 end_date = datetime.date(2000, 1, 1)

 time_between_dates = end_date - start_date
 days_between_dates = time_between_dates.days
 random_number_of_days = random.randrange(days_between_dates)
 random_date = start_date + datetime.timedelta(days=random_number_of_days)
 return str(random_date)

with open("Candidates.txt", "w") as f:
    for i in range(1,10001):
        f.write(str(i)+",")
        f.write(random_with_N_digits(9)+",")
        f.write(sex()+",")
        f.write(dob()+",")
        f.write("TitleName"+str(i)+",")
        f.write("FirstNameEmployee"+str(i)+",")
        f.write("LastNameEmployee"+str(i)+",")
        f.write(str(random.randint(1,1000))+"\n")

# create data for Dependent Table
with open("dependent.txt", "w") as f:
    for i in range(1,10001):
        f.write(str(i)+",")
        f.write(random_with_N_digits(9)+",")
        f.write("FirstNameEmployee"+str(i)+",")
        f.write("LastNameEmployee"+str(i)+",")
        f.write(dob()+",")
        f.write(sex()+",")
        f.write(str(random.randint(1,10000))+"\n")

# create data for Manages Table
with open("manages.txt", "w") as f:
    for i in range(1,6):
        f.write(str(i)+",")
        f.write(str(random.randint(1,10000))+"\n")

# create data for Works On Table
with open("workson.txt", "w") as f:
    for i in range(10000):
        f.write(str(random.randint(1,10000))+",")
        f.write(str(random.randint(1,1000))+"\n")


def start_date_works_for():
 start_date = datetime.date(2006, 1, 1)
 end_date = datetime.date(2020, 1, 1)

 time_between_dates = end_date - start_date
 days_between_dates = time_between_dates.days
 random_number_of_days = random.randrange(days_between_dates)
 random_date = start_date + datetime.timedelta(days=random_number_of_days)
 return str(random_date)


# create data for Works For Table
with open("worksfor.txt", "w") as f:
    for i in range(10000):
        f.write(str(random.randint(1,5))+",")
        f.write(str(random.randint(1,10000))+",")
        f.write(start_date_works_for()+"\n")
