import requests
import time

minutes = 1
oldtemp = "filler"
timer = False
reopen = False
start = 1000000000000
re = 100000000000
while True:
    file = open('/home/pi/MindLabs/temp.txt', 'r')
    temp = file.read()

    if(temp == "on"):
        if(temp != oldtemp):
            requests.post("https://maker.ifttt.com/trigger/valve/with/key/c8KQL3DmweeIca1KvGRrNJFNtjPicgesNPoNSs509JL")
            print("the valve is now open")
    else:
        if(temp != oldtemp):
            requests.post("https://maker.ifttt.com/trigger/valveOff/with/key/c8KQL3DmweeIca1KvGRrNJFNtjPicgesNPoNSs509JL")
            print("the valve is now close")
            timer = False


    time.sleep(.25)

    oldtemp = temp

    flowfile = open('/home/pi/MindLabs/flow.txt', 'r')
    flow = flowfile.read()
    print("flow: " + flow)

    try:
        if(float(flow) <= 1.0 or float(flow) >= 60.0):
            timer = False
    except:
        print("float not understood")
    
    if(timer == False):
        start = time.time()

    try:
        if(float(flow) >= 1.0):
            if(float(flow)<= 60.0):
                if(timer == False):
                    start = time.time()
                    print("timer started")
                    timer = True
    except:
        print("flow nothing")

    timeFile = open('/home/pi/MindLabs/maxTime.txt', 'r')
    minutes = int(timeFile.read())
    print("minutes:" + str(minutes))

    currentTime = time.time() - start
    
    if(currentTime > (minutes * 60)):
        if(timer == True):
            requests.post("https://maker.ifttt.com/trigger/valveOff/with/key/c8KQL3DmweeIca1KvGRrNJFNtjPicgesNPoNSs509JL")
            print("the valve is now close")
            timer = False
            reopen = True

    elif(timer == True):
        print(currentTime)

    if(reopen == False):
        re = time.time()

    currentreopenTime = time.time() - re
    
    if(reopen == True and currentreopenTime >= 300):
        reopen = False
        requests.post("https://maker.ifttt.com/trigger/valve/with/key/c8KQL3DmweeIca1KvGRrNJFNtjPicgesNPoNSs509JL")
        print("the valve is now reopen")
