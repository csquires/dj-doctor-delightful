from sensor_interface import SensorInterface as SI
import time
import cv2
import numpy as np
import pickle

sensor = SI()
try:
	sensor.connect()
except:
	print "Error connecting to sensor"
	raise

def get_image_data_sequence(t):
	initial_time = time.time()
	image_data_sequence = []
	while time.time() - initial_time < t:
		images = sensor.getAllImages()
		image_data_sequence.extend(images)

	return image_data_sequence

def get_images(image_data_sequence):
	return map(lambda imageData: np.array(imageData["image"]), image_data_sequence)

def get_image_times(image_data_sequence):
	return map(lambda imageData: imageData["timeStamp"], image_data_sequence)

def normalize_images(images):
	baselined_images = images - images[0]
	image_max_val = np.max(images)
	image_min_val = np.min(images)
	normalized_images = (images-image_min_val)/float(image_max_val-image_min_val)*255
	normalized_images = normalized_images.astype(np.uint8)
	return map(lambda image: cv2.cvtColor(image, cv2.COLOR_GRAY2RGB), normalized_images)

def show_images(images,image_times):
	t=time.time()
	for i,image in enumerate(images):
		cv2.imshow("window",image)
		if i<len(images)-1:
			delay = image_times[i+1] - image_times[i]
			delay /= 1000 #convert from microseconds to milliseconds
		else:
			delay = 1
		print delay
		cv2.waitKey(delay)
	cv2.destroyAllWindows()
	print time.time()-t

	# to close window, have to send waitKey's to flush out messages
	for i in range(5):
		cv2.waitKey(1)

def record_and_playback():
	image_data_sequence = get_image_data_sequence(2)
	images = get_images(image_data_sequence)
	norm_images = normalize_images(images)
	times = get_image_times(image_data_sequence)
	show_images(images,times)
	return norm_images

def record_to_file(images):
	img = images[0]
	rows = img.shape[0]
	cols = img.shape[1]
	fourcc = cv2.cv.CV_FOURCC(*'XVID')
	out = cv2.VideoWriter('output.avi',fourcc, 20.0, (cols,rows))
	print out.isOpened()

	for image in images:
		cv2.imshow("frame",image)
		out.write(image)
	out.release()
	cv2.destroyAllWindows()

def record_now():
	image_data_sequence = get_image_data_sequence(2)
	images = get_images(image_data_sequence)
	norm_images = normalize_images(images)

	img = norm_images[0]
	rows = img.shape[0]
	cols = img.shape[1]
	fourcc = cv2.cv.CV_FOURCC(*'XVID')
	out = cv2.VideoWriter('output.avi',fourcc, 20.0, (cols,rows))
	print out.isOpened()

	for image in norm_images:
		cv2.imshow("frame",image)
		out.write(image)
	out.release()
	cv2.destroyAllWindows()

image_data_sequence = get_image_data_sequence(2)
images = get_images(image_data_sequence)
norm_images = normalize_images(images)