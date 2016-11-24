# David Powis-Dow CS:Python
# 2016-10-01 v0.1
# Modulus - Seconds conversion

total_secs = int(input("How many seconds, in total?"))
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("Hrs=", hours, " mins=", minutes, "secs=", secs_finally_remaining)

