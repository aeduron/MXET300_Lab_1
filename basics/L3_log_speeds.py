import time
import L1_ina
import L1_log
import L2_kinematics

while(1):
    volts = L1_ina.readVolts()
    L1_log.tmpFile(volts, "voltage_fred")

    C = L2_kinematics.getMotion()
    L1_log.tmpFile(C[0], "xdot_fred")
    L1_log.tmpFile(C[1], "thetadot_fred")
    
    PdCurrents = L2_kinematics.getPdCurrent()
    L1_log.tmpFile(PdCurrents[0], "left_fred")
    L1_log.tmpFile(PdCurrents[1], "right_fred")

    print("Left = " + PdCurrents[0] + " rad/s, Right = " + PdCurrents[1] + " rad/s" )

    time.sleep(1)