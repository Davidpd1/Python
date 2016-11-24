# David Powis-Dow CS 101:Python 
# 2016-10-02 v0.1
# Chapter 2 Exercise 8: What Time Will It Be with Input Twice  

time_now = int(input("What is the current time in military time? "))
wait_time = int(input("How many hours before the alarm rings? "))

time_now_calc = time_now // 100
day = 24

future_time = (time_now_calc + wait_time)

days = future_time // day 
time_of_day = (future_time % day) * 100

print("The alarm will sound in", days,"days at", time_of_day)
