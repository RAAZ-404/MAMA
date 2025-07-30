import os, sys, platform


bit = platform.architecture()[0]
if "32bit" in bit:
    os.system("clear")
    print(" your device is 32bit ")
    print(" tool not supported ")
elif "64bit" in bit:
    os.system("clear")
    print(" welcome .... ")
    import mama64
else:
    os.system("clear")
    print(" unknown arch ")
    sys.exit()
