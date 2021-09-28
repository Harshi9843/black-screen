import cv2
import time 
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)

time.sleep(2)
bg = 0

for frame in range(60):
	ret, bg = cap.read()

bg = np.flip(bg, axis = 1)

while(cap.isOpened()):
	ret, img = cap.read()
	if not ret:
		break
	image = np.flip(img, axis = 1)
	
	image = cv2.resize(image, (640, 480))
	frame = cv2.resize(frame, (640, 480))

	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	l_black = np.array([104, 153, 170])
	u_black = np.array([30, 30, 0])

	mask = cv2.inRange(frame, l_black, u_black)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	f = frame-res	
	f = np.where(f == 0, image, f)

	final_output = cv2.addWeighted(res, 1)
	output_file.write(final_output)

	cv2.imshow("magic", final_output)
	cv2.waitKey(1)

cap.release()
out.release()
cv2.destroyAllWindows()

