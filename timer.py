import os
import time
import re


while True:
    timer = input("enter the time when to stop the timer =  ")
    if "second" in timer or "seconds"in timer:
        filtering = re.findall(r'\d+', timer)
        timer = int(''.join(filtering))
    elif ('minutes' not in timer and "minute" not in timer) and ("hour" in timer or "hours" in timer):
        filtering = re.findall(r'\d+', timer)
        timer = int(''.join(filtering))*3600
    elif ("hour" in timer or "hours" in timer) and ("minutes" in timer or "minute" in timer):
        print('hello')
        filtering = re.findall(r'\d+', timer)
        a=(int(''.join(filtering[0]))*3600)
        b=(int(''.join(filtering[1]))*60)
        timer =a+b
    elif "minutes" in timer or "minute" in timer:
        filtering = re.findall(r'\d+', timer)
        timer = int(''.join(filtering))*60
    else:
        print("Please! write valid number")

    when_to_stop =abs(int(timer))
    while when_to_stop >0:
        os.system('cls')
        m,s = divmod(when_to_stop,60)
        h,m = divmod(m,60)
        print("\n\n\n\n\n\n\n\n\n")
        print("\t\t\t\t|"+str(h).zfill(2)+":" + str(m).zfill(2)+":"+str(s).zfill(2)+"|")
        time.sleep(1)
        when_to_stop -=1
        print()
    print("\t\t\t\tTIME OUT")
    exit()