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

gc.collect()

# https://raw.githubusercontent.com/rrbotlab/hello-ota/refs/heads/main/hello_ota.py

def boot():
    try:
        gc.collect()
        hash_local = hexlify(uhashlib.sha256(open('hello_ota.py').read()).digest())
        r = urequests.get("https://raw.githubusercontent.com/rrbotlab/hello-ota/refs/heads/main/hello_ota.py") #?status=up&msg=OK&ping=1")
        # r = urequests.get("https://www.google.com") #?status=up&msg=OK&ping=1")
        print('r.response: \t', r.status_code)
        hash_remote = hexlify(uhashlib.sha256(r.content).digest())
        print('hash_local\t', hash_local)
        print('hash_remote\t', hash_remote)
        # with open('temp', "a") as fp:
        #     fp.write(r.content)
        r.close()
        gc.collect()

    except Exception as ex:
        print("boot error:", str(ex))


if __name__ == '__main__':
    boot()
