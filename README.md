python_Time-consuming
=====================

utils for common test

Example
========
```python
#coding:utf-8
from tc import TC


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
```

output:
```shell
Time-consuming: 3.000021 ms

another test:
Time-consuming: 3.000021 ms
```


