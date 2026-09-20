import numpy as np
import cv2
from PIL import ImageGrab

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out = cv2.VideoWriter("output.mpv4", fourcc,20.0,(1366,768))

while True:
    img =  ImageGrab.grab(bbox=(0,0,1280,720))
    img_np = np.array(img)
    cv2.imshow('SC',img_np)
    out.write(img_np)
    if cv2.waitKey(50) == ord('q'):
        break



# frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
# cv2.imshow("Screen", frame)
# out.write(frame)

# if cv2.waitKey(1)==27:
#     break
# out.release()
# cv2.destroyAllWindows()
