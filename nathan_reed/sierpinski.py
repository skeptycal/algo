# Sierpinski carpet generator, in Python using Numpy and Pillow.
# Written by Nathan Reed, June 2014.
# This code is released into the public domain.

import numpy as np
from PIL import Image

numLevels = 6
imageSize = 3**numLevels

# Create the image and fill it with white
img = np.empty([imageSize, imageSize, 3], dtype=np.uint8)
img.fill(255)
color = np.array([66, 0, 130], dtype=np.uint8)

for level in range(0, numLevels + 1):
	stepSize = 3**(numLevels - level)
	for x in range(0, 3**level):
		if x % 3 == 1:
			for y in range(0, 3**level):
				if y % 3 == 1:
					img[y*stepSize:(y+1)*stepSize, x*stepSize:(x+1)*stepSize] = color

	# Send to PIL and save
	outputFilename = "sierpinski%d.bmp" % level
	Image.fromarray(img).save(outputFilename)
	print('Wrote %s' % outputFilename)
