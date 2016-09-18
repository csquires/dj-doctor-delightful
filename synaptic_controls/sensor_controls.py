from sensor_interface import SensorInterface as SI

sensor = SI()
try:
	sensor.connect()
except:
	print "Error connecting to sensor"
	raise

# image_data_sequence = sensor.get_image_data_sequence(2)
# image_data_sequence.show_images()