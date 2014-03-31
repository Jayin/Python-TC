#coding:utf-8
from tc import TC,Test


def task():
    for x in range(1,200000,2):
        pass

#basic
with TC() as test:
    task()

#custom:
class T(TC):
    def __init__(self):
        super(T,self).__init__()

    def __enter__(self):
        super(T,self).__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('another test:')
        super(T,self).__exit__(exc_type, exc_val, exc_tb)

print
with T() as t:
    task()

print

@Test
def work():
    for x in range(1,200000,2):
        pass

work()


