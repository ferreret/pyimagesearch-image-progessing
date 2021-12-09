import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and convert it to grayscale and display it to our screen
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# Here is the image is not BN, you have to apply some thresholding to the image

# apply a series of erosions
for i in range(0, 3):
    eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Eroded {} times".format(i + 1), eroded)
    cv2.waitKey(0)

cv2.destroyAllWindows()

# apply a series of dilations
for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Dilated {} times".format(i + 1), dilated)
    cv2.waitKey(0)

cv2.destroyAllWindows()


# An opening
# Initialize a list of kernel sizes that will be applied to the image
kernelSizes = [(3, 3), (5, 5), (7, 7)]

# loop over the kernel sizes and apply an opening operation to the image
for kernelsize in kernelSizes:
    # construct a rectangular kernel of the current size and apply it to the image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelsize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(kernelsize[0], kernelsize[1]), opening)
    cv2.waitKey(0)


cv2.destroyAllWindows()

# Closing
# Initialize a list of kernel sizes that will be applied to the image
for kernelsize in kernelSizes:
    # construct a rectangular kernel of the current size and apply it to the image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelsize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(kernelsize[0], kernelsize[1]), closing)
    cv2.waitKey(0)

# morphological gradient
for kernelsize in kernelSizes:
    # construct a rectangular kernel of the current size and apply it to the image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelsize)
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient: ({}, {})".format(kernelsize[0], kernelsize[1]), gradient)
    cv2.waitKey(0)