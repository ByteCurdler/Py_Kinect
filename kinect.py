import pexpect as pex

class Py2:
    def __init__(self, file):
        self.p = pex.spawn("python2 kinect_server.py %s" % file.replace(" ", "\ "))
    def __getattr__(self, attr):
        self.p.sendline("\x01\x02GET %s" % attr)
        result = ""
        while not result.startswith("\x01\x02"):
            result = self.p.readline().decode()
        ret = result[2:]
        try:
            return int(ret)
        except:
            return float(ret)

import2 = Py2
