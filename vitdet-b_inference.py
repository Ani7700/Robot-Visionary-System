from functools import partial

from detectron2 import model_zoo
from detectron2.config import LazyCall as L

model = model_zoo.get_config("common/models/mask_rcnn_vitdet.py").model

# Initialization and trainer settings
train = model_zoo.get_config("common/train.py").train
train.amp.enabled = True
train.ddp.fp16_compression = True
train.init_checkpoint = "model_final_61ccd1.pkl"