import RPi.GPIO as GPIO
import time, sys
GPIO.setmode(GPIO.BOARD)
inpt = 13
GPIO.setup(inpt,GPIO.IN)
rate_cnt = 0
tot_cnt = 0
minutes = 0
constant = 0.10
time_new = 0.0

print('Water Flow')

while True:
    time_new = time.time() + 10
    rate_cnt = 0
    while time.time() <= time_new:
        if GPIO.input(inpt)!= 0:
            rate_cnt += 1
            tot_cnt += 1
        try:
           print(GPIO.input(inpt), end='')
        except KeyboardInterrupt:
           print('\nCTRL C - Exiting nicely')
           GPIO.cleanup()
           sys.exit()
    minutes += 1
    file = open('/home/pi/MindLabs/flow.txt', 'w')
    file.write((str)(round(rate_cnt * constant,4)))
    file.close()
    print('\nLiters / min ', round(rate_cnt * constant,4))
    print('Total Liters ', round(tot_cnt * constant, 4))
    print('Time (min & clock) ', minutes, '\t', time.asctime(time.localtime()))

GPIO.cleanup()
print('Done')
