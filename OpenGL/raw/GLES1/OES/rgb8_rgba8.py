'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES1 import _types as _cs
# End users want this...
from OpenGL.raw.GLES1._types import *
from OpenGL.raw.GLES1 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES1_OES_rgb8_rgba8'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES1,'GLES1_OES_rgb8_rgba8',error_checker=_errors._error_checker)
GL_RGB8_OES=_C('GL_RGB8_OES',0x8051)
GL_RGBA8_OES=_C('GL_RGBA8_OES',0x8058)

