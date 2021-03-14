import h5py
import numpy as np
import shutil
import sys
sys.path.append('C:\\Users\\lamin\\Desktop\\PFE\\traffic_objetct_detection')
from misc_utils.tensor_sampling_utils import sample_tensors
from keras.optimizers import Adam
from keras import backend as K
from keras.models import load_model

from models.keras_ssd300 import ssd_300
from keras_loss_function.keras_ssd_loss import SSDLoss
from keras_layers.keras_layer_AnchorBoxes import AnchorBoxes
from keras_layers.keras_layer_DecodeDetections import DecodeDetections
from keras_layers.keras_layer_DecodeDetectionsFast import DecodeDetectionsFast
from keras_layers.keras_layer_L2Normalization import L2Normalization

def apprentissage_trft():

	poids_source_lien = 'C:\\Users\\lamin\\Desktop\\PFE\\traffic_objetct_detection\\VGG_coco_SSD_300x300_iter_400000.h5'
	poids_destination_lien='C:\\Users\\lamin\\Desktop\\PFE\\traffic_objetct_detection\\VGG_SSD_300x300_8_classes.h5'
	shutil.copy(poids_source_lien, poids_destination_lien)
	poids_source_file = h5py.File(poids_source_lien, 'r')
	poids_destination_file = h5py.File(poids_destination_lien)

	classifier_nom = ['conv4_3_norm_mbox_conf',
                    	'fc7_mbox_conf',
                    	'conv6_2_mbox_conf',
                    	'conv7_2_mbox_conf',
                    	'conv8_2_mbox_conf',
                    	'conv9_2_mbox_conf']
    

	n_classes_source = 81
	classes_interet = [0, 3, 8, 1, 2, 10, 4, 6, 12]
	
	for nom in classifier_nom:
    	
    	kernel = poids_source_file[nom][nom]['kernel:0'].value
    	bias = poids_source_file[nom][nom]['bias:0'].value

    	
    	height, width, in_channels, out_channels = kernel.shape
    
    	
    	if isinstance(classes_interet, (list, tuple)):
        	subsampling_indices = []
        	for i in range(int(out_channels/n_classes_source)):
            	indices = np.array(classes_interet) + i * n_classes_source
            	subsampling_indices.append(indices)
        	subsampling_indices = list(np.concatenate(subsampling_indices))
    	elif isinstance(classes_interet, int):
        	subsampling_indices = int(classes_interet * (out_channels/n_classes_source))
    	else:
        	raise ValueError("`classes_interet` doit etre entier ou(list/tuple).")
   
    	new_kernel, new_bias = sample_tensors(weights_list=[kernel, bias],
                                          	sampling_instructions=[height, width, in_channels, subsampling_indices],
                                          	axes=[[3]], 
                                          	init=['gaussian', 'zeros'],
                                          	mean=0.0,
                                          	stddev=0.005)
    
    	del poids_destination_file[name][name]['kernel:0']
    	del poids_destination_file[name][name]['bias:0']
    	
    	poids_destination_file[name][name].create_dataset(name='kernel:0', data=new_kernel)
    	poids_destination_file[name][name].create_dataset(name='bias:0', data=new_bias)

	poids_destination_file.flush()

	