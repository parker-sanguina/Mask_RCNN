import os
import json

"""
Acces json file from labelling and double check whether or not
images are contained in the folder. If this isn't done, there 
will be an issue with annotations not aligning with available images.
"""
DIR = os.getcwd()

train_path = os.path.join(DIR, "datasets/fingernail/train")
val_path = os.path.join(DIR, "datasets/fingernail/val")

#print(train_path)
#print(val_path)

train_annots = json.load(open(os.path.join(train_path, "train.json")))
val_annots = json.load(open(os.path.join(val_path, "val.json")))

train = set([f.split(".png")[0] for f in train_annots["_via_image_id_list"]])
val = set([f.split(".png")[0] for f in val_annots["_via_image_id_list"]])

train_images_set = set([f.split(".png")[0] for f in os.listdir(train_path)])
val_images_set = set([f.split(".png")[0] for f in os.listdir(val_path)])

#print(train_images_set - train)     # This shouldn't return anything except ".DS_Store" and "train.json"
#print(val_images_set - val)   # This shouldn't return anything except ".DS_Store" and "val.json"