import time
import L1_ina
import L1_log

while(1):
    volts = L1_ina.readVolts()
    L1_log.tmpFile(volts, "voltage_fred")
    time.sleep(1)
    