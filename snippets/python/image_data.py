#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" image_data.py """
from Pillow import Image


def image_data(filename: str):
    """ return image data for filename """
    try:
        im = Image.open(filename)
    except IOError:
        print("failed to identify", filename)
    else:
        print("image format:", im.format)
        print("image mode:", im.mode)
        print("image size:", im.size)
        if "description" in im.info:
            print("image description:", im.info["description"])


""" References:

http://effbot.org/zone/python-fileinfo.htm

Getting Information from Image Files
For an image file, you might be interested in things like image size, type of
image data, and compression ratio. The easiest way to get this information is
to use PIL’s identification mechanism. Simply call PIL’s open function, and
examine the resulting image object. This operation is usually fast, since PIL
only reads as much of the file as is necessary to determine what the file
contains, and how to read the image data proper. The actual image is not read
or decoded until it is actually needed.

The following example determines format, pixel type, and size of a given image
file:

from PIL import Image

try:
    im = Image.open(file)
except IOError:
    print("failed to identify", file)
else:
    print("image format:", im.format)
    print("image mode:", im.mode)
    print("image size:", im.size)
    if im.info.has_key("description"):
    print("image description:", im.info["description"])
You can derive other metrics from this information as well. For example, by
comparing the size of the image file with the size of the actual image data,
you can get a measure of the compression ratio for an image.


MODEBITS = {
    # bits per pixel for common PIL image modes
    "1": 1, "P": 8, "L": 8, "RGB": 24, "RGBA": 32, "CMYK": 32
}

try:
    bits = MODEBITS[im.mode]
    imagebytes = ((im.size[0] * bits + 7) / 8) * im.size[1]
    filebytes = os.stat(file)[ST_SIZE]
except (IOError, KeyError):
    print("failed to determine compression ratio for", file)
else:
    print("compression:", round(imagebytes / filebytes, 2), "times")
The compression ratio is close to 1 for non-compressed formats like BMP and PPM
typically 2-10 for GIF and other lossless compression formats, and 10-20 for
JPEG files. Note that as the expression is written, you won’t end up dividing
by zero since an empty file cannot possibly be a valid image file. If you
change the expression to get the compressed size in percent of the full size,
don’t forget that an image file may contain an empty image (imagebytes=0).
"""
