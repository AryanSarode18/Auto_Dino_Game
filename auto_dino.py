import cv2
import pyautogui
import numpy as np
import time

while True:
    image = pyautogui.screenshot(region=(200, 350, 255, 250))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    black_pixel_count = np.sum(image < 100)
    white_pixel_count = np.sum(image > 100)

    print("Number of Black Pixels:", black_pixel_count)
    print("Number of White Pixels:", white_pixel_count)

    if 4000 < black_pixel_count < 30000:
        time.sleep(0.0001)
        pyautogui.press('up')
    if 4000 < white_pixel_count < 30000:
        time.sleep(0.0001)
        pyautogui.press('up')

    cv2.imshow('image', image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break