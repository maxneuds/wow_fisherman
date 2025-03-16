from screen_capture import stream_screen_capture

# import mss
import pyscreenshot


def stream_screen_capture(interval=1):
    try:
        while True:
            im = pyscreenshot.grab()
            im.show()
            # time.sleep(interval)
    except KeyboardInterrupt:
        print("Screen capture stopped.")

if __name__ == "__main__":
    # capture_screen()
    stream_screen_capture()

# im = pyscreenshot.grab()
# im.show()


# def list_screens():
#     with mss.mss() as sct:
#         for monitor in sct.monitors:
#             print(monitor)

# def capture_screen():
#     with mss.mss() as sct:
#         # Capture the first monitor
#         monitor = sct.monitors[1]
#         fn = mss.mss().shot(mon=-1, output="screenshot.png")
#         print(fn)
#         # screenshot = sct.grab(monitor)
#         # print(screenshot)
#         # mss.tools.to_png(screenshot.rgb, screenshot.size, output='screenshot.png')

# if __name__ == "__main__":
#     # list_screens()
#     capture_screen()
#     # stream_screen_capture()


