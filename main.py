__version__ = '0.0.4'
"""
Default main with escape key on IO 2
"""
import utime
import machine

led = machine.Pin(2, machine.Pin.OUT, value=0)
esc = machine.Pin(0, machine.Pin.IN)

# print('\n\nmain.py\t', __version__ + '\n')

print("__name__\t", __name__)
print("__version__\t", __version__)
print('')

utime.sleep(2)
if not esc.value():
    print("\nescape")
    led.value(1)
    import sys
    sys.exit()

try:
    led.value(1)
    import hello_ota
    # app.main()
except Exception as ex:
    led.value(0)
    print("\nmain.py exception: " + str(ex))
