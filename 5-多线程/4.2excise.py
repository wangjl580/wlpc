
from threading import Thread


class Mythread(Thread):
    def run(self):
        for i in range(10):
            print('子线程',i)

if __name__ == "__main__":
    t=Mythread()
    t.start()
    for i in range(10):
        print("主线程",i)