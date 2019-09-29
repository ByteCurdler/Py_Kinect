import pexpect as pex

class Py2Object:
    def __init__(self, parent, path):
        self._Py2_parent = parent
        self._Py2_path = path
    def __getattr__(self, attr):
        return self._Py2_parent.__getattr__(self._Py2_path + "." + attr)

class Py2:
    def __init__(self, file):
        self._Py2_p = pex.spawn("python2 kinect_server.py %s" % file.replace(" ", "\ "))
    def __getattr__(self, attr):
        self._Py2_p.sendline("\x01\x02GET %s" % attr)
        result = ""
        while not result.startswith("\x01\x02"):
            result = self._Py2_p.readline().decode()
        ret = result[2:-2]
        if ret.isdigit():
            return int(ret)
        else:
            try:
                return float(ret)
            except:
                pass
            if ret[0] + ret[-1] in ["''", '""']:
                return eval(ret)
            elif ret == "OBJECT":
                return Py2Object(self, attr)
            elif ret == "ERR_WRONG_TYPE":
                raise TypeError("Argument is not of type int, float or str")
            elif ret == "ERR_NO_ATTR":
                raise AttributeError("No attribute %s" % attr)
            elif ret == "ERR_UNKNOWN_INPUT":
                raise IOError("The Py2 server was given unknown input")
            else:
                raise IOError("Unknown input \"%s\" marked as Py2's" % ret)

import2 = Py2
