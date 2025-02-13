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

gc.collect()

# https://raw.githubusercontent.com/rrbotlab/hello-ota/refs/heads/main/hello_ota.py

def boot():
    try:
        gc.collect()
        r = urequests.get("https://raw.githubusercontent.com/rrbotlab/hello-ota/refs/heads/main/hello_ota.py") #?status=up&msg=OK&ping=1")
        # r = urequests.get("https://www.google.com") #?status=up&msg=OK&ping=1")
        print('r.response: ', r.status_code)
        r.close()

    except Exception as ex:
        print("boot error:", str(ex))


if __name__ == '__main__':
    boot()
