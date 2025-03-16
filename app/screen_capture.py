import numpy as np
import mss
import cv2

def capture_screen():
    """Fast screen capture on Linux"""
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        img = np.array(screenshot)[:, :, :3]
        return img

def stream_screen_capture():
    """Stream screen capture"""
    while True:
        img = capture_screen()
        cv2.imshow("Capture Live Stream", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
