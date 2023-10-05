import time
import L1_ina
import L1_log
import L2_vector



while(1):

    volts = L1_ina.readVolts()
    L1_log.tmpFile(volts, "voltage_fred")
    
    Dist = L2_vector.getNearest()
    L1_log.tmpFile(Dist[0], "obsm_fred") #Distance in m
    L1_log.tmpFile(Dist[1], "obsd_fred") #angle of object in degrees
    
    
    Cart = L2_vector.polar2cart(Dist[0], Dist[1])
    L1_log.tmpFile(Cart[0], "x_fred")
    L1_log.tmpFile(Cart[1], "y_fred")

    time.sleep(1)