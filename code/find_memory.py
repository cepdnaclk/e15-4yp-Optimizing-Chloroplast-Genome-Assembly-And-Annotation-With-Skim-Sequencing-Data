import multiprocessing as mp
import psutil
from psutil import Process
import os
print(mp.cpu_count())

def memory_usage_psutil():
 print(os.getpid())
 process = psutil.Process(input())
 mem = process.memory_percent()
 return mem


p=psutil.Process(23242)
threads= p.threads()
for i in threads:
 o=i[0]
 th = psutil.Process(o)
 cpu_perc = th.cpu_percent(interval=1)
 print('PID %s use %% CPU = %s' % (o,cpu_perc))
#print(threads)
consume_memory = range(20*1000*1000)

while True:
 print memory_usage_psutil()
 #print thread_usage_psutil()

