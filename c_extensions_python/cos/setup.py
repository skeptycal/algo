# Ref: http://scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html

from distutils.core import setup, Extension

# define the extension module
cos_module = Extension('cos_module', sources=['cos_module.c'])

# run the setup
setup(ext_modules=[cos_module])
