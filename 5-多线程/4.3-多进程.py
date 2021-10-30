from multiprocessing import Process  #多进程

# 多进程的第一种方法
'''
def func():
    for i in range(1000):
        print('子进程--',i)

#---其逻辑和多线程是一样的
if __name__ == "__main__":
    p=Process(target=func) #创建一个子进程类对象，类的实例化
    p.start()  
    for i in range(1000):
        print('主进程++',i)
'''

# 多进程的第二种方法, 与多线程的形式一样, 参考4.2-多线程的文档文字说明和理解
# '''
class MyProcess(Process):
    def run(self):
        for i in range(10):
            print("子线程--",i)

if __name__ == "__main__":
    p=MyProcess()
    p.start()
    for i in range(100):
        print("主进程++",i)
# '''
