from datetime import datetime, timedelta

#### PARAMETERS ####

# Change to the date you started in (YYYY, MM, DD) format
date_started = datetime(2023, 8, 7)
# Goal that you wish to complete everyday
goal_per_day = 3
# Length of course in days which is 100 days long in our case
course_length = 100

#### PARAMETERS ####

# File that keeps count of the number of days completed
f = open("data.txt", "r")
text = f.read().split("= ")
days_completed = int(text.pop(1))
f.close()

todays_date = datetime.today()
completed_today = int(input("How many days worth of content did you complete today?\n"))
days_completed += completed_today
days_remaining = course_length - days_completed
days_passed = int((todays_date - date_started).days)
average = round((days_completed / days_passed), 2)
forecasted_date = todays_date.date() + timedelta(round(days_remaining / average))
days_till_forecast = forecasted_date - todays_date.date()
delta_to_goal = (goal_per_day * days_passed) - days_completed

print(f"You have completed {days_completed} days in total.")
print(f"Your running average is {average} days per day.")
print(
    f"To get to your goal of {goal_per_day} days per day, you need to complete {delta_to_goal} days of additional "
    f"study today.")
print(
    f"Your estimated date of completion at this rate is {forecasted_date} which is {days_till_forecast.days} days from "
    f"today.")

f = open("data.txt", "w")
f.write(f"Days of work completed in total = {days_completed}")
f.close()

# File that logs with date and time the completion status
if completed_today != 0:
    f = open("log.txt", "a")
    f.write(f"Finished {completed_today} day(s) worth of content on {todays_date}. Running Average = {average}\n")
    f.close()




