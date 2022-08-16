
#--------------KERAS---------------------
from tensorflow.keras.models import load_model
from tensorflow import keras


import keras_ocr
model = keras_ocr.recognition.Recognizer(alphabet="0123456789abcdefghijklmnopqrstuvwxyzáäæèéíñöøüćčđřšžșабвгдежзийклмнопрстуфхцчшьэюяі╓")
model.model.load_weights(r'P:\Jan-ML\ANPR\standard-anpr\data\models\CRNN\recognizer_fine_tune_last.h5')
#model = load_model(r'P:\Jan-ML\ANPR\standard-anpr\data\models\CRNN\recognizer_fine_tune_last.h5')
model.summary()


model_json = model.to_json()
with open("CRNN_ANPR.json", "w") as json_file:
   json_file.write(model_json)
print('JSON file written')
keras.utils.plot_model(
    model, to_file="CRNN_ANPR.png", show_shapes=True, show_dtype=True, show_layer_names=True, 
    rankdir="TB", expand_nested=False, dpi=96, layer_range=None, show_layer_activations=True,
)
print('finshed')

#------------------------PyTorch Tensorboard---------------------------
# from torch.utils.tensorboard import SummaryWriter
# import torch
# print(torch.__version__)
# from models import wpod_model
# model = wpod_model.wpod_net()
# #print(model)
# #model.to_device((torch.device('cpu')))
# model.load_state_dict(torch.load('/media/harshal/Coding/Jan-ML/premium-anpr/data/weights/wpod/sADAMmae1-WPOD/weights_WPOD_sADAMmae1.pth',
#                                 map_location=torch.device('cpu')))
# writer = SummaryWriter('./data')
# import numpy as np
# writer.add_graph(model, torch.tensor(np.random.random((1,3,120, 480))).float())





print('finished2')
