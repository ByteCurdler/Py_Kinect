import sys
exec("import " + sys.argv[1] + " as module")
while True:
    want = ""
    while not want.startswith("\x01\x02"):
        want = raw_input()
    want = want[2:]
    if want.startswith("GET "):
        result = eval("module." + want[4:])
        if type(result) in [int, float]:
            print("\x01\x02" + str(result))
