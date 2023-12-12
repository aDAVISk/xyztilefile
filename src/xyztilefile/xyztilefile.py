import os
from .xyzgeneric import *

class XYZTileFile:
    typeclass = {}
    def __new__(cls, type=None):
        if type == "http":
            return XYZHttpTileFile()
        if type in cls.typeclass:
            return cls.typeclass[type]()
        return XYZGeneric()

class XYZHttpTileFile(XYZTileFile):
    typeclass = {}
    def __new__(cls, type=None):
        if type in cls.typeclass:
            return cls.typeclass[type]()
        return XYZHttpGeneric()


for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module == "xyztilefile.py" \
        or module == "xyzgeneric.py" or module[-3:] != '.py':
        continue
    #print(f"Importing {module}")
    exec("from .%s import *" % module[:-3])
    XYZTileFile.typeclass.update(xyztiletype)
    XYZHttpTileFile.typeclass.update(xyzhttptype)
del module
del xyztiletype
del xyzhttptype

#print(XYZTileFile.typeclass)
