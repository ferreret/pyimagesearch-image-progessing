import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and convert it to grayscale and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for (diameter, sigmaColor, sigmaSpace) in params:
    # apply bilateral filter and display the output image
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    title = "Bilateral Filter, Diameter: {}, Color Sigma: {}, Space Sigma: {}".format(diameter, sigmaColor, sigmaSpace)
    cv2.imshow(title, blurred)
    cv2.waitKey(0)
