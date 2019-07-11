# This file is executed on every boot (including wake-boot from deepsleep)
from machine import ADC
import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()

print (machine.ADC(1).read())
print (machine.ADC(0).read())

