# Digital_Clock

import time

print("=" * 60)
print("              DIGITAL CLOCK              ")
print("=" * 60)

while True:
    current_time=time.strftime("%H:%M:%S")
    print("Current Time: ",current_time, end="\r")
    time.sleep(1)

