import os
import cv2
import numpy as np


def extract_face(img):
	# Establishing paths to the model data files
	base_dir = os.path.dirname(__file__)
	prototxt_path = os.path.join(base_dir + '/model_data/deploy.prototxt')
	caffemodel_path = os.path.join(base_dir + '/model_data/weights.caffemodel')

	face_model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

	image = cv2.imread('uploads/prathamesh.jpg')

	(h, w) = image.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
	face_model.setInput(blob)
	detections = face_model.forward()
	# Identify each face
	for i in range(0, detections.shape[2]):
		box=detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")
		confidence = detections[0, 0, i, 2]
		
		if confidence > 0.5:
			frame = image[startY:endY, startX:endX]
			cv2.imwrite(base_dir+'/uploads/faces/prathamesh.jpg', frame)
			# cv2.imshow("frame",frame)
			# cv2.waitKey(0)
			# cv2.destroyAllWindows()

if __name__ == '__main__':
	extract_face('uploads/prathamesh.jpg')