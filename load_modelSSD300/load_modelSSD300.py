import sys 
sys.path.append("C:\\Users\\lamin\\Desktop\\PFE\\traffic_objetct_detection")
import h5py
from keras.optimizers import Adam
from keras import backend as K
from keras.models import load_model
from models.keras_ssd300 import ssd_300
from keras_loss_function.keras_ssd_loss import SSDLoss
from keras_layers.keras_layer_AnchorBoxes import AnchorBoxes
from keras_layers.keras_layer_DecodeDetections import DecodeDetections
from keras_layers.keras_layer_DecodeDetectionsFast import DecodeDetectionsFast
from keras_layers.keras_layer_L2Normalization import L2Normalization

def model_detection():
		img_height = 300 # Height of the input images
		img_width = 300 # Width of the input images
		img_channels = 3 # Number of color channels of the input images
		subtract_mean = [123, 117, 104] # The per-channel mean of the images in the dataset
		swap_channels = [2, 1, 0] # The color channel order in the original SSD is BGR, so we should set this to `True`, but weirdly the results are better without swapping.
		# TODO: Set the number of classes.
		n_classes = 8 # Number of positive classes, e.g. 20 for Pascal VOC, 80 for MS COCO
		scales = [0.07, 0.15, 0.33, 0.51, 0.69, 0.87, 1.05] # The anchor box scaling factors used in the original SSD300 for the MS COCO datasets.
		# scales = [0.1, 0.2, 0.37, 0.54, 0.71, 0.88, 1.05] # The anchor box scaling factors used in the original SSD300 for the Pascal VOC datasets.
		aspect_ratios = [[1.0, 2.0, 0.5],
                 		[1.0, 2.0, 0.5, 3.0, 1.0/3.0],
                 		[1.0, 2.0, 0.5, 3.0, 1.0/3.0],
                 		[1.0, 2.0, 0.5, 3.0, 1.0/3.0],
                 		[1.0, 2.0, 0.5],
                 		[1.0, 2.0, 0.5]] # The anchor box aspect ratios used in the original SSD300; the order matters
		two_boxes_for_ar1 = True
		steps = [8, 16, 32, 64, 100, 300] # The space between two adjacent anchor box center points for each predictor layer.
		offsets = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5] # The offsets of the first anchor box center points from the top and left borders of the image as a fraction of the step size for each predictor layer.
		clip_boxes = False # Whether or not you want to limit the anchor boxes to lie entirely within the image boundaries
		variances = [0.1, 0.1, 0.2, 0.2] # The variances by which the encoded target coordinates are scaled as in the original implementation
		normalize_coords = True
		weights_path = 'C:\\Users\\lamin\\Desktop\\PFE\\traffic_objetct_detection\\weights\\VGG_coco_SSD_300x300_iter_400000_subsampled_8_classes.h5'
		model = ssd_300(image_size=(img_height, img_width, img_channels),
					n_classes=n_classes,
                	mode='inference',
                	l2_regularization=0.0005,
                	scales=scales,
                	aspect_ratios_per_layer=aspect_ratios,
                	two_boxes_for_ar1=two_boxes_for_ar1,
                	steps=steps,
                	offsets=offsets,
                	clip_boxes=clip_boxes,
                	variances=variances,
                	normalize_coords=normalize_coords,
                	subtract_mean=subtract_mean,
                	divide_by_stddev=None,
                	swap_channels=swap_channels,
                	confidence_thresh=0.5,
                	iou_threshold=0.45,
                	top_k=200,
                	nms_max_output_size=400,
                	return_predictor_sizes=False)

		print("Model built.")

		# 2: Load the sub-sampled weights into the model.

		# Load the weights that we've just created via sub-sampling.
	

		model.load_weights(weights_path, by_name=True)

		print("Weights file loaded:", weights_path)
		return model
	