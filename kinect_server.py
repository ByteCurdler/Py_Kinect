import sys
exec("import " + sys.argv[1] + " as module")
while True:
    want = ""
    while not want.startswith("\x01\x02"):
        want = raw_input("{Kinect} ")
    want = want[2:]
    if want.startswith("GET "):
        try:
            result = eval("module." + want[4:])
        except AttributeError:
            print("\x01\x02"+"ERR_NO_ATTR")
        if type(result) in [int, float]:
            print("\x01\x02" + str(result))
        elif type(result) == str:
            print("\x01\x02" + repr(result))
        else:
            print("\x01\x02"+"OBJECT")
    else:
        print("\x01\x02"+"ERR_UNKNOWN_INPUT")
