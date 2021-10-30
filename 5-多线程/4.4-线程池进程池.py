# 线程池：一次性开辟一些线程，用户直接给线程池提交任务。线程任务的调度交给线程池来完成。
# 调度：比如1000个任务交给50个线程工作，50个完成后，哪50个任务再开始工作。


# python3 中如何来做？
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor  #线程池和进程池

def fn(name):
    for i in range(1000):
        print(name,i)

if __name__ == "__main__":
    #创建线程池
    with ThreadPoolExecutor(50) as t: #创建有50个线程的线程池  # ThreadPoolExcutor 改成ProcessPoolExecutor就变成进程池
        for i in range(100):
            t.submit(fn, name=f"线程{i}")  #给线程池提交一个任务，在for循环里，故100个任务，name指定前面fn函数的参数
    #with： 等待线程池中的任务全部执行完毕，才继续执行，这称为守护。

    print('123')  #这里会等待线程执行完毕才会执行print


# 进程池：
# with 后面 ThreadPoolExcutor 改成ProcessPoolExecutor就变成进程池
