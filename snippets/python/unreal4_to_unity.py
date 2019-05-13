# http://trevorius.com/scrapbook/uncategorized/converting-unreal4-textures-to-unity/

import shutil
import os
import ctypes
import traceback

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from contextlib import contextmanager


@contextmanager
def edit(path):
    img = QImage(path).convertToFormat(QImage.Format_ARGB32)
    bits = ctypes.c_void_p(img.bits().__int__())
    bits = ctypes.cast(
        bits, ctypes.POINTER(ctypes.c_int * (img.width() * img.height())))[0]
    yield bits, img.width(), img.height()
    img.save(path)


def gather():
    textureSets = {}
    for name in os.listdir('.'):
        if not name.lower().endswith('.png'):
            continue
        key, sub = name.rsplit('_', 1)
        data = textureSets.get(key, [])
        data.append(sub)
        textureSets[key] = data

    # validate sets
    for name, members in textureSets.iteritems():
        if set(members) != set(
            ('BaseColor.png', 'Normal.png', 'OcclusionRoughnessMetallic.png')):
            raise RuntimeError('Unexpected texture set %s' % name)

    return textureSets


def convert(name):
    # copy maps
    shutil.copy(name + '_BaseColor.png',
                'Unity/%s/%s _MainTex.png' % (name, name))

    dst = 'Unity/%s/%s _BumpMap.png' % (name, name)
    shutil.copy(name + '_Normal.png', dst)

    # flip normal map green channel
    with edit(dst) as data:
        pixels, width, height = data
        for px in xrange(width * height):
            # invert green
            g = pixels[px] & 0x0000ff00
            g = (
                255 - (g >> 8)
            ) << 8  # overwrite green arb = pixels[px] & ~(0x0000ff00) pixels[px] = arb | g # split occlusion from roughness & metallic dst = 'Unity/%s/%s _OcclusionMap.png' % (name, name) shutil.copy(name + '_OcclusionRoughnessMetallic.png', dst) # occlusion can be in A8 format, make monochrome with edit(dst) as data: pixels, width, height = data for px in xrange(width * height): r = (pixels[px] & 0x00ff0000) pixels[px] = 0xff000000 | r | r >> 8 | r >> 16

    dst = 'Unity/%s/%s _MetallicGlossMap.png' % (name, name)
    shutil.copy(name + '_OcclusionRoughnessMetallic.png', dst)

    # unity metallic & smoothness live in R and A respectively
    with edit(dst) as data:
        pixels, width, height = data
        for px in xrange(width * height):
            g = pixels[px] & 0x0000ff00
            b = pixels[px] & 0x000000ff
            g = (255 - (g >> 8)) << 24
            pixels[px] = g | (b << 16)


def run():
    textureSets = gather()
    diag = QProgressDialog()
    diag.setMaximum(len(textureSets))
    diag.show()
    for i, name in enumerate(textureSets):
        diag.setLabelText('Converting: ' + name)
        diag.setValue(i)
        QApplication.processEvents()
        if diag.wasCanceled():
            break
        convert(name)


if __name__ == '__main__':
    app = QApplication([])
    try:
        run()
    except Exception as e:
        QMessageBox.critical(None, 'Error!',
                             e.message + '\n\n' + traceback.format_exc(e))
    app.exec_()
