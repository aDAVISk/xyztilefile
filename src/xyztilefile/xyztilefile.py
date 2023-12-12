import os
from .xyzgeneric import *


class XYZTileFile:
    types = {}
    def __new__(cls, type=None):
        if type == "http":
            return XYZHttpTileFile()
        if type in cls.types:
            return cls.types[type]()
        return XYZgeneric()

class XYZHttpTileFile(XYZTileFile):
    types = {}
    def __new__(cls, type=None):
        if type in cls.types:
            return cls.types[type]()
        return XYZHttpGeneric()


for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module == "xyztilefile.py" \
        or module == "xyzgeneric.py" or module[-3:] != '.py':
        #or module[-3:] != '.py':
        #print("Pass")
        continue
    print(f"Importing {module}")
    exec("from .%s import *" % module[:-3])
    XYZTileFile.types.update(tiletype)
    XYZHttpTileFile.types.update(httptype)
del module

print(XYZTileFile.types)
