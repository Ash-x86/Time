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
    if os==61:
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

def opt():
    # gets input of oh,om
    oh = int(input("Input time offset by Hours\n> "))
    om = int(input("Input time offset by minutes\n> "))
    # gets input of opt
    print("1 = time right now")
    print("2 = time looping every min")
    opt = input("> ")
    # checks if opt = 1
    if opt == "1":
        # prints time
        print(timezone(oh,om))
    elif opt == "2":
        # creates while loop
        while True:
            # prints time
            print(timezone(5,21))
            # waits 60 secs
            t.sleep(60)