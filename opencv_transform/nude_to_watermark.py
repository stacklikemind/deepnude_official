2
import cv2
import numpy as np
import os

# create_watermark ===============================================================
# return:
#	(<Boolean> True/False), depending on the transformation process
def create_watermark(nude):

	# Add alpha channel if missing
	if nude.shape[2] < 4:
		nude = np.dstack([nude, np.ones((512, 512), dtype="uint8") * 255])

	watermark = cv2.imread("fake.png", cv2.IMREAD_UNCHANGED)
	
	f1 = np.asarray([0, 0, 0, 250])   # red color filter
	f2 = np.asarray([255, 255, 255, 255])
	mask = cv2.bitwise_not(cv2.inRange(watermark, f1, f2))
	mask_inv = cv2.bitwise_not(mask)

	res1 = cv2.bitwise_and(nude, nude, mask = mask)
	res2 = cv2.bitwise_and(watermark, watermark, mask = mask_inv)
	res = cv2.add(res1, res2)

	alpha = 0.6
	return cv2.addWeighted(res, alpha, nude, 1 - alpha, 0) 
