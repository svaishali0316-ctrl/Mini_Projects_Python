# Stopwatch

import time

print("="*30)
print("             STOPWATCH             ")
print("="*30)

print("Stopwatch started!")

start=time.time()

input("Press enter to stopwatch... ")

stop=time.time()

total=stop-start

print("Time Taken: ",round(total,3),"seconds")
