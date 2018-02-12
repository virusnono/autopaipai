# -*- coding: utf-8 -*-

import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard
m = PyMouse()
k = PyKeyboard()
n=0
while n<100:
    time.sleep(1)
    print(m.position())
    n+=1

input('输入[Enter]后退出。。。')