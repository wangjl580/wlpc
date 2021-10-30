#概念
# 进程：是资源单位，占用一块内存区域，内部至少需要一个线程来执行
# 线程：是执行单位，cpu执行要找线程

# 启动一个程序，默认都会有一个主线程

#---单线程例子
'''
def func():
    for i in range(10):
        print('func',i)

if __name__ == '__main__':
    func()    #执行完func，才会执行，下面的循环
    for i in range(10):
        print('main',i)
'''

# 多线程
from threading import Thread

# #实现多线程的第一种写法
# from threading import Thread  #线程类

# def func():
#     for i in range(10):
#         print('func',i)

# if __name__ == "__main__":
#     t=Thread(target=func)  #创建一个线程类对象,  target=func：告诉子线程要干的事情。可以理解为：并给线程安排任务
#     t.start()  #开始执行该线程，多线程状态为可以开始工作状态，具体的执行时间由cpu决定  
#     for i in range(10):
#         print('mian',i)

#--程序多运行几次会发现，func和main交替执行，这就是多线程

#------------------------------
#实现多线程的第二种写法  #业界大佬常用的方法
# '''
class MyThread(Thread):  #创建一个线程子类, 继承了Thread类，是Thread的子类
    def run(self):  #覆写线程的run方法，self是固定的  --> 当线程被执行的时候: t.start()，执行run()
        for i in range(20):
            print("子线程", i)

if __name__  == "__main__":
    t=MyThread()  #类的实例化
    # t.run()  #类方法的调用，如果这样写就是单线程
    t.start()  #开启线程， 程序执行到这里，--> 就开始执行run()方法

    for i in range(20):
        print("主线程",i )
# '''

#给线程传递参数
# 方法1

# def func(name):    #为了区分两个进程，加个参数
#     for i in range(1000):
#         print(name,i) 

# if __name__ == "__main__":
#     t1=Thread(target=func, args=('周杰伦',))  #传参args后面必须是元组，且要加','
#     t1.start() 
    
#     t2=Thread(target=func, args=('王力宏',)) 
#     t2.start() 


# 方法2  这个方法我并未成功，以后考虑修改
'''
class MyThread(Thread):  
    def __init__(self,name):
        self.n=name
    def run(self):  
        for i in range(20):
            print(self.n, i)

if __name__  == "__main__":
    t1=MyThread(('周杰伦',))  
    t1.start() 
    
    t2=MyThread(('王力宏',))
    t2.start()
'''
