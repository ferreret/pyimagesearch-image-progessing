import argparse
import cv2

# construct and parse command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-s", "--scharr", type=int, default=0, help="whether to use Scharr operator")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray", gray)

# set the kernel size, depending on whether we are using the Scharr
# then compute the gradient along the x and y axes respectively
ksize = -1 if args["scharr"] > 0 else 3
gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)

# the gradient magnitudes are now of the floating point data type,
# so take the absolute value and then cast it back to an unsigned 8-bit integer
gx = cv2.convertScaleAbs(gradX)
gy = cv2.convertScaleAbs(gradY)

# combine the two gradient images together
combined = cv2.addWeighted(gx, 0.5, gy, 0.5, 0)

# show the output images
cv2.imshow("Sobel X", gx)
cv2.imshow("Sobel Y", gy)
cv2.imshow("Combined", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()