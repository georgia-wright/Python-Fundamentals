
#use date time library

# todays date

# date born




import datetime

# first attempt
# date = datetime.datetime(2020, 5, 17)

# number_of_days_in_year = date.strftime("%j"))

# number_of_days_in_year + (365*)

today = datetime.date.today()

dob = datetime.date(1991, 8, 13)

alive_for = (today - dob).days

print(f" I have been alive for {alive_for} days")













