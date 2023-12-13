import os
from .xyzgeneric import *

class XYZTileFile:
    typeclass = {}
    def __new__(cls, base=None, **kwargs):
        if isinstance(base, str):
            if base[0:7] == "http://":
                return XYZHttpTileFile(base=base, **kwargs)
            type = os.path.splitext(base)[-1][1:]
            if type in cls.typeclass:
                return cls.typeclass[type](base=base, **kwargs)
        return XYZGeneric(base=base, **kwargs)

class XYZHttpTileFile(XYZTileFile):
    typeclass = {}
    def __new__(cls, base=None, **kwargs):
        if isinstance(base, str):
            if base[0:7] != "http://":
                return XYZTileFile(base=base, **kwargs)
            type = os.path.splitext(base)[-1][1:]
            if type in cls.typeclass:
                return cls.typeclass[type](base=base, **kwargs)
        return XYZHttpGeneric(base=base, **kwargs)


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
