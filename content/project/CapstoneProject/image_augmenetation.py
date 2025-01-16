import cv2 as cv2
import numpy as np

# Opening the image
img = cv2.imread('content/project/CapstoneProject/autocadTemplate.png', 1)
# cv2.imshow('Original Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# need to find the color of the gray background
# place a red dot at pixel 30, 30
# Finding the color of the image at the pixel 30, 30
# print(img[30, 30]) # = [56 50 45]
# background = img[30, 30]

# Now we need to loop through the image and anywhere the image is the same color as the background, we make it white.
# all other pixels will be black

# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         pixel_color = img[i, j]
#         difference = np.abs(pixel_color - background)
#         # print(difference)

#         if difference[0] < 4 and difference[1] < 4 and difference[2] < 4:
#             img[i, j] = [255, 255, 255]
#         else:
#             img[i, j] = [0, 0, 0]


# Threshold the colors in the image
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray Image', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# flip the colors
gray = cv2.bitwise_not(gray)



# Threshold the image
_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)




cv2.imshow('Image with red dot', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('AugmetnedSample.png', threshold)




