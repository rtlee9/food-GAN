from PIL import Image
import glob
from os import path
import config

# read existing blacklist
if path.exists(config.path_blacklist):
    with open(path.join(config.path_base, 'blacklist.txt'), 'r') as f:
        blacklist = f.readlines()
else:
    blacklist = []

# try opening all images, save error-generating images to blacklist
for filename in glob.glob(path.join(config.path_img, '*')): #assuming gif
    try:
        im=Image.open(filename)
    except OSError:
        basename = path.basename(filename)
        print('Adding {} to blacklist'.format(basename))
        blacklist.append(basename)

# write resulting blacklist to disk
with open(path.join(config.path_base, 'blacklist.txt'), 'w') as f:
    blacklist = f.write('\n'.join(blacklist) + '\n')
