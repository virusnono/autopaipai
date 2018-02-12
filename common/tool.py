# -*- coding: utf-8 -*-#
# Created by: fwj

import datetime
import functools
import os
import threading
import const
import time
import sys

def writelog(file='log.log', logContent=None):
    if logContent is None:
        logContent = []
    now = datetime.datetime.now()
    dirName = os.path.dirname(file)
    if not os.path.exists(dirName):
        os.mkdir(dirName)

    result = now.strftime('%Y-%m-%d %H:%M:%S.%f') 
    result += ',{},{}'.format(os.getpid(), threading.current_thread().name)
    for i in range(len(logContent)):
        result += ',"{}"'.format(logContent[i])
    result +=  '\n'
        
    with open(file, 'a') as f:
        f.write(result)

def catchException(errors=(Exception, ), defaultValule=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            try:
                return func(*args, **kw)
            except Exception as e:
                # args[0].ShowError(e, func.__name__)
                funcName = func.__name__
                ErrorInfo = '{}失败！: {}'.format(const.FunctionName.get(funcName, funcName), repr(e))
                sys.stdout.write('thread({}) error: {}\n'.format(threading.currentThread().name, ErrorInfo))
                writelog(file='log\\error{}.log'.format(time.strftime('%Y%m%d')), logContent=['error', args[0].__class__.__name__, ErrorInfo])
                args[0].signal_ShowError.emit(e, funcName)
                return defaultValule
            
        return wrapper
    return decorator

def log():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            name = const.FunctionName.get(func.__name__, func.__name__)
            writelog(file='log\\{}{}.log'.format(args[0].__class__.__name__, time.strftime('%Y%m%d')), logContent=['info', name, args])
            # args[0].ShowStatus('{}开始!'.format(name))
            value = func(*args, **kw)
            # args[0].ShowStatus('{}结束!'.format(name))
            return value
        return wrapper
    return decorator
