import cv2 as cv
import mss
import numpy as np
import os
import time

from ultralytics import YOLO

model = YOLO("re4r.pt")

output_folder = "videos"
os.makedirs(output_folder, exist_ok=True)
fourcc = cv.VideoWriter_fourcc(*"mp4v")
vid = cv.VideoWriter(
    os.path.join(output_folder, "video_tracked.mp4"), fourcc, 24.0, (1280, 720)
)

with mss.mss() as sct:
    while "Tracking":
        last_time = time.time()

        # Screenshot Monitor 1
        img = np.array(sct.grab(sct.monitors[1]))

        results = model.track(cv.cvtColor(img, cv.COLOR_BGRA2BGR), persist=True)
        annotated_img = results[0].plot()
        vid.write(annotated_img)
        cv.imshow("YOLO11 Tracking", annotated_img)
        print(f"FPS: {1 / (time.time() - last_time)}")

        # Press "q" to quit.
        if cv.waitKey(25) & 0xFF == ord("q"):
            cv.destroyAllWindows()
            break
