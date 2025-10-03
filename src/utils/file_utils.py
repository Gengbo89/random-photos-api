import os
from glob import glob

def get_all_photos(directory):
    # Supported image extensions
    extensions = ('*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff')
    photos = []

    for ext in extensions:
        photos.extend(glob(os.path.join(directory, ext)))

    return photos