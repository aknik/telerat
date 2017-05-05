try:
    from platform import node, system, release, machine, platform, processor, win32_ver, python_version, python_compiler, python_implementation
    from os import popen
    from uuid import uuid4, getnode
    from requests import get
    from json import dumps, loads
except ImportError as e:
    print str(e)

ram =  ""
def ramWin():
    a = 0
    for m in popen('wmic memorychip get capacity').read().split("  \r\n")[1:-1]:
            a += int(m)
    return a / (1024**3); process.close()

def allinfo():
    global ram
    if system() == "Linux":
        pass
    else:
        ram = ramWin()
    return info()

def info():
    global ram
    return "Network name: " + node() + "\nOS: %s" % (system()) + "\nKernel: %s" %(release()) + "\nUUID: " + str(uuid4()) + "\nMac address: " + ':'.join(['{:02x}'.format((getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1]) + "\nArch: " + machine() + "\nCPU: " + processor() + "\nOS uname: " + str(win32_ver()) + "\nRAM: %s Gb" %  (str(ram)) + "\nPython version:  " + python_version() + "\nPython compiler: " + str(python_compiler()) + "\nPython implementation : " + python_implementation() + "\n"


#print allinfo()
