import os 
import time

second = 0    
minute = 0    
hours = 0
print("Stopwatch will start in 3 second")
time.sleep(3)    
while(True):    
    print("Simple Stopwatch Created By Abhishek Kumar Bharti...")
    print("Press ctrl+c to exit ")   
    print('\n\n\n\n\n\n\n')    
    print('\t\t\t\t-------------')    
    print('\t\t\t\t  %d : %d : %d '%(hours,minute,second))    
    print('\t\t\t\t-------------')    
    time.sleep(1)    
    second+=1    
    if(second == 60):    
        second = 0    
        minute+=1    
    if(minute == 60):    
        minute = 0    
        hour+=1;    
    os.system('cls')