import cv2 as cv
import mss
import numpy as np
import os
import time

output_folder = "./mss/images"
os.makedirs(output_folder, exist_ok=True)
frame_count = 0

with mss.mss() as sct:
    while "Screenshotting":
        last_time = time.time()

        # Screenshot Monitor 1
        img = np.array(sct.grab(sct.monitors[1]))

        # Display
        # cv.imshow("OpenCV/Numpy", img)

        # Save
        filename = os.path.join(output_folder, f"image_{frame_count:04d}.png")
        cv.imwrite(filename, cv.cvtColor(img, cv.COLOR_BGRA2BGR))
        frame_count += 1

        print(f"Saved: {filename} FPS: {1 / (time.time() - last_time)}")

        # Press "q" to quit.
        # if cv.waitKey(25) & 0xFF == ord("q"):
        #    cv.destroyAllWindows()
        #    break

        time.sleep(1)
