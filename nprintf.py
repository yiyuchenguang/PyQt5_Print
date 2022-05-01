from inspect import getframeinfo, stack
import os
import time

def nprintf(*args ,  level = "INFO", end = " "):
    datatime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    caller = getframeinfo(stack()[1][0])
    message = end.join(["{}".format(i) for i in args])
    str = "{} - {}[line:{}] - {}:\n{}".format(datatime, os.path.split(caller.filename)[1], caller.lineno, level, message )
    print(str)
