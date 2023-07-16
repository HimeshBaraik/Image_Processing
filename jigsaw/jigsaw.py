from google.colab.patches import cv2_imshow
import numpy as np
import cv2 as cv
def gutter(number):
  image = cv.imread(f"gutters{number}.JPG")
  cv2_imshow(f"gutters{number}.JPG")
  gray = cv.cvtColor(image, code = cv.COLOR_BGR2GRAY)
  width = gray.shape[1]
  height = gray.shape[0]
  print(f"{width} x {height}")
  if number == 1:
    dil_img = cv.dilate(gray, np.ones((5, 5)))
    blur_img = cv.GaussianBlur(dil_img, (7,7), 128 )
    final = 255 - cv.absdiff(blur_img, gray)
    for i in range(0, height):
      for j in range(0, 100):
        final[i][j] = ( final[i][j] / 255 ) ** (1.4) * 255
  elif number == 2:
    dil_img = cv.dilate(gray, np.ones((19, 19)))
    blur_img = cv.medianBlur(dil_img, 23)
    final = 255 - cv.absdiff(blur_img, gray)
  elif number == 3:
    final = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, [2], [2])
  cv2_imshow(final)
