import json

path = "datasets/fingernail/train/train.json"

data = json.load(open(path))

#print(data["_via_img_metadata"].keys())

# _via_img_metadata: contains all the images
# {"_via_img_metadata": {
#       "{filename+size}": {
#           "filename": "7.2.png,
#           "size": 14859027,  
#           "regions": [{
#               "shape_attributes": {
#                   "name": "polyline",
#                   "all_points_x": [...],
#                   "all_points_y": [...]},
#               "region_attributes": {}},
#               ... more regions ...
#               ],
#               "file_attributes": {}},
#       ... more files ...
#       }
# }
annotations = list(data["_via_img_metadata"].values())

annotations = [a for a in annotations if a['regions']]

print(annotations)