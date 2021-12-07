from PIL import Image
import os
import copy

# Procedure
# 1) Loop over all images
# 2) Read image
# 3) Rotate image 270 degrees left
#       * This is how most of the original images are oriented
# 4) Manual note the images that haven't been correctly rotated and fix those

images = "/Users/parker/Desktop/only-images"

for i, img in enumerate(os.listdir(images)):
    img_name = copy.copy(img)
    img = Image.open(f"{images}/{img}")
    img = img.rotate(270)
    img.save(f'/Users/parker/Desktop/only_images/{img_name}')
    break