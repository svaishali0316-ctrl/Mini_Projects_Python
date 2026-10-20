# Alarm

import time
import winsound
from datetime import datetime

print("=" * 30)
print("       ALARM CLOCK        ")
print("=" * 30)

def Set_Alarm():
     alarm_time = input("Enter the alarm time (24hrs format HH:MM): ")

     print("Alarm set for ", alarm_time)
 
     while True:
       current_time = datetime.now().strftime("%H:%M")
    
       if current_time == alarm_time:
          print("WAKE UP! ALARM TIME!")
        
          for i in range(6):
              winsound(2000, 1000)
        
          break


Set_Alarm()
    
