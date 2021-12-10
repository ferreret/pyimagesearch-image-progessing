import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and convert it to grayscale and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# loop over each of the individual channels and display them
for (i, (name, channel)) in enumerate(zip(("B", "G", "R"), cv2.split(image))):
    cv2.imshow(name, channel)

# convert the image to the HSV color space and display it
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# loop over each of the individual channels and display them
for (i, (name, channel)) in enumerate(zip(("H", "S", "V"), cv2.split(hsv))):
    cv2.imshow(name, channel)

# convert the image to the L*a*b* color space and display it
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# loop over each of the individual channels and display them
for (i, (name, channel)) in enumerate(zip(("L", "A", "B"), cv2.split(lab))):
    cv2.imshow(name, channel)

cv2.waitKey(0)

