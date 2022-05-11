# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


dayweek = 2
daymonth = 1
month = 1
year = 1901
counter = 0

while daymonth < 31 or month < 12 or year < 2000:
    daymonth = daymonth + 1
    dayweek = dayweek + 1
    if dayweek>7:
        dayweek=1
    if daymonth>28 and month==2 and year%4!=0 and (year%400!=0 or year%100==0):
        daymonth=1
        month=month+1
    if daymonth>29 and month==2:
        daymonth=1
        month=month+1
    if daymonth > 30 and (month == 9 or month == 4 or month == 6 or month == 11 ):
        daymonth = 1
        month = month + 1
    if daymonth>31:
        daymonth=1
        month=month+1
    if month> 12:
        month=1
        year=year+1
    if dayweek == 7 and daymonth == 1:
        counter = counter + 1
        print("!!!",counter,"!!!",year,month,daymonth)
    print(year,month,daymonth)
print("!!!",counter)