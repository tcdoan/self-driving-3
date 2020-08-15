import argparse
import cv2
import numpy as np
import os

# Hough is the tool to find lane lines in an given image.
# To run the program, just type:
# python hough.py <image_file_name>
class Hough:
    def __init__(self, img, polygon_pts):
        self.img = img

        # For test image, exit-ramp.jpg, decent parameters are:
        #   Low_threshold of 50 and high_threshold of 150 for Canny edge detection
        #   Region selection, vertices = [(0,imshape[0]),(450, 290), (490, 290), (imshape[1], imshape[0])]
        #   Parameters for Hough space grid to be a rho of 2 pixels and theta of 1 degree (pi/180 radian)
        #   A threshold of 15, meaning at least 15 points in image space need to be associated with each line segment. 
        #   Also imposed a min_line_length of 40 pixels, and max_line_gap of 20 pixels.
        #   With these parameters, Hough transform algorithm picks up lanes lines and nothing else!

        self.polygon_pts = polygon_pts

        self.blur_ksize = 5
        self.blur_sigmaX = 1
        self.blur_sigmaY = 0
        self.canny_threshold_low = 50
        self.canny_threshold_hi = 150

        # Distance and angular resolution of grid in Hough space.
        self.rho = 2
        self.theta = np.pi/180

        # Minimum number of votes a candidate line needs to have
        self.threshold = 15

        # Minimum length of a line (in pixels) accepted
        self.min_line_length = 40

        # Maximum distance between segments allowed to be connected into a single line
        self.max_line_gap = 20

        def onchangeBlurKernelSize(value):
            self.blur_ksize = value
            # Make sure it is an odd number
            self.blur_ksize += (self.blur_ksize + 1) %2
            self.line_segments()

        def onchangeBlurSigmaX(value):
            self.blur_sigmaX = value
            self.line_segments()

        def onchangeBlurSigmaY(value):
            self.blur_sigmaY = value
            self.line_segments()

        def onchangeCannyThresHoldLow(value):
            self.canny_threshold_low = value
            self.line_segments()

        def onchangeCannyThresHoldHi(value):
            self.canny_threshold_hi = value
            self.line_segments()

        def onchangeRho(value):
            self.rho = value
            self.line_segments()

        def onchangeThreshold(value):
            self.threshold = value
            self.line_segments()

        def onchangeMinLineLen(value):
            self.min_line_length = value
            self.line_segments()

        def onchangeMaxLineGap(value):
            self.max_line_gap = value
            self.line_segments()

        cv2.namedWindow('edges')
        cv2.namedWindow('hough')

        cv2.createTrackbar("blur_ksize", "edges", self.blur_ksize, 19, onchangeBlurKernelSize)
        cv2.createTrackbar("blur_sigmaX", "edges", self.blur_sigmaX, 20, onchangeBlurSigmaX)
        cv2.createTrackbar("blur_sigmaY", "edges", self.blur_sigmaY, 20, onchangeBlurSigmaY)
        cv2.createTrackbar("canny_threshold_low", "edges", self.canny_threshold_low, 255, onchangeCannyThresHoldLow)
        cv2.createTrackbar("canny_threshold_hi", "edges", self.canny_threshold_hi, 255, onchangeCannyThresHoldHi)

        cv2.createTrackbar("rho", "hough", self.rho, 100, onchangeRho)
        cv2.createTrackbar("threshold", "hough", self.threshold, 100, onchangeThreshold)
        cv2.createTrackbar("min_line_length", "hough", self.min_line_length, 100, onchangeMinLineLen)
        cv2.createTrackbar("max_line_gap", "hough", self.max_line_gap, 100, onchangeMaxLineGap)

        self.line_segments()

        print("Change the parameters from trackbar UI to fine tune.  Press a key to close.")
        cv2.waitKey(0)
        cv2.destroyWindow('edges')
        cv2.destroyWindow('hough')

    def line_segments(self):
        blur_gray = cv2.GaussianBlur(self.img, (self.blur_ksize, self.blur_ksize), self.blur_sigmaX, self.blur_sigmaY)

        self.edge_img = cv2.Canny(blur_gray, self.canny_threshold_low, self.canny_threshold_hi)

        mask  = np.zeros_like(self.edge_img)
        vertices = np.array([self.polygon_pts], dtype=np.int32)
        cv2.fillPoly(mask, vertices, 255)
        masked_edges = cv2.bitwise_and(self.edge_img, mask)

        lines = cv2.HoughLinesP(masked_edges, self.rho, self.theta, self.threshold,
                                np.array([]), self.min_line_length, self.max_line_gap)

        line_image = np.copy(self.img)*0
        line_image = np.dstack((line_image, line_image, line_image))

        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)
        
        # create a "color" binary image to combine with line image.
        color_edges = np.dstack((masked_edges, masked_edges, masked_edges))
        self.combo = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0)
        cv2.imshow('edges', self.edge_img)
        cv2.imshow('hough', self.combo)

def main():    
    parser = argparse.ArgumentParser(description='Visualizing line segments for lane line detection')
    parser.add_argument('filename')
    args = parser.parse_args()

    img = cv2.imread(args.filename, cv2.IMREAD_GRAYSCALE)
    poly_corners = [(0, img.shape[0]), (450, 290), (490, 290), (img.shape[1], img.shape[0])]

    cv2.imshow('original', img)
    hough = Hough(img, poly_corners)

    print("Fine tuned  parameters:")
    print("- blur_ksize:", hough.blur_ksize)
    print("- blur_sigmaX:", hough.blur_sigmaX)
    print("- blur_sigmaY:", hough.blur_sigmaY)
    print("- canny_threshold_low:", hough.canny_threshold_low)
    print("- canny_threshold_hi:", hough.canny_threshold_hi)
    print("- rho:", hough.rho)
    print("- threshold:", hough.threshold)
    print("- min_line_length:", hough.min_line_length)
    print("- max_line_gap:", hough.max_line_gap)

    path, fname = os.path.split(args.filename)
    file, ext = os.path.splitext(fname)
    edges_filename = os.path.join("output", root + "-edges" + ext)
    lines_filename = os.path.join("output", root + "-lines" + ext)    
    cv2.imwrite(edges_filename, hough.edge_img)
    cv2.imwrite(lines_filename, hough.combo)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
