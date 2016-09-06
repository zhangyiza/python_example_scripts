# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:28:16 2016

@author: Yingzhi
"""

import time
import threading

a = 0

#定义两个事件
def event1(e):  #2秒
    for i in range(2):
        print 'evert1({}) ing... at {}'.format(e, time.ctime())
        time.sleep(1)

def event2(e):  #15秒
    global a
    for i in range(3):
        print 'evert2({}) ing... at {}'.format(e, time.ctime())
        a+=1
        time.sleep(5)

#创建线程列表，start后的线程都要存进去，所以里面可能有正在运行/运行完毕的线程
workers = []
# 创建Thread类，target=该线程运行的函数，args=(arg1, arg2,..)对target函数传参
#得到<Thread(Thread-25, initial)>
worker1 = threading.Thread(target=event1, args=('cooking',))
worker1.start()       #开始跑线程
workers.append(worker1)     #start后马上存进列表
worker2 = threading.Thread(target=event2, args=('reading',))
worker2.start()
workers.append(worker2)
#join，可设置线程结束后再运行主程序，可设置最多等几秒
worker1.join()
worker2.join(6)

#主程序
print 'main event continue at {}'.format(time.ctime())

#Lock
t = time.time()
l = 0
#lock = threading.Lock()
def addx(x):
    global l, lock
    for i in range(10):
        time.sleep(1)
#        if lock.acquire():
        l+=1
#            lock.release()

workers = []
worker1 = threading.Thread(target=addx, args=(1,))
worker2 = threading.Thread(target=addx, args=(2,))
worker1.setDaemon(True)
worker2.setDaemon(True)
worker1.start()
worker2.start()
workers.append(worker1)
workers.append(worker2)

worker1.join()
worker2.join()

print 'runtime ' + str(time.time()-t)

