# imports needed libraries

import datetime
import time as t

# Defines time()
# oh = OffsetHour
# om = OffsetMin
def timezone(oh,om,os=float(61)):
    # gets utc Min,Hour,Sec
    uH = int(datetime.datetime.utcnow().strftime("%H"))
    uM = int(datetime.datetime.utcnow().strftime("%M"))
    uS = int(datetime.datetime.utcnow().strftime("%S"))

    # Converts UTC to Current time in your location
    S = 0
    if os==0:
        H = uH+oh
        M = uM+om
    else:
        H = int(uH+oh)
        M = int(uM+om)
        S = int(uS+os)

    # Checks if M > 60 then sets M = M-60 -
    # And Sets H = H+1

    if S > 60:
        S = S-60
        M = M+1
    
    if M > 60:
        M = M-60
        H = H+1
    
    # Converts to 12 Hour Format
    
    if H > 12:
        H = H-12
        T = f"{H}:{M}:{S} p.m"
    else:
        T = f"{H}:{M}:{S} a.m"
    
    # returns Time
    return T

# lde = longitude
# tzof = timezone offset by utc
# tzofo = timezone offset by utc output
# trn = Time Right Now
# h=hour m=minute s=secon
# 

# inputs lde
lde = float(input("Input Longitude\n> "))

# sets tzof to offset between longitude and utc
tzof = (lde * 4) / 60

# sets h,m,s
h = int(tzof)
m = (tzof*60) % 60
s = (tzof * 3600) % 60

# sets tzofo to correct time
tzofo = "Your time off set is %d:%02d:%02d" % (h,m,s)

#prints tzofo
print(tzofo)

# sets trn to time offset
trn = timezone(h,m,s)

# prints trn
print(f"Time Right Now is {trn}")

# waits 10 secs before closing
t.sleep(10)