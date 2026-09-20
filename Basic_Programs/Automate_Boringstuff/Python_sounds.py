import time

import winsound

freq = 500
dur = 80
x = "Start"
if True:
    # loop iterates 5 times i.e, 5 beeps will be produced.
    for i in range(0,7):

        winsound.Beep(freq, dur)

        time.sleep(0.2)
