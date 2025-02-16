# boot ota
# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
import uos, machine
# uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
# import webrepl
# webrepl.start()
# import mrequests as requests
import urequests
import uhashlib
from ubinascii import hexlify

# https://raw.githubusercontent.com/rrbotlab/hello-ota/refs/heads/main/hello_ota.py

def init():
    try:
        gc.collect()
        hash_local = hexlify(uhashlib.sha256(open('hello_ota.py').read()).digest())
        r = urequests.get("https://raw.githubusercontent.com/rrbotlab/hello-ota/main/hello_ota.py") #?status=up&msg=OK&ping=1")
        print('\nr.status_code: \t', r.status_code)
        if r.status_code == 200:
            hash_remote = hexlify(uhashlib.sha256(r.text).digest())
            print('hash_local\t', hash_local)
            print('hash_remote\t', hash_remote)
            if hash_remote != hash_local:
                print('updating...')
                with open('hello_ota.py', "w") as fp:
                    fp.write(r.text)
            else:
                print('updated')
            r.close()
        gc.collect()


    except Exception as ex:
        print("boot error:", str(ex))


if __name__ == '__main__':
    init()
    print('boot end')
