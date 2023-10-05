import time
import L2_compass_heading
import L1_log


def direction(comp):
    if (comp >= -22.5) and (comp < 22.5):
        direction = "North"
    elif(comp >= 22.5) and (comp < 67.5):
        direction = "North East"
    elif(comp >= 67.5) and (comp < 112.5):
        direction = "East"
    elif(comp >= 112.5) and (comp < 157.5):
        direction = "South East"
    elif(comp >= 157.5)or ((comp < -157.5)):
        direction = "South"
    elif(comp < -112.5) and (comp >= -157.5):
        direction = "South West"
    elif(comp < -67.5) and (comp >= -112.5):
        direction = "West"
    elif(comp < -22.5) and (comp >= -67.5):
        direction = "Norht West"
    else:
        direction = "Error"
    return direction

while(1):
    comp = L2_compass_heading.get_heading()
    L1_log.tmpFile(comp, "comp_fred")

    direc = direction(comp)
    L1_log.stringTmpFile(direc, "direc_fred")

    time.sleep(1)
