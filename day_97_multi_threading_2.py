import threading
import time
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    #suppose it will take x seconds to execute so used sleep method
time1=time.perf_counter()
#performance time
# normal code
# func(5)
# func(2)
# func(1)

#using threads
t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[3])
t3=threading.Thread(target=func,args=[1])
t1.start()
t2.start()
t3.start()
# t1.join()
# t2.join()
# t3.join()
time2=time.perf_counter()
print(time2-time1,"seconds")
